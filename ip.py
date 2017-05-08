from socket import*
print  ('Descobrir endereço IP de um site')
alvo = input("Digite o Host: ")
IPalvo =  gethostbyname(alvo)
print ('O IP do alvo é: ', IPalvo)

