#!/usr/bin/python

#importando as bibliotecas
import os
import readline
import hashlib
import base64

#base64
def base64Encode(string):
    str_b64 = string.encode("UTF-8")
    str_b64 = base64.b64encode(str_b64)        
    return str_b64.decode()

#md5
def md5sum(string):
    print('asad')

def makeList(string):
    seclist = open('./wordlist_centos.txt','a')
    seclist.write(string+"\n")

#Temp Whois
seclist = open('/usr/share/seclists/Passwords/Common-Credentials/100k-most-used-passwords-NCSC.txt', 'r')
array = seclist.readlines()

for line in array:
    nwpass = "infrapositec:"+str(line)
    pass_64 = base64Encode(nwpass)
    
    makeList(pass_64)

    print(nwpass.strip()+" - "+pass_64.strip()+"\n")
