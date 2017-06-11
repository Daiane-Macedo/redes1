"""
Lado do Servidor: Abre um TCP/IP numa porta, espera por uma menssagem
de um cliente, e envia uma mensagem de confirmação de volta. Esse
é uma simples ouve/responde conversação por cliente, mas percorre um loop
infinito para ouvir por mais clientes enquanto o script do servidor
estiver rodando. O cliente pode rodar em outra máquina ou no mesmo
computador se usar o 'localhost' como servidor
"""

from socket import *
import time

# Cria o nome do host
host = ''

# Utiliza este número de porta
porta = 5000

# Cria um objeto socket. As duas constantes referem-se a:
# Familia do endereço (padrão é socket.AF_INET)
# Se é stream (socket.SOCK_STREAM, o padrão) ou datagram (socket.SOCK_DGRAM)
# E o protocolo (padrão é 0)
# Da maneira como configuramos:
# AF_INIT == Protocolo de endereço de IP
# SOCK_STREAM == Protocolo de transferência TCP
# Combinação = Server TCP/IP
sockobj = socket(AF_INET, SOCK_STREAM)

# Vincula o servidor ao número de porta
sockobj.bind((host, porta))

# O socket começa a esperar por clientes limitando a 
# 5 conexões por vez
sockobj.listen(5)


while True:
    # Aceita uma conexão quando encontrada e devolve
    # um novo socket conexão e o endereço do cliente
    # conectado
    conexão, endereço = sockobj.accept()
    print('Server conectado por', endereço)
    
    while True:
        # Recebe data enviada pelo cliente
        data = conexão.recv(1024)
        # time.sleep(3)
        
        # Se não receber nada para o loop
        if not data: break

        # O servidor manda de volta uma resposta
        conexão.send(b'Servidor recebeu: '+ data)
    
    # Fecha a conexão criada depois de responder o
    # cliente
    conexão.close()
