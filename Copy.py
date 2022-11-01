#Importando Bibliotecas
import shutil
import subprocess
import time
import os

#copiando o arquivo de instalação
source = "\\source.txt"
destination = "C:\\temp\\teste.txt"
shutil.copyfile(source,destination)

#executando o script
subprocess.Popen('powershell.exe -ExecutionPolicy Bypass -command C:\\temp\\teste.txt')

#aguardando a execução
time.sleep(60)

#remover script
os.remove("C:\\temp\\teste.txt")
