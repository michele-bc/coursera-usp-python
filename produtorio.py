produto = 1
numero = int(input("Digite o numero a ser multiplicado: "))

while numero != 0:
    produto = produto*numero
    numero = int(input("Digite o numero a ser multiplicado: "))
    
print("O produto dos números é:", produto)
