print("-=-"*10)
print("      \33[31mPAR OU ÍMPAR")
print("\33[m-=-"*10)#aqui criamos um menu

#vamos criar uma função de entrada e armazenar em uma variável
numero=int(input("digite um número: "))

if numero%2==0:
  print("O número {} é \33[31mPAR!!!".format(numero))
else:
  print("\33[mO número {} é \33[34mÍMPAR!!!".format(numero))
