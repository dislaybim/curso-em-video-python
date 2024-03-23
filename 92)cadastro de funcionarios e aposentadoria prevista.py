#crie um programa que leia nome, ano de nascimento e carteira de trabalho a cadastre-os(com idade) em um dicionário se por acaso a ctps for diferente do zero

cadastro=dict()#criar dicionario vazio para armazenar as variáveis
import datetime

pessoas=int(input("quantas pessoas você quer? "))
lista=list()

for i in range(0,pessoas):
  cadastro["colaborador"]=str(input("digite o nome do sujeito: "))
  cadastro["nascimento"]=int(input("ano de nascimento: "))
  cadastro["idade"]=datetime.date.today().year-cadastro["nascimento"]
  cadastro["CTPS"]=int(input("numero da carteira de trabalho(não tem-0): "))
  print("\n")
  if(cadastro["CTPS"]==0):
    for k,v in cadastro.items():
      print(f"{k}: {v}") 
      break
  else:
    cadastro["contrato"]=int(input("Ano de contratação: "))
    inicio=datetime.date.today().year 
    cadastro["salario"]=float(input("diga seu salario: "))
    #35 anos de contribuição
    comeco=datetime.date.today().year-cadastro["contrato"]
    falta=35-comeco
    cadastro["aposenta"]=cadastro["idade"]+falta
    lista.append(cadastro)
    
for k,v in cadastro.items():
  print(f"{k}: {v}")

#print(f"começou a trabalhar com {inicio}")

print(lista)
