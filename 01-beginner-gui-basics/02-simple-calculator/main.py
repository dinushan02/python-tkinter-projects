"""
Project: Simple Calculator
Level: 01 - Beginner (GUI Basics)
Concepts covered: grid() layout, Entry widget, lambda in loops, basic arithmetic via eval()
"""

import tkinter as tk


def button_click(value):
    """Appends the clicked value (digit/operator) to the display."""
    display.insert(tk.END, value)


def clear_display():
    """Clears the entire display."""
    display.delete(0, tk.END)


def calculate():
    """Evaluates the expression currently shown on the display."""
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(tk.END, str(result))
    except Exception:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")


# 1. Main window setup
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")
root.resizable(False, False)

# 2. Display (Entry widget)
display = tk.Entry(root, font=("Arial", 20), justify="right", bd=10)
display.grid(row=0, column=0, columnspan=4, sticky="nsew")

# 3. Button layout: (label, row, column)
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

# 4. Create and place buttons
for (text, row, col) in buttons:
    if text == '=':
        cmd = calculate
    elif text == 'C':
        cmd = clear_display
    else:
        cmd = lambda t=text: button_click(t)   # t=text avoids the closure bug

    btn = tk.Button(root, text=text, font=("Arial", 16), command=cmd)
    btn.grid(row=row, column=col, sticky="nsew")

# 5. Make rows/columns resize evenly
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(5):
    root.grid_rowconfigure(i, weight=1)

# 6. Run the app
root.mainloop()
