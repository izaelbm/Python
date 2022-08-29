#!/usr/bin/python

#Script para capturar o ip do host
#By Izael Magalhaes
#izaelbm.com.br
#25/08/2022

#*** Conhecimento não é crime, porem o que você fara com ele é de sua responsabilidade..... ***

#importando bibliotecas    
from ping3 import ping
import os

#check host
def checkping(host):
    resp = ping(host)

    if resp == False:
        return False
    else:
        return True

def numLines(file):
    with open(file) as count:
        return  sum(1 for line in count)

sumLine = numLines("hosts.txt")

#lendo a base de hosts
with open("hosts.txt","r", encoding="utf-8") as file:
    hosts = file.readlines()

for host in hosts:
    
    percent = "0"    

    if hosts.index(host) > 1:
        percent = format((hosts.index(host)/sumLine) * 100, '.1f') 

    #escrevendo na tela
    os.system("cls")
    print("====================================")
    print("By Izael Magalhaes")
    print("====================================")
    print("Progresso: " + str(percent) + "%")
    print("====================================")
    os.system("type log.txt")

    if checkping(host.strip()):
        rs_os = os.popen("ping -4 -c 1 "+host).read()

        str1 = rs_os.split("[",1)
        str2 = str1[1].split("]")

        txt = str(hosts.index(host)) + ";" + str(checkping(host.strip())) + ";" + str2[0]  
        print(txt.strip())
    else:
        txt = str(hosts.index(host)) + ";" + str(checkping(host.strip())) + ";" + "FORA"
        print(txt.strip())
    
    log_file = open('log.txt', 'a')    
    log_file.write(txt)
