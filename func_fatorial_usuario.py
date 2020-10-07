def fun_fatorial(n):
   fatorial = 1
   while n > 1:
      fatorial = fatorial*n
      n = n - 1
   return fatorial

numero = int(input("Digite número a ser calculado o fatorial (número negativo encerra): "))
while numero >= 0:
   print(fun_fatorial(numero))
   numero = int(input("Digite número a ser calculado o fatorial (número negativo encerra): "))
