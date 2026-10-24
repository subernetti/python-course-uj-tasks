import tkinter as tk
import random

def throw_a_dice():
    result_index = random.randint(0, 5)
    label.config(image=possible_throws[result_index])
    label.image = possible_throws[result_index]


root = tk.Tk()
root.geometry("300x300")

possible_throws = [
    tk.PhotoImage(file="dice1.png"),
    tk.PhotoImage(file="dice2.png"),
    tk.PhotoImage(file="dice3.png"),
    tk.PhotoImage(file="dice4.png"),
    tk.PhotoImage(file="dice5.png"),
    tk.PhotoImage(file="dice6.png")
]

label = tk.Label(root, image=possible_throws[0])
label.pack(pady=20)

dice_button = tk.Button(root , text="THROW A DICE", command=throw_a_dice)
dice_button.pack()



root.mainloop()


