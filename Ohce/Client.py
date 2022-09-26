#!/usr/bin/env python


import socket
from random import randrange

address_to_server = ('localhost', 8686)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(address_to_server)

lines = "\n".join([str(randrange(0, 10**40)) for i in range(40)])
print(lines)

client.send(lines.encode("utf-8"))
client.close()

if __name__ == "__main__":
    pass
