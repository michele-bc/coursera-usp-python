n = int(input("Digite o numero n: "))

i = 2
parou = False
resposta = "Não"

while not parou:
    
    if (not n % i) and (not n % (i+1)) and (not n % (i+2)):
      parou = True
      resposta = "Sim"
    else:
      if i == 20:
        parou = True
      i = i + 1

print("O número é triangular? " + resposta)
