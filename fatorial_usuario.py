numero = int(input("Digite número a ser calculado o fatorial (número negativo encerra): "))
while numero >= 0:
   fatorial = 1
   #print(fatorial)
   while numero > 1:
      fatorial = fatorial*numero
      #print(fatorial)
      numero = numero - 1
      #print(numero)
   print(fatorial)
   numero = int(input("Digite número a ser calculado o fatorial (número negativo encerra): "))
