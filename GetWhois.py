#!/usr/bin/python

#Script para automatizar a consulta ao WHOIS
#Autor: Izael Magalhaes - 17.10.2022
#Modo de uso: python getWhois.py lista.txt
##nao deixar o nome do arquivo como whois.py, pois causa conflito entre as bibliotecas##

#importando bibliotecas
import os
import sys
import re
import whois

if os.path.isfile("whois_temp.txt"):
    os.remove("whois_temp.txt")

if os.path.isfile("result_whois.txt"):
    os.remove("result_whois.txt")

file = open(sys.argv[1],'r')
conteudo = file.readlines()

#Temp Whois
def tempWhois(string):
    report = open('whois_temp.txt', 'w')    
    report.write(string.strip())

#GetName
def getName(string):
    temp_whois = open('whois_temp.txt', 'r')
    result_temp_whois = temp_whois.readlines()
    for line in result_temp_whois:
        
        if re.search(string, line):
            name=line.strip()
            break
        else:
            name="#:#"
        
    array_country = name.split(":")        
    ct = array_country[1].strip()
    return ct

#Insert Data
def insertData(host,string):    
    report = open("result_whois.txt", 'a')    
    report.write(host.strip()+";"+string.strip()+"\n")

cont = 0
querys = ["owner:", "Organization:", "NetName:"]

for host in conteudo:
    result = whois.whois(host.strip())    
    
    tempWhois(result.text)

    cont = cont+1  

    for q in querys:
        if getName(q) != "#":
            insertData(host.strip(),getName(q))
            print(str(cont)+";"+host.strip()+";"+getName(q))
            break
        else:
            insertData(host.strip(),"Blank")
            print(str(cont)+";"+host.strip()+";Blank")
