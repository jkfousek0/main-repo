import tkinter as tk
from tkinter import messagebox


def show_message():
    messagebox.showinfo("Message", "hello, world!")


#generate main application window
root = tk.Tk()
root.title("DnD rip off")

#lable and button
greeting_label = tk.Label(root, text="Welcome to My Desktop App!")
greeting_label.pack(pady=10)

greet_button = tk.Button(root, text="Click me", command=show_message)
greet_button.pack(pady=10)

# Start the application
root.mainloop()
