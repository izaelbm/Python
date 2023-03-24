import requests
import time
import random
import sys

#GetUserAgent
def GetUserAgent():
    array = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36', 'Mozilla/5.0 (Linux; Android 12; moto g(60) Build/S2RIS32.32-20-7-7; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.117 Mobile Safari/537.36 PKeyAuth/1.0', 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; Zoom 3.6.0; Zoom 3.6.0; Microsoft Outlook 15.0.5399', 'BAV2ROPC']
    
    agent = random.choice(array)

    return agent

#GetUserAgent
def GetIp():
    array = [
        '189.58.137.2',
        '179.157.234.240',
        '156.96.154.75',
        '45.221.8.198',
        '191.32.68.18',
        '186.231.28.186',
        '200.186.180.70',
        '179.191.82.82',
        '127.0.0.1'
    ]
    
    ip = random.choice(array)

    return ip


# Lendo o arquivo texto
file = open('/usr/share/wordlists/dirb/common.txt', 'r')
result = file.readlines()

url = sys.argv[1]

print("##############")
print("# DirSearch - By izaelbm")
print("# Script para bruteforce de diretorios , user agent e ip de origem randomico")
print("##############")
print(f"# Scaneando o FQDN:",{url})
print("##############")
#Percorrendo o arquivo 
for line in result:
    payload = line.strip()

    send = url + payload

    headers = {
        'X-Forwarded-For': '127.0.0.1',
        'User-Agent': 'GetUserAgent()'      
    }

    headers['User-Agent'] = GetUserAgent()
    headers['X-Forwarded-For'] = GetIp()
    
    #Realizando a requisição HTTP e obtendo o código de resposta
    http_response = requests.get(send, headers=headers)
    codigo_http = http_response.status_code

    if codigo_http == 200:
        #Imprimindo o código de resposta HTTP
        print(f'{send} -> [{codigo_http}]')
        
    time.sleep(5)

print('Pesquisa Concluida')  
