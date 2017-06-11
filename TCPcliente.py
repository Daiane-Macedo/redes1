"""
Lado do cliente: Usa sockets para mandar dados para o servidor, e imprime
a resposta do servidor para cada linha na mensagem.
"""

from socket import *

# Configurações de conexão do servidor

serverHost = 'localhost' #"localhost' indica que o servidor está na mesma máquina
serverPort = 5000 #porta do servidor

print("Entre com a mensagem a ser enviada")
mensagem=input()

# A menssagem a ser enviada condificada é codificada em bytes
mensagem = bytes (mensagem,'ascii')
mensagem = [b''+mensagem]

sockobj = socket(AF_INET, SOCK_STREAM) #Criando o socket
sockobj.connect((serverHost, serverPort)) #conectando ao servidor

# Manda a menssagem linha por linha
for linha in mensagem:
    sockobj.send(linha)
    # Depois de mandar uma linha espera uma resposta
    # do servidor
    resp = sockobj.recv(1024)
    print(resp) #resp = resposta

# Fecha a conexão
sockobj.close()
