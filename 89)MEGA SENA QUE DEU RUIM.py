print("-=-"*10)
print("      MEGA-SENA")
print("-=-"*10)
import random

quantidade = int(input("Quantidade de jogos: "))

lista = [[0 for j in range(6)] for i in range(quantidade)]

for j in range(0, quantidade):
    for i in range(0, 6):
        lista[j][i] = random.randint(0, 60)
        
# Imprime a matriz completa
cont=0
for j in range(0,quantidade):
  for i in range(0,6):
    con=cont+1
    print("O jogo {}={},".format(j+1,lista[j][i]), end='')
    if cont==5:
      print("\n")
      cont=0