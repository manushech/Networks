#!/usr/bin/env python

import socket

# Задаем адрес сервера
SERVER_ADDRESS = ('localhost', 8686) #create ip and port

# Настраиваем сокет
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create socket
server_socket.bind(SERVER_ADDRESS) #bind adress and socket
server_socket.listen(1) #listen one socket
print('server is running, please, press ctrl+c to stop')

# Слушаем запросы
while True:
    connection, address = server_socket.accept()

    data = connection.recv(1024) # ждёт пока сервер не отправит 1024 байт
    print(data.decode('utf-8') + "\n")  # декодирование принятых данных
    connection.close()
    break
