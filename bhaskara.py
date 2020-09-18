import math

def raizUnica(a,b):
   return -b/(2*a)

def raizPositiva(a,b,delta):
   return ( -b+math.sqrt(delta) )/(2*a)

def raizNegativa(a,b,delta):
   return ( -b-math.sqrt(delta) )/(2*a)

print("Tendo a equacao de segundo grau no formato ax2 + bx + c=0")

a = int(input("Digite o coeficiente a: "))
b = int(input("Digite o coeficiente b: "))
c = int(input("Digite o coeficiente c: "))

delta = b**2 - 4*a*c


if delta == 0:
   print("a raiz desta equação é", raizUnica(a,b))
   
elif delta > 0:
   print("as raízes da equação são", raizNegativa(a,b,delta), "e", raizPositiva(a,b,delta))
   
else:
   print("esta equação não possui raízes reais")
