import requests
import json

url = "https://graph.microsoft.com/v1.0/me/drive/items/#id_dir#/children"

payload={}
headers = {
  'Authorization': 'Bearer #token#}

response = requests.request("GET", url, headers=headers, data=payload)
list_json = json.loads(response.text)

for file in list_json['value']:
    print("[ID -> " + file['id'] + " ] [Name -> " + file['name'] + " ]")

  
  #other option
  
  # -*- coding: utf-8 -*-
import urllib
import urllib2
import json

# Definir as informações de autenticação
client_id = '#client_id#'
client_secret = '#client_secret#'
tenant_id = '#tenant_id#'

# Fazer uma solicitação para obter um token de acesso
auth_url = 'https://login.microsoftonline.com/{}/oauth2/v2.0/token'.format(tenant_id)
auth_data = {
    'client_id': client_id,
    'client_secret': client_secret,
    'grant_type': 'password',
    'username': 'email@micro.com',
    'password': 'password',
    'scope': 'https://graph.microsoft.com/Files.Read.All'
}
auth_headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}
auth_data_encoded = urllib.urlencode(auth_data)
auth_request = urllib2.Request(auth_url, auth_data_encoded, auth_headers)
auth_response = urllib2.urlopen(auth_request)
auth_response_data = json.loads(auth_response.read())
access_token = auth_response_data['access_token']

# Listar todos os arquivos e pastas
list_url = 'https://graph.microsoft.com/v1.0/me/drive/items/#id_dir#/children'
list_headers = {'Authorization': 'Bearer ' + access_token}
list_request = urllib2.Request(list_url, headers=list_headers)
list_response = urllib2.urlopen(list_request)
list_json = json.loads(list_response.read())

for file in list_json['value']:
    print("[ID -> " + file['id'] + " ] [Name -> " + file['name'] + " ]")
