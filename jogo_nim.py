def computador_escolhe_jogada(n,m):
   multiploMmais1 = n % (m+1)
   if multiploMmais1 <= m:
      return multiploMmais1
   else:
      if n >= m:
         return m
      else:
         return n

def usuario_escolhe_jogada(n,m):
   jogadaValida = False
   while not jogadaValida:
      print()
      jogadaUsuario = int(input("Quantas peças você vai tirar? "))
      if jogadaUsuario > 0 and jogadaUsuario <= m and jogadaUsuario <= n:
         jogadaValida = True
      else:
         print()
         print("Oops! Jogada inválida! Tente de novo.")
         jogadaValida = False
   return jogadaUsuario

def imprimeSituacaoPartida(n):
   if n == 1:
      print("Agora resta apenas uma peça no tabuleiro.")
   else:
      print("Agora restam", n, "peças no tabuleiro.")

def partida():
   print()
   n = int(input("Quantas peças? "))
   m = int(input("Limite de peças por jogada? "))
   jogada = 1
   if not n % (m+1): # Se for múltiplo de (m+1)
      print()
      print("Você começa!")
      vezDOcomputador = False
   else:
      print()
      print("Computador começa!")
      vezDOcomputador = True
            
   while n > 0:
      if jogada != 1:
         imprimeSituacaoPartida(n)
      if vezDOcomputador:
         jogadaComputador = computador_escolhe_jogada(n,m)
         n = n - jogadaComputador
         print()
         if jogadaComputador == 1:
            print("O computador tirou uma peça.")
         else:
            print("O computador tirou", jogadaComputador, "peças.")
         vezDOcomputador = False
      else:
         jogadaUsuario = usuario_escolhe_jogada(n,m)
         n = n - jogadaUsuario
         print()
         if jogadaUsuario == 1:
            print("Você tirou uma peça.")
         else:
            print("Você tirou", jogadaUsuario, "peças.")
         vezDOcomputador = True
      jogada = jogada + 1
   print("Fim do jogo! O computador ganhou!")

def campeonato():
   print()
   print("1 - para jogar uma partida isolada")
   escolha = int(input("2 - para jogar um campeonato "))
   if escolha == 1:
      print()
      print("Você escolheu uma partida isolada!")
      
      partida()
   else:
      print()
      print("Você escolheu um campeonato!")
      rodada = 1
      while rodada <= 3:
         print()
         print("**** Rodada", rodada, "****")
         partida()
         rodada += 1
      print()
      print("**** Final do campeonato! ****")
      print()
      print("Placar: Você 0 x 3 Computador")

print()
print("Bem-vindo ao jogo do NIM! Escolha:")   
campeonato()
