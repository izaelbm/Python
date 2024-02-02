# -*- coding: utf-8 -*-
import urllib
import urllib2
import json
import zipfile
import subprocess
import os
import shutil

def getToken():

    # Definir as informações de autenticação
    client_id = '123123'
    client_secret = '123123'
    tenant_id = '123123'
    access_token = ''

    # Fazer uma solicitação para obter um token de acesso
    auth_url = 'https://login.microsoftonline.com/{}/oauth2/v2.0/token'.format(tenant_id)
    auth_data = {
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': 'password',
        'username': 'email@email.com',
        'password': '123123123',
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

    return access_token


def getFile(file_id,file_name,dir):

    access_token = getToken()
    # Fazer uma solicitação para baixar o arquivo
    download_url = 'https://graph.microsoft.com/v1.0/drives/me/items/{}/content'.format(file_id)
    download_headers = {
        'Authorization': 'Bearer {}'.format(access_token)
    }
    download_request = urllib2.Request(download_url,None, headers=download_headers)
    download_response = urllib2.urlopen(download_request)

    dir_local = dir

    # Salvar o arquivo localmente
    with open(dir_local + file_name, 'wb') as f:
        f.write(download_response.read())


def install(command):
    
    command_start = command

    # Iniciando o processo
    try:
        process_start = subprocess.Popen(command_start, shell=True, stdout=subprocess.PIPE)
        process_start.wait()  # Espera o comando terminar
        print("Comando executado com sucesso.")
    except OSError as e:
        print("Erro ao executar o comando:", e)


def is_software_installed(file):
    # Monta o comando para procurar pela instalação do software
    comando = 'wmic product where "Name LIKE \'%%%s%%\'" get Name' % file
    
    try:
        # Executa o comando e captura a saída
        resultado = subprocess.check_output(comando, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
        
        # Verifica se a saída contém algum nome de programa
        if "No Instance(s) Available." in resultado or "Name" not in resultado:
            return False
        else:
            return True
    except subprocess.CalledProcessError as e:
        print "Erro ao executar o comando: ", e

#Validando se o software ja esta instalado e realizando a instalacao caso necessario
if is_software_installed('name SW'):
    print("Software ja instalado.")
else:
    #fazendo o Download do Arquivo
    getFile(str('idfile'),str('file.exe'),str('C:/temp/'))
    
    #instalando
    cmd = str('cmd command')
    install(cmd)
