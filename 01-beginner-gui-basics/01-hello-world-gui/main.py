"""
Project: Hello World GUI
Level: 01 - Beginner (GUI Basics)
Concepts covered: Tkinter window, Label, Button, event handling with command
"""

import tkinter as tk


def say_hello():
    """Runs when the button is clicked. Updates the label text."""
    label.config(text="Button was clicked! 🎉")


# 1. Create the main window
root = tk.Tk()
root.title("Hello World GUI")
root.geometry("300x200")
root.resizable(False, False)   # prevents resizing, optional

# 2. Create widgets
label = tk.Label(root, text="Hello, World!", font=("Arial", 16))
button = tk.Button(root, text="Click Me", font=("Arial", 12), command=say_hello)

# 3. Place widgets on the window
label.pack(pady=30)
button.pack()

# 4. Start the event loop (keeps the window open)
root.mainloop()
