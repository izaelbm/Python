# -*- coding: utf-8 -*-
import urllib
import urllib2
import json

# Definir as informações de autenticação
client_id = '#client_id#'
client_secret = '#secret#'
tenant_id = '#tenant_id#'
access_token = ''

# Definir as informações do arquivo a ser baixado
file_id = itsm.getParameter('file_id')
#'file-id'
file_name = itsm.getParameter('file_name')
#'name.zip'

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

# Fazer uma solicitação para baixar o arquivo
download_url = 'https://graph.microsoft.com/v1.0/drives/me/items/{}/content'.format(file_id)
download_headers = {
    'Authorization': 'Bearer {}'.format(access_token)
}
download_request = urllib2.Request(download_url,None, headers=download_headers)
download_response = urllib2.urlopen(download_request)

dir_local = itsm.getParameter('temp_dir')
#"C:\\temp\\"

# Salvar o arquivo localmente
with open(dir_local + file_name, 'wb') as f:
    f.write(download_response.read())
