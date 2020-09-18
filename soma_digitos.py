numero = input("Digite um número inteiro: ")
qntsDigitos = len(numero)
numero = int(numero)
i = 0
soma = 0

while i < qntsDigitos:
   encurtado = numero // (10**i)
   digito = encurtado % 10
   soma = soma + digito
   i = i + 1

print(soma)
