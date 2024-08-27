#!/usr/bin/env python3
"""
Móduglo de rede para o jogo.

Fonte: https://www.techwithtim.net/tutorials/python-online-game-tutorial/sending-receiving-information
"""

import socket


def sender(ip_address):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    address = (ip_address, 5555)

    try:
        client.connect(address)
        print(client.recv(2048).decode())
    except:
        print("Connection failed")
        exit()

    while True:
        try:
            client.send(str.encode(input(">> ")))
        except socket.error as e:
            print(e)
            break
