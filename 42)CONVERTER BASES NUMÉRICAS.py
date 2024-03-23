#conversor de bases

x=int(input("digite o numero a ser convertido: "))
escolha=input("\nESCOLHA PARA QUAL BASE VOCÊ QUER CONVERTER\n(a)BINÁRIO\n(b)HEXADECIMAL\n(c)OCTAL\nDigite aqui o caractere: ")
if escolha=='a':
  sistema=bin(x)
  print(binario)
elif(escolha=='b'):
  sistema=hex(x)
  print(sistema)
elif(escolha=='c'):
  sistema=oct(x)
  print(sistema)
else:
  print("ERRO!\nutilise o caractere correto")