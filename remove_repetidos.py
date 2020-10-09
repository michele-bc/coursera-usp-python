def remove_repetidos(lista):
   lista.sort()
   nova_lista = []
   for i in range(1,len(lista)):
      print(i, lista[i-1], lista[i])
      if lista[i-1] != lista[i]:
         nova_lista.append(lista[i-1])
   nova_lista.append(lista[-1])
   return nova_lista
