import random

hmt = int(input("Enter amout of times u want to play , please keep in minde the max is 10: "))
if hmt > 10:
    hmt = 10

for i in range (hmt):
    random.choice = ("Орел", "Решка")
    user_choise = input("Enter your choise 1 for Орел and 2 for Решка: ")
    if user_choise == random.choice:
        print("You win!")
    elif user_choise != random.choice:
        print("You lose!")
    else:
        print("Invalid choise, try again!")