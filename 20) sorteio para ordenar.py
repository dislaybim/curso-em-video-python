#aqui vamos criar uma lógica semelhante ao programa anteror
#so que aqui vamos determinar uma ordem, dentro de uma lista que iremos criar
import random  #importo a biblioteca random

nomes = []  #lista vazia para adicionar valore

for i in range(0, 4):  #quatroiterações
  pessoa = input("adicione: ")  #para adicionar nome de pessoas
  nomes.append(pessoa)  #na lista

random.shuffle(nomes)  #função da biblioteca para selecionar ordem arbitrária
sequencia = random.sample(nomes, 4)  #outra ordem de mesmo propósito

print(nomes)  #e aqui temos as telas de printe do sistema
print(sequencia)