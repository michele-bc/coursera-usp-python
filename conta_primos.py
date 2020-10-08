def VerificaPrimo(n):
   i = 2
   primo = True
   while i < n and primo:
      if n % i == 0:
         primo = False
      i += 1
   return primo

def n_primos(numero):
   contadorPrimos = 0
   i = 2
   while numero > 1 and i <= numero:
      if VerificaPrimo(i):
         contadorPrimos += 1
      i += 1
   return contadorPrimos
