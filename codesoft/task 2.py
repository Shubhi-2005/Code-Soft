#Calculator
from tkinter import *
def press(num):
    entry_var.set(entry_var.get() + str(num))

def equal():
    try:
        result = str(eval(entry_var.get()))
        entry_var.set(result)
    except:
        entry_var.set("Error")

def clear():
    entry_var.set("")

root = Tk()
root.title("Calculator")
root.geometry("500x400")
root.resizable(False,False)

entry_var = StringVar()
entry = Entry(root, textvariable=entry_var, font=('Arial', 20), bd=10, relief=RIDGE, justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=10)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
    ('=', 5, 0, 4)
]
for btn in buttons:
    text = btn[0]
    row = btn[1]
    col = btn[2]
    colspan = btn[3] if len(btn) == 4  else 1

    if text == '=':
        Button(root, text=text, height=2, width=32, font=('Arial', 12), command=equal)\
           .grid(row=row, column=col, columnspan=colspan, padx=5, pady=5)
    elif text == 'C':
        Button(root, text=text, height=2, width=7, font=('Arial', 12), command=clear)\
            .grid(row=row, column=col, columnspan=colspan, padx=5, pady=5) 
    else:
        Button(root, text=text, height=2, width=7, font=('Arial', 12), command=lambda t=text: press(t))\
            .grid(row=row, column=col, padx=5, pady=5)
        
root.mainloop()
