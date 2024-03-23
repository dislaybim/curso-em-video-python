#conversor de temperaturas

x=int(input("qual escala?(°C=1,°F=2,K=3): "))

if x==1:
  celsiu=float(input("temperatura(°C): "))
  y=int(input("para qual deseja converter?(°F=2,K=3): "))
  if y==2: 
    farenheit= 1.8*celsiu + 32
    print("{}°C equivale {}°F".format(round(celsiu,2),round(farenheit,2)))
  else:
    kelvin = celsiu + 273.15
    print("{}°C equivale {}K".format(round(celsiu,2),round(kelvin,2)))

elif x==2:
  farenheit=float(input("temperatura(°F): "))
  y=int(input("para qual deseja converter?(°C=2,K=3): "))
  if y==2: 
    celsiu= 0.555*farenheit - 17.78
    print("{}°F equivale {}°C".format(round(farenheit,2),round(celsiu,2)))
  else:
    celsiu= 0.555*farenheit - 17.78
    kelvin = celsiu + 273.15
    print("{}°F equivale {}K".format(round(farenheit,2),round(kelvin,2)))
else:
  kelvin=float(input("temperatura(K): "))
  z=int(input("para qual deseja converter?(°C=1,°F=2): "))
  if z==1: 
    celsiu=kelvin-273,15
    print("{}K equivale {}°C".format(round(kelvin,2),round(celsiu,2)))
  else:
    celsiu=kelvin-273,15
    farenheit= 1.8*celsiu + 32
    print("{}K equivale {}°F".format(round(kelvin,2),round(farenheit,2)))
  


