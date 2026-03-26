import tkinter as tk
import random

root = tk.Tk()
root.title("камень ножницы бумага")
root.geometry("300x200")


label = tk.Label(root, text="welcome to камень ножницы бумага")
label.pack()


def play(choice):
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)

    if choice == computer:
        result = "Draw"

    elif (
        (choice == "rock" and computer == "scissors") or
        (choice == "paper" and computer == "rock") or
        (choice == "scissors" and computer == "paper")
    ):
        result = "You win"

    else:
        result = "Computer wins"

    label.config(text=f"You: {choice} | Computer: {computer} | {result}")


btn_rock = tk.Button(root, text="rock",
                     command=lambda: play("rock"))
btn_rock.pack()

btn_paper = tk.Button(root, text="paper",
                      command=lambda: play("paper"))
btn_paper.pack()

btn_scissors = tk.Button(root, text="scissors",
                         command=lambda: play("scissors"))
btn_scissors.pack()


root.mainloop()