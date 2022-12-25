import sys
import dns.resolver

from concurrent.futures import wait
from concurrent.futures import ThreadPoolExecutor

host = sys.argv[1]
wlist = sys.argv[2]

universal_list = []
record_types = ['A', 'AAAA', 'CNAME', 'MX', 'PTR', 'SOA', 'HINFO', 'TXT']

def gen_banner():
    print(""" 
+=================================================================+
|              ######     ######              #          ######   |
|   #######                                   #   ###             |
|      #     ########## ##########   ##       ####     ########## |
|      #     #        #      #      #  ##     #        #        # |
|      #            ##       #     #     ##   #               ##  |
|      #          ##        #              ## #             ##    |
| ##########    ##        ##                   #######    ##      |
+=================================================================+                                                             
| Made By: Arthur Ottoni --> github.com/arthurhydr/DnScan         |
+=================================================================+
            """)

def read_list():
    open_file = open(wlist, 'r')
    for word in open_file:
        universal_list.append(word.rstrip('\n'))

def start_subdomain_thread():
    with ThreadPoolExecutor(50) as executor:
        scan = [executor.submit(sub_domain_scan, word) for word in universal_list]
        wait(scan)

def start_takeover_thread():
    with ThreadPoolExecutor(50) as executor:
        scan = [executor.submit(possible_takeover, word) for word in universal_list]
        wait(scan)

def start_dns_resolve_thread():
    with ThreadPoolExecutor(50) as executor:
        scan = [executor.submit(dns_recon, word) for word in universal_list]
        wait(scan)

def sub_domain_scan(word):
    try:
        ip_value = dns.resolver.resolve(f'{word}.{host}', 'A')
        if ip_value:
            print(f'{word}.{host}')
        else:
            pass
    except dns.resolver.NXDOMAIN:
        pass
    except dns.resolver.NoAnswer:
        pass

def possible_takeover(word):
    try:
        answer = dns.resolver.resolve(f'{word}.{host}', 'CNAME')
        for record in answer:
            print(f'{word}.{host} -> {record.to_text()}')
    except dns.resolver.NXDOMAIN:
        pass
    except dns.resolver.NoAnswer:
        pass

def dns_recon(word):
    for record in record_types:
        try:
            answer = dns.resolver.resolve(f'{word}.{host}', record)
            for data in answer:
                print(f'{word}.{host}  {record}  ->', data.to_text())
        except dns.resolver.NoAnswer:
            pass
        except dns.resolver.NXDOMAIN:
            pass

def main():
    gen_banner()
    read_list()
    
    try:    
        print("\n------------- Subdomain ---------------")
        start_subdomain_thread()
        print("\n------------- Possible Takeover -------------")
        start_takeover_thread()
        print("\n------------- DNS Recon -------------")
        start_dns_resolve_thread()
    except KeyboardInterrupt:
        quit()

if __name__ == '__main__':
    main()
