#programinha da hora
x=int(input("voce quer armazenar quantos valores? "))
lista=[]

for i in range(0,x):
   valor=int(input("digite o valo da posição [{}]: ".format(i)))
   lista.append(valor)

maior=[]
max=max(lista)
print(max)

for c in range(0,x):
  if(max==lista[c]):
    maior.append(c)


r=len(maior)

menor=[]
min=min(lista)

for d in range(0,x):
  if(min==lista[d]):
    menor.append(d)

l=len(menor)


print("o maior valor é {}".format(max))
for i in range(0,r):
  print("[{}] >>> ".format(maior[i]), end='')

print("\n\n")

print("O menor valo é {}".format(min))
for i in range(0,l):
  print("[{}] >>> ".format(menor[i]), end='')
    