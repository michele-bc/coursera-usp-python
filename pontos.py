import math

num1 = int(input("Digite a coordenada x do ponto A: "))
num2 = int(input("Digite a coordenada y do ponto A: "))
num3 = int(input("Digite a coordenada x do ponto B: "))
num4 = int(input("Digite a coordenada y do ponto B: "))

diferencax = num1-num3
diferencay = num2-num4

distancia = math.sqrt(diferencax*diferencax + diferencay*diferencay)

if distancia >= 10:
   print("longe")
else:
   print("perto")
