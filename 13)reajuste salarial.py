#Reajuste salarial

salario=float(input("qual o salário(R$): "))
percentual=int(input("porcentagem(%): "))
x=int(input("aumentar(0) ou diminuir(1):"))
if x==0:
  final = salario + (salario*(percentual/100))
  print("ganhava: R${}, aumento de {}%, receberá: R${}.".format(round(salario,2),percentual,round(final,2)))
else:
  final = salario - (salario*(percentual/100))
  print("ganhava: R${}, o desconto de {}%, receberá: R${}.".format(round(salario,2),percentual,round(final,2)))

