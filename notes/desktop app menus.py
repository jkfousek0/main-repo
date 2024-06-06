import tkinter as tk
from tkinter import ttk
root = tk.Tk()
root.title("menus")

menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

root.mainloop