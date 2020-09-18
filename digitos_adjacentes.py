numero = input("Digite um número inteiro: ")
qntsDigitos = len(numero)
numero = int(numero)
igual = False
i = 1
encurtado = 1

if qntsDigitos > 1:
   digito_anterior = numero % 10
   while not igual and encurtado != 0:
      encurtado = numero // (10**i)  # Digitos para frente da casa da 10**(i-1)-dade 
      digito = encurtado % 10        # Digito da casa da unidade
      i += 1
      if digito == digito_anterior:
         igual = True
      digito_anterior = digito
   
if igual:
   print("sim")
else:
   print("não")
