#sorteando dado e ranqueando os 4 ganhadores
import random
from operator import itemgetter

dicionario={}#dicionario vazio

for i in range(0,4):
  dicionario["jogador {}".format(i+1)]=random.randint(1,6)

print(dicionario)

for chave in dicionario:
  print(chave)
  #OUTPUT
  #jogador 1
  #jogador 2
  #jogador 3
  #jogador 4

for k, v in dicionario.items():
  print("{} tirou {} no dado".format(k,v))
  #OUTPUT
  #AQUI TEREMOS UM PRINT DE UMA FORMA UM POUCO MAIS DIFERENTE.
rank=dict()#dicionario vazzio

rank=sorted(dicionario.items(),key=itemgetter(1))#nesse dicionario vazio conseguimos ordenar o dicionarionario anterior por meio da função sort, que será parametrizada pela função itemgetter(), no final esse dicionario se tornará uma lista

print("-=-"*10)
print("      RANKING\n")

for k,v in enumerate(rank):
  print(f"{k+1}° lugar: {v[0]} com {v[1]}.")
#esse print será formada pela iteração for, com a função enumerate() que será definido pelos parametros k e v, na qual é o meio para acessar os valores da lista organizada pot tuplas, e assim printa-las



