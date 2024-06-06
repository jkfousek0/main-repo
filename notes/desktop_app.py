import tkinter as tk
from tkinter import ttk

class MultiPageApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Multi-Page Application")
        self.geometry("400x300")

        # Container to hold all pages
        container = tk.Frame(self)
        container.pack(fill="both", expand=True)

        # Dictionary to keep track of pages
        self.frames = {}

        for F in (StartPage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text=":Welcome to the launch menu!")
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Go to DnD ripoff",
                            command=lambda: controller.show_frame("PageOne"))
        button1.pack()

        button2 = tk.Button(self, text="Go to Page Two",
                            command=lambda: controller.show_frame("PageTwo"))
        button2.pack()
#==========================================================================
class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="This is Page One")
        label.pack(pady=10, padx=10)
    p1 = "user"
    p2 = "computer"
    print("you must be 18 to play")
    num = int(input("Age?:"))
    print("Age:",num)
    if num > 18:
        print("Acceptable") 
    else:
        print('Access denided: Reason not over 18')
        button = tk.Button(self, text="Go to the Start Page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="This is Page Two")
        label.pack(pady=10, padx=10)

        button = tk.Button(self, text="Go to the Start Page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

if __name__ == "__main__":
    app = MultiPageApp()
    app.mainloop()

