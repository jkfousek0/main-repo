import tkinter as tk
from tkinter import ttk
#---------module

root = tk.Tk()
root.title("phriedphoenix's launch menu")
root.geometry("400x300")
#------base

label = tk.Label(root, text="Hello, Tkinter!")
label.pack()
#------widget

def on_button_click():
    print("Button clicked!")
listbox = tk.Listbox(root)
listbox.insert(1, "Item 1")
listbox.insert(2, "Item 2")
listbox.pack()
button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack()

root.mainloop()