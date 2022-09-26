#!/usr/bin/env python


import socket


address_to_server = ('localhost', 8686)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(address_to_server)

client.send(bytearray("Hello world", encoding='UTF-8'))
client.close()
