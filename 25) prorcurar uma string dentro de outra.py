#procurando string dentro de outra
nome=str(input("digite seu nome completo: ")).strip()
print("AGUARDE")
print("seu nome tem silva? ")
#print("{}".format(nome[:5]=="silva"))
print("{}".format("silva" in nome.lower()))

