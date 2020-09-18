def éPrimo(k):
   i = 2
   primo = True
   while i < k and primo:
      if k % i == 0:
         primo = False
      i += 1
   return primo

def maior_primo(x):
   primo = False
   while x > 1 and not primo:
      primo = éPrimo(x) 
      if primo:
         return x
      else:
         x = x - 1
