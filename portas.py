import socket
ip = input("IP/DNS alvo: ")
aux = True
print ("Digite 0 para sair")
while aux:
    print("")
    port = int(input("Testar porta: "))
    if(port == 0):
        aux = False
        break
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.settimeout(0.9)
    conexao = cliente.connect_ex((ip, port))
    if conexao == 0:
        print (str(port) + " > porta aberta")
    else:
        print (str(port) + " > porta fechada")
