#procurando string dentro de outra
#como não consegui desenvolver esse programa sozinho, vou elaborar um problema mais chao:
quantidade=int(input("tua empresa tem quantos colaboradores? "))#pergunta basica para limitara quantidade de iterações
nomes=[]#lista vazia

for i in range(0,quantidade):#criei 10 iterações
  nomes.append(str(input("digite o nome do colaborador {}: ".format(i+1))).strip())#adicionar nomes na lista que era vazia
#função append()// serve para adicionar a entrada na lista vazia
#a função strip(serve para desconsiderar espaços)

sobrenome=str(input("digite o sobrenome que deseja verificar: "))#seleciono um sobrenome para comparar com qual lista

for i in range(0,quantidade):#iteração para verificar 
  print("o colaborador {} tem sobrenome {}? {}".format(nomes[i], sobrenome, sobrenome in nomes[i].lower()))#lower serve para considerar caracteres maiúculos
#sera que tem como colocar condicional para considerar caracteres minuculos?
