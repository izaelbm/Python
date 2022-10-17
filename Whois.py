#!/usr/bin/python

#Script para automatizar a consulta ao WHOIS
#Autor: Izael Magalhaes - 17.10.2022
#Modo de uso: python getWhois.py lista.txt
##nao deixar o nome do arquivo como whois.py, pois causa conflito entre as bibliotecas##

#importando bibliotecas
import os
import sys
import re
import whois #pip install python-whois

#removendo arquivos temporarios
os.remove("whois_temp.txt")
os.remove("result_whois.txt")

#lendo a lista de hosts
file = open(sys.argv[1],'r')
conteudo = file.readlines()

#Temp Whois
def tempWhois(string):
    report = open('whois_temp.txt', 'w')    
    report.write(string.strip())

#GetName
def getName():
    temp_whois = open('whois_temp.txt', 'r')
    result_temp_whois = temp_whois.readlines()
    for line in result_temp_whois:
        if re.search('owner:', line):
            name=line.strip()
            break
        elif re.search('Organization:', line):
            name=line.strip()
            break
        elif re.search('NetName:', line):
            name=line.strip()
            break
        elif re.search('Domain Name:', line):
            name=line.strip()
            break

    array_country = name.split(":")        
    ct = array_country[1].strip()
    return ct

#Insert Data
def insertData(host,string):    
    report = open("result_whois.txt", 'a')    
    report.write(host.strip()+";"+string.strip()+"\n")

#lendo os hosts
cont = 0
for host in conteudo:
    result = whois.whois(host.strip())    
    
    tempWhois(result.text)

    cont = cont+1

    if getName():
        insertData(host.strip(),getName())
        print(str(cont)+";"+host.strip()+";"+getName())
    else:        
        insertData(host.strip(),"Blank")
        print(str(cont)+";"+host.strip()+";Blank")
