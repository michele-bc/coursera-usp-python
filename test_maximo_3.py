def maximo2(x,y):
   if x > y:
      return x
   else:
      return y
      
def maximo(x,y,z):
   return maximo2( maximo2(x,y), z )
      
def test_answer1():
   assert maximo(30, 14, 10) == 30
def test_answer2():
   assert maximo(0, -1, 1) == 1
