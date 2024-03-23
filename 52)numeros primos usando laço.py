#programa de verificar se um número é

numero=int(input("digite um número: "))
divisiveis=[]
cont=0
for i in range(1,numero+1):
  print("{} ".format(i), end='')
  if numero % i == 0:
     print("\033[m")
     divisiveis.append(i)
     cont=cont+1

if cont == 2: 
  print("é primo")
else:
  print("não é primo")
