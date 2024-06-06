
import tkinter as tk
from tkinter import ttk



root = tk.Tk()
root.title("dnd ripoff")
root.geometry("400x300")
''
p1 = "user"
p2 = "computer"
print("you must be 18 to play")
num = int(input("Age?:"))
print("Age:",num)
if num > 18:
    print("Acceptable") 
else:
    print("Access denided: Reason not over 18")
    