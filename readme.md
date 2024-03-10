# 💻 What is this

> A multithread dns scanner that shows subdomains of a host, possible subdomains vulnerable to "Subdomain Takeover" and DNS records for each subdomain.

## 📃 Requirements

- `Python 3.10.x`

## 🚀 Installation

* To install **DnScan** follow the steps

```
git clone https://github.com/ArthurHydr/DnScan.git
```
* To install requirements: (dnspython)
```
pip3 install -r requirements.txt
```
## ☕ Use

### To run DnScan:

```
python3 app.py <host> <wordlist> (subdomains.txt wordlist, in repository)
params: 
  --flags <dns flag> DEFAULT: ALL
  --threads <n threads>
  --scan {subdomain,takeover,recon,all} DEFAULT: ALL
```

## 📫 Contribuite

### To contribute to chip-8, follow these steps

1. Fork this repository.
2. Create a branch: `git checkout -b <branch_name>`.
3. Make your changes and commit them: `git commit -m '<message_commit>'`
4. Push to the original branch: `git push origin <project_name> / <local>`
5. Create the pull request

Alternatively, see the GitHub documentation at: [how to create a pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

## 🤝 Contribuitors

We thank the following people who contributed to this project:

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/ArthurHydr">
        <img src="https://avatars3.githubusercontent.com/u/61481946" width="100px;" alt="Arthur Ottoni on GitHub"/><br>
        <sub>
          <b>Arthur Ottoni</b>
        </sub>
      </a>
    </td>
     <td align="center">
      <a href="https://github.com/Garoze">
        <img src="https://avatars.githubusercontent.com/u/63270057" width="100px;" alt="Garoze on GitHub"/><br>
        <sub>
          <b>Garoze</b>
        </sub>
      </a>
    </td>
  </tr>
</table>
