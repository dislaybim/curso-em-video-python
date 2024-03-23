#criar um dicionario para armazenar os valores o nome do aluno e notas

dicionario = dict()#criar um dicionario vazio
dicionario["aluno"]=str(input("nome do aluno: "))#adicionar elemento no dicionario
dicionario["nota"]=float(input("valor da nmedia: "))#adicionar outro elemento no dicionário
if dicionario['nota'] >= 7:
  dicionario["situação"]="aprovado"
else:
  dicionario["situação"]="reprovado"
#condicionais no proporcionando outro valor no dicionario
print(dicionario)

print("\n")
for k, v in dicionario.items():
  print(f"{k} é igual a {v}")
  #print formatado 