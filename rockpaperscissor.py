from tkinter import *
from tkinter import messagebox
import random

root = Tk()
root.title("Rock Paper Scissors")
root.configure(bg="light blue")
root.geometry("650x500")

label1 = Label(
    root,
    text="Welcome to Rock Paper Scissors!",
    bg="light blue",
    font=("Arial", 18, "bold")
)
label1.place(relx=0.5, y=40, anchor=CENTER)

label2 = Label(
    root,
    text="Choose your move:",
    bg="light blue",
    font=("Arial", 14)
)
label2.place(relx=0.5, y=100, anchor=CENTER)

computer_choices = ["Rock", "Paper", "Scissors"]

user_score = 0
computer_score = 0

user_label = Label(
    root,
    text="Your Score: 0",
    bg="light blue",
    font=("Arial", 12, "bold")
)
user_label.place(x=100, y=150)

computer_label = Label(
    root,
    text="Computer Score: 0",
    bg="light blue",
    font=("Arial", 12, "bold")
)
computer_label.place(x=350, y=150)

result_label = Label(
    root,
    text="Make your choice to start!",
    bg="light blue",
    font=("Arial", 14, "bold")
)
result_label.place(relx=0.5, y=300, anchor=CENTER)

choice_label = Label(
    root,
    text="",
    bg="light blue",
    font=("Arial", 12)
)
choice_label.place(relx=0.5, y=260, anchor=CENTER)


def play(user_choice):
    global user_score, computer_score

    computer_choice = random.choice(computer_choices)

    choice_label.config(
        text=f"You chose: {user_choice}  |  Computer chose: {computer_choice}"
    )

    if user_choice == computer_choice:
        result = "It's a Tie!"

    elif (
        (user_choice == "Rock" and computer_choice == "Scissors")
        or (user_choice == "Paper" and computer_choice == "Rock")
        or (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "You Win!"
        user_score += 1

    else:
        result = "Computer Wins!"
        computer_score += 1

    result_label.config(text=result)

    user_label.config(text=f"Your Score: {user_score}")
    computer_label.config(text=f"Computer Score: {computer_score}")


def reset():
    global user_score, computer_score

    user_score = 0
    computer_score = 0

    user_label.config(text="Your Score: 0")
    computer_label.config(text="Computer Score: 0")
    result_label.config(text="Make your choice to start!")
    choice_label.config(text="")


button1 = Button(
    root,
    text="🪨 Rock",
    command=lambda: play("Rock"),
    bg="brown",
    fg="black",
    font=("Arial", 12, "bold"),
    width=10
)
button1.place(x=70, y=200)

button2 = Button(
    root,
    text="📄 Paper",
    command=lambda: play("Paper"),
    bg="green",
    fg="black",
    font=("Arial", 12, "bold"),
    width=10
)
button2.place(x=250, y=200)

button3 = Button(
    root,
    text="✂️ Scissors",
    command=lambda: play("Scissors"),
    bg="blue",
    fg="black",
    font=("Arial", 12, "bold"),
    width=10
)
button3.place(x=430, y=200)

button4 = Button(
    root,
    text="Reset Game",
    command=reset,
    bg="red",
    fg="black",
    font=("Arial", 12, "bold")
)
button4.place(relx=0.5, y=380, anchor=CENTER)

root.mainloop()