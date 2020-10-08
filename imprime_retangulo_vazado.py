largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))

a = 1
while a <= altura:
   l = 1
   while l <= largura:
      if a == 1 or a == altura or l == 1 or l == largura:
         print("#", end='')
      else:
         print(" ", end='')
      l += 1
   print()
   a += 1
