from tkinter import *
import random

def roll_dice():
    global roll_count

    dice1_value = random.randint(1, 6)
    dice2_value = random.randint(1, 6)

    dice1_display_label.config(text=str(dice1_value))
    dice2_display_label.config(text=str(dice2_value))

    roll_count += 1
    roll_count_display_label.config(text=f"roll count = {roll_count}")

    if dice1_value == 6 and dice2_value == 6:
        dice1_display_label.config(bg="green")
        dice2_display_label.config(bg="green")
    else:
        dice1_display_label.config(bg="red")
        dice2_display_label.config(bg="red")

def quit_app():
    root.destroy()

root = Tk()
root.title("Dice Roll")
style = ('Comic Sans MS', 20, 'bold')

roll_count = 0

quit_button = Button(root, text="Quit", command=quit_app, font=style)
quit_button.grid(row=0, column=0, padx=5, pady=10)

random_button = Button(root, text="Random", command=roll_dice, font=style)
random_button.grid(row=0, column=1, padx=5, pady=10)


dice1_display_label = Label(root, text="", bg="red", width=5, height=2, relief="sunken", font=style)
dice1_display_label.grid(row=1, column=0, padx=5, pady=15)
dice2_display_label = Label(root, text="", bg="red", width=5, height=2, relief="sunken", font=style)
dice2_display_label.grid(row=1, column=1, padx=5, pady=15) 

roll_count_display_label = Label(root, text=f"roll count = {roll_count}", font=style)
roll_count_display_label.grid(row=2, column=0, columnspan=2, pady=15) 
root.mainloop()