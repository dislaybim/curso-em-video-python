x=float(input("largura da parede: "))
y=float(input("altura da parede: "))
area = x*y
#cada 2 m² de parede precisar de 1 litro de tinta
litros=area/2
print("sua parede tem área de {} m²".format(round(area, 3)))#a função round serve para aproximar vlores
print("vamos precisar de {} litros".format(round(litros,3)))