#jogo de adivinhação
#crio o menu do joguito:
#crio um laço de condição if e else no qual, vai iterar 5 vezes, no propósito de me darchances de tentar descobrir o número sorteado no inicio
#pela função random
import random
#primeiramente, vamos sortear o número arbitrário
sorteio=random.randint(0,3)#essa é a função específica para gerar tal número

for i in range(0,6): #INDICA QUE VAMOS REALIZAR 5 TENTATIVAS
  if(i==5):
    print("VOCÊ PERDEU, O NÚMERO CORRETO É {}".format(sorteio))
  
  numero=int(input("digite seu número: "))
  if(numero == sorteio):
        print("PARABENS!!! ACERTOU\nO NÚMERO DA SORTE É {}.".format(sorteio))
        
  elif(numero > sorteio):
        print("você errou, o número da sorte é menor que {}".format(numero))
  elif(numero < sorteio):
    print("você errou, o número da sorte é maior que {}".format(numero))

