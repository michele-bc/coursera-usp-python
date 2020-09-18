def fizzbuzz(numero):
   if not numero % 15:
      return "FizzBuzz"
   elif not numero % 5:
      return "Buzz"
   elif not numero % 3:
      return "Fizz"
   else: 
      return numero
      
def test_answer3():
   assert fizzbuzz(3) == 'Fizz'
def test_answer5():
   assert fizzbuzz(5) == 'Buzz'
def test_answer15():
   assert fizzbuzz(15) == 'FizzBuzz'
def test_answer4():
   assert fizzbuzz(4) == 4
