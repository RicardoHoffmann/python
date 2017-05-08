import re, os

os.system("cls")

print ('Verificando IP em rede interna')
for i in range(100, 256):
    num = str(i)
    cmd = 'ping -n 1 192.168.43.'+ num
    print ("Testando IP -> 192.168.43."+num)
    r = "".join(os.popen(cmd).readlines())

    if re.search('Resposta de',r):
        print ('IP ativo')
    else:
        print('IP Inativo')
