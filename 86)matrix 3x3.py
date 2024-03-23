
matrix=[]
louco=[]
cont=0
for c in range(0,3):
  for l in range(0,3):
    matrix[c][l]=int(input("digita uma coisa ai: "))
  cont=cont+matrix[c][l]

print(cont)