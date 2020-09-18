n = int(input("Digite o valor de n: "))
i = 1
fatorial = 1

if n != 0: 
   while i <= n:
      fatorial = fatorial*i
      i = i + 1
else:
   fatorial = 1

print(fatorial)
