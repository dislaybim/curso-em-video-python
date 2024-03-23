y=int(input("qual a matrix: MXN? "))

matrix = [[0 for j in range(y)] for i in range(y)]
louco = []
cont = 0

for c in range(0, y):
  for l in range(0, y):
    matrix[c][l] = int(input("Digite um valor: "))
    cont += matrix[c][l]

soma=0
toma=0
pega=0
for c in range(0,y):
  for l in range(0,y):
    if matrix[c][l] % 2 == 0:
      soma+=matrix[c][l]
    elif matrix[2][l]:
      toma+=matrix[2][l]
    elif matrix[c][0]:
      pega+=pega[c][0]

print(toma)
print(pega)
print("\n\n")
print("soma dos valores pares: {}".format(soma))
print("Soma dos valores:", cont)
print("Matriz:", matrix)
