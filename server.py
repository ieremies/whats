#!/usr/bin/env python3
"""
Módulo do servidor usado para demonstrar multiplay com Pygame.

Fonte: https://www.techwithtim.net/tutorials/python-online-game-tutorial/server
"""

import socket
from _thread import *
from sys import argv

# Lembre de pegar essas informações usando o comando ipconfig
# O valor que queremos está em IPv4 Adress. . . . . . . . . .
if len(argv) > 1:
    server = argv[1]
else:
    server = "192.168.0.109"  # COLOQUE AQUI SEU IP
port = 5555  # número da porta

# Cria um objeto do tipo Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Tenta "bindar"
    s.bind((server, port))
except socket.error as e:
    # Se não conseguir, imprime o erro
    print(str(e))
    exit()


def threaded_client(connection):
    """
    Função que irá processar a conexão com o cliente.
    Haverá uma função dessas rodando para cada conexão aberta.
    """
    # Comando para enviar uma mensagem *pequena*
    connection.send(str.encode(f"Connected!"))
    msg = ""

    # Continua a escutar a conexão passada
    while True:
        try:
            # Recebe a informação e "decodifica"
            data = connection.recv(2048)
            msg = data.decode("utf-8")

            if msg == "":
                break

            print("<<", msg)
        except:  # Se alguma coisa falhar no processo
            break

    # Quando sairmos do laço, podemos fechar a conexão
    print("Lost connection")
    connection.close()


def receiver():
    # Começamos a escutar mensagens no socket!
    s.listen()
    print(f"Waiting for a connection at {server}:{port}")

    # Escuta por qualquer solicitação de conexão no socket
    while True:
        # s.accept() devolve dois valores:
        # - a conexão aceita;
        # - o endereço de onde ela veio;
        connection, address = s.accept()
        print("Connected to:", address)

        # Spawnamos uma nova thread
        start_new_thread(threaded_client, (connection,))
