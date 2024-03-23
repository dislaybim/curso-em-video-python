#aqui iremos construir um analisador de textos

nome=str(input("digite seu nome completo: "))#escrever o nome armazenando na variável string
print("analisando nome...")#loading
print("seu nome em letras maiúculas é {}".format(nome.upper()))#aqui transformando a saída em letras maiúculas
print("seu nome em letras minúsculas é {}".format(nome.lower()))#função para transformar a saida em letras minuscolas
print("seu nome tem ao todo {} letras".format(len(nome)))#função para contar a quantidade de caracteres