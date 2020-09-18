maisNumeros = True
crescente = True
numero_ant = int(input("Digite um número: "))
while maisNumeros:
    respostaSouN = input("Digite s para mais números: ")
    if respostaSouN == 's':
      numero = int(input("Digite um número: "))
      if numero > numero_ant:
        crescente = crescente and True
      else:
        crescente = crescente and False
    else:
      maisNumeros = False
if crescente:
   print("Está em ordem crescente.")
else:
   print("Não está em ordem crescente.") 
