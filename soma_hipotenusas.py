def é_hipotenusa(n):
   i = 1
   n2 = n*n
   éHipo = False
   while i <= n2:
      j = 1
      while j <= n2:
         soma2 = i*i + j*j
         if soma2 == n2:
            éHipo = True
         j += 1
      
      i += 1
   return éHipo

def soma_hipotenusas(numero):
   n = 1
   somaH = 0
   while n <= numero:
      if é_hipotenusa(n):
         somaH = somaH + n
      n += 1
   return somaH
