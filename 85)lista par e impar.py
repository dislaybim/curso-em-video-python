#lista que cadastre 7 valores numericos

par=[]
impar=[]

for i in range(0,7):
  valor=int(input("adicione: "))
  if valor % 2 == 0:
    #é par
    par.append(valor)
  else:
    #é impar
    impar.append(valor)

par.sort()#colocar em ordem crescente
impar.sort()#colocar em ordem crescente

print(par)
print(impar)

  