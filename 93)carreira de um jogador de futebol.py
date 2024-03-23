#crie um programa para gerenciar o aproveitamento de um jogador de futebol

jogador=dict()

jogador["nome"]=str(input("nome do jogador: "))
jogador["partidas"]=int(input("quantas partidas ele jogou na carreira? "))
jogador["gols"]=list()
cont=0#variavel contador que acumula a quantidade de gols
for i in range(0,jogador["partidas"]):
  gols=int(input("quantidade de gols na partida {}? ".format(i+1)))
  cont=cont+gols
  jogador["gols"].append(gols)
jogador["total"]=cont
print("-="*40)
print(jogador)
print("-="*40)
for k,v in jogador.items():
  print(f"O campo {k} tem o valor {v}.")
print("-="*40)
print("O jogador {} jogou {} jogos".format(jogador["nome"],jogador["partidas"]))
partida=1
for c,k in enumerate(jogador["gols"]):
  print(f"=> Na partida {partida}, fez {k} gols")
  partida=partida+1
print("Foi um total: de {} gols | {} partidas".format(jogador["total"],jogador["partidas"]))

print("gostei demais do programa, top")
  
  
  