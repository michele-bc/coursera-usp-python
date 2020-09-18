def fizzbuzz(numero):
   if not numero % 15:
      return "FizzBuzz"
   elif not numero % 5:
      return "Buzz"
   elif not numero % 3:
      return "Fizz"
   else: 
      return numero
