import csv

#removendo caracteres especiais
def format(string):
    x = ["\\r","\\n","\\t","{","}","[","]","%"]

    for w in x:
        string = string.replace(w, "")

    return string

#criando um novo arquivo csv
def makeFile(string):
    with open('/media/sf_vm_share/dados.csv', 'a') as arquivo:
        arquivo.write(string+"\n")

#lendo o arquivo original
with open('/media/sf_vm_share/dados.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
    for row in reader:
        makeFile(format(str(row['message'].strip())))

        print(format(str(row['message'].strip()))+"\n")
