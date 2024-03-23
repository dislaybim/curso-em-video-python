#classificação de atletas olimpicos
#41)CLASSIFICAÇÃO DOS ATLETAS
import datetime

print("\33[34m-=-\33[m"*8)
print("\33[31mSEJA BEM-VINDO\33[m")
pergunta="sim"
nomes=[]#lista vazia
nascimentos=[]#lista vazia
classifica=["MIRIM","INFANTIL","JUNIOR","SENIOR","MASTER"]#lista de classificação

while pergunta == 'sim':
  atleta=input("digite o nome do atleta: ")
  nomes.append(atleta)#adicionar elemento na lista
  ano=int(input("digite o ano de nascimento: "))
  nascimentos.append(ano)
  idade=datetime.date.today().year - ano
  if(idade<=9 ):
    print("o atleta {} é {} pois tem {} anos".format(atleta,classifica[0],idade))

  elif(idade>9 and idade<=14):
    print("o atleta {} é {} pois tem {} anos".format(atleta,classifica[1],idade))
  elif(idade>14 and idade<=19):
    print("o atleta {} é {} pois tem {} anos".format(atleta,classifica[2],idade))

  elif(idade>19 and idade<=25):
    print("o atleta {} é {} pois tem {} anos".format(atleta,classifica[3],idade))
  elif(idade>25):
    print("o atleta {} é {} pois tem {} anos".format(atleta,classifica[4],idade))
    
  
  x=input("deseja continuar?")
  pergunta=x

print("{} | {} ".format(nomes,nascimentos))
  
  
  