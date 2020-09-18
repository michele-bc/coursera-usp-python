n = input("Digite o numero n: ")
d = int(input("Digite o numero d: "))
qntsAlgarismos = len(n)
n_int = int(n)
i = qntsAlgarismos - 1
contador = 0
while i >= 0:
    div = n_int // (10 ** i)
    if div == d:
        contador = contador + 1
    n_int = n_int - div*(10**i)
    i = i - 1
print("O dígito", d, "ocorre", contador, "vezes em " + n)
