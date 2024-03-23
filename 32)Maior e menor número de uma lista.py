#o objetivo do programa é criar um algoritimo que armazene uma quantidade de números em uma lista e diga qual o maior e menor valor

quantidade=int(input("quantos numeros você quer agrupar? "))
lista=[]#lista vazia

#criar um laçopen
for i in range(0,quantidade):#criar lista
  numero=int(input("digite um número: "))
  lista.append(numero)

print(lista)
#criar uma função, que ordene essa lista de forma crescente, assim 
lista.sort()
print("O MENOR NÚMERO É {}".format(lista[0]))
print("O MAIOR NÚMERO É {}".format(lista[quantidade-1]))