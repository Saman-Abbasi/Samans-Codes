op = input("Choose an operator: ")

try:
    num1 = float(input("Choose your first number: "))
    num2 = float(input("Choose your second number: "))

    if op == "+":
        print(num1 + num2)

    elif op == "-":
        print(num2 - num1)

    elif op == "*":
        print(num1 * num2)

    elif op == "/":

        try:
            print(num2 / num1)
        except ZeroDivisionError:
            print("Division by zero, cannot divide")
        # Making sure we don't divide a number by zero

    else:
        print("Invalid operator selected")

except ValueError:
    print("Invalid Input")
