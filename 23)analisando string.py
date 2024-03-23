#separando os digitos de um numero
x=str(input("escreva um numero: "))#a entrada será uma variável string
y=len(x)#essa é uma função que ira ler a quantidade de caracteres
string=["unidade","dezenas", "centenas", "milhar", "dezenha de milhar", "centena de milhar"]#criamouma string com palavras que ficarao em ordem nas iterações
x = list(x)#armazenaremos os valores da função imput em uma string
x.reverse()#invertemos as posições das strings
for i in range(0,y):#criamos um laço de iteração para igualar uma string a outra
  print("{}: {}".format(string[i],x[i]))