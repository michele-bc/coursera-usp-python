lista = []
entrada = 1
while entrada != 0:
   entrada = int(input("Digite um número: "))
   lista.append(entrada)

i = len(lista) - 1
lista_invertida = []
while i > 0:
   i = i - 1
   lista_invertida.append(lista[i])
print()
for numero in lista_invertida:
   print(numero)
print()
