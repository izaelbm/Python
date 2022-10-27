import urllib
import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

def makeLog(string):
    name_file = "log.txt"
    report = open(name_file, 'a')    
    report.write(string+"\n")


methods = ["http://", "https://"]

file = open('hosts.txt', 'r')
hosts = file.readlines()
for line in hosts:
    for mtd in methods:           
        site = mtd + line

        try:
            site1=urllib.request.urlopen(site)
        except urllib.request.URLError:
            makeLog(str("[NOK] - Indisponivel - "+site))
            print("[NOK] - Indisponivel - "+site)
        else:
            makeLog(str("[OK] - Disponivel - "+site))
            print("[OK] - Disponivel - "+site)
