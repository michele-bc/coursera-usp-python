def fatorial(n):
   n_fatorial = 1
   while n > 1:
      n_fatorial = n_fatorial*n
      n = n - 1
   return n_fatorial

n = 6
k = 2

binomio = fatorial(n)/( fatorial(k)*fatorial(n-k) )

print(binomio)
