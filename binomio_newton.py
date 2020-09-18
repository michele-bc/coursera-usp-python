def fatorial(k):

    k_fat = 1
    while k>1:
        k_fat = k_fat*k
        k = k-1
    return k_fat

def combinacao(m, n):
    resultado = fatorial(m)/( fatorial(n)*fatorial(m-n) )
    return resultado

def binomio_newton(x,y,n):
    i = 0
    binew = 0
    while i <= n:
        binew += combinacao(n,i)*( x**(n-i) )*( y**i )
    return binew

   
