#calculando descontos, gustavo guanabara
x=float(input("preço do produto(R$): "))
y=int(input("valor do desconto(%): "))
desconto = x - (x*(y/100))
print("o produto que custava {}R$, na promoção de {}% custará{}R$.".format(round(x,2), y, round(desconto,2)))
