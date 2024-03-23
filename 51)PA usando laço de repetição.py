#progressão Aritimética

#escolher a quantidade de termos para a PA

quantidade=int(input("quantidade de termos: "))

#primeiro termo da PA
primeiro=int(input("primeiro termo da PA: "))

#Razão da PA
razao=int(input("Razão da PA: "))
cont=1
print(primeiro)
while cont != quantidade:
  elemento=(cont*razao)+primeiro
  print(elemento)
  cont=cont+1
  
  
  

