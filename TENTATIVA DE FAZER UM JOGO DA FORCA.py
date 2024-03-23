#fazer um jogor da forca:
#primeiro criar um menu do jogo:
import random
import time


print("\33[34m-=-\33[m"*7)
print("   \33[31mJOGO DA FORCA\33[m")
print("\33[34m-=-\33[m"*7)
print("\n\n0 -INICIAR")
print("\n1 - ADICIONAR PALAVRA")

menu=int(input("\n\n"))

if menu==0:
  print("COMEÇAR:")
  
elif menu==1:
  lista=[]
  lista.append(str(input("adicione o nome de um animal: ")))
  print("\33[34mCARREGANDO\33[m")
  time.sleep(5)
  print("OK!!\n\n")
  print("adicionar outro nome?(0-NÃO OU 1-SIM) ")
  x=int(input(""))
  if x==0:
    print("\33[34m-=-\33[m"*7)
    print("   \33[31mJOGO DA FORCA\33[m")
    print("\33[34m-=-\33[m"*7)
    print("\n\n0 -INICIAR")
    print("\n1 - ADICIONAR PALAVRA")
    menu=int(input("\n\n"))
    

  