x=str(input("nome: ")).strip()#função de entrada para escrever o nome em formato string e armazenar em uma variável
y=x.split()#tranforma cada parte da string em subgrupos que se tornar´uma nova posição de uma nova lista
e=list(x)#transforma cada caractere da string em um subgrupo, sando assim, cada caractere uma posição da noma lista
print("{}".format(y))#
print(e)
cont=len(y)#ler a quantidade de posições salvas na listas "y", para podermos saber a ultima posição que corresponde o ultimo sobrenome
print("\n")
print("seu primeiro nome é: {}".format(y[0]))
print("seu ultimo nome é: {}".format(y[cont-1]))

  