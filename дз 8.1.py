import random

random_int = random.randint(1, 10)

for i in range (3):
    guess = int(input("Guess a number between 1 and 10: "))
    if guess != random_int:
        print("Wrong guess, u have ", 2 - i, " tries left")
    else:
        print("Congrats, you guessed it right!")
        break
else:
    print("Sorry, you've used all your tries. The correct number was ", random_int)


    