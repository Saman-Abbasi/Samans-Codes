num = int(input("Enter a number: "))

if (num % 3 == 0) and (num % 5 == 0):
    print("FizzBuzz")

# Had to put FizzBuzz first, because if it isn't first and the first statement is true, it'll run that
# And fail to mention FizzBuzz. Only looking for one output, not FizzBuzz and then underneath Fizz or Buzz

elif num % 3 == 0:
    print("Fizz")

elif num % 5 == 0:
    print("Buzz")

elif (num % 3 != 0) and (num % 5 != 0):
    print("Neither")
