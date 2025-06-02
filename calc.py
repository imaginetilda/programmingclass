from tkinter import *

def quit_app():
    root.destroy()

def calculate_sum():
    try:
        num1 = float(box1.get())
        num2 = float(box2.get())
        total_sum = num1 + num2
        sum_label.config(text=str(total_sum))
    except ValueError:
        sum_label.config(text="invalid")

def clear_entries():
    box1.delete(0, END)
    box2.delete(0, END)
    sum_label.config(text="")

root = Tk()
root.title("calc (short for calculator)")
root.resizable(0,0)

box1 = Entry(root, justify = CENTER)
box1.pack(fill = X, ipady = 10, pady=(10,0))

plus_label = Label(root, text="+")
plus_label.pack()

box2 = Entry(root, justify = CENTER)
box2.pack(fill = X, ipady = 10, pady=(0,10))

sum_label = Label(root, text="")
sum_label.pack(ipady=10)

button_print = Button(root, text = "Print", width = 10, command = calculate_sum)
button_print.pack(side = LEFT, ipadx = 10, pady = 10)

button_reset = Button(root, text = "Reset", width = 10, command = clear_entries)
button_reset.pack(side = LEFT, ipadx = 10, pady = 10)

button_quit = Button(root, text = "Quit", width = 10, command = quit_app)
button_quit.pack(side = LEFT, ipadx = 10, pady = 10)

root.mainloop()