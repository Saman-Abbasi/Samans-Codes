import random  # importing the random module
# Program to generate a random number between a and b inclusive
# In the form            random.randint(a,b)

tries = 0
randNum = random.randint(0, 100)

# print(randNum)

print("Welcome to The Random Number Guessing Game!")
print("You get three attempts at guessing the random number between 1-100.\n")

while True:
    try:
        guess = int(input("What is your guess?: "))
        tries += 1

        if guess == randNum:
            print("Correct guess, you win!")
            break

        elif (guess != randNum) and (tries == 3):
            print("You ran out of guesses, you lose!")
            break

    except ValueError:
        print("Invalid input")





