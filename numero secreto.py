#quebrando número
#import random
#nomes = [] #criei uma lista vazia
#for i in range(0,7):
 # nomes.append(input("digite o nome: "))#adicionar elementos na #lista
#print(nomes)
import random
import math

numero_secreto = random.randint(1, 100)
maximo_tentativas = 5
tentativas = []

for tentativa in range(maximo_tentativas):
    palpite = int(input("Digite um número entre 1 e 100: "))
    tentativas.append(palpite)
    
    if palpite == numero_secreto:
        print("Parabéns! Você acertou o número secreto em {} tentativas.".format(len(tentativas)))
        break
    elif palpite > numero_secreto:
        print("O número secreto é menor do que {}. Tente novamente.".format(palpite))
    else:
        print("O número secreto é maior do que {}. Tente novamente.".format(palpite))
        
if len(tentativas) == maximo_tentativas:
    print("Que pena! Você atingiu o número máximo de tentativas. O número secreto era {}.".format(numero_secreto))
    
print("Suas tentativas foram: {}".format(tentativas))

  






