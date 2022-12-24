import dns.resolver
import sys
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import wait

host = sys.argv[1]
wlist = sys.argv[2]

record_types = ['A', 'AAAA', 'CNAME', 'MX', 'PTR', 'SOA', 'HINFO', 'TXT']
universal_list = []

def read_list():
    open_file = open(wlist, 'r')
    for word in open_file:
        universal_list.append(word.rstrip('\n'))

def start_subscan():
    with ThreadPoolExecutor(30) as executor:
        print("------------- subdomain ---------------")
        sub_scan = [executor.submit(sub_domain_scan, word) for word in universal_list]
        wait(sub_scan)
        print("------------- possible Takeover ---------------")
        take_scan = [executor.submit(possible_takeover, word) for word in universal_list]
        wait(take_scan)
        print("------------- DNS RECON ---------------")
        dns_scan = [executor.submit(dns_recon, word) for word in universal_list]

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
        except KeyboardInterrupt:
            quit()
def possible_takeover(word):
    try:
        answer = dns.resolver.resolve(f'{word}.{host}', 'CNAME')
        for record in answer:
            print(f'{word}.{host} -> {record.to_text()}')
    except dns.resolver.NXDOMAIN:
        pass
    except dns.resolver.NoAnswer:
        pass
    except KeyboardInterrupt:
        quit()

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
        except KeyboardInterrupt:
            quit()

def main():
    read_list()
    start_subscan()
main()
