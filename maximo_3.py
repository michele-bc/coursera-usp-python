def maximo2(x,y):
   if x > y:
      return x
   else:
      return y
      
def maximo(x,y,z):
   return maximo2( maximo2(x,y), z )
