from tkinter import *
from tkinter import filedialog
import os
import random
import string
import secrets

class App(Tk):
    def __init__(self):
        super(App, self).__init__()
        self.title("Password Generator")
        self.minsize(485, 280)

        pass_many_label = Label(self, text = 'Generates 10 characters', font=('bold', 14))
        pass_many_label.place(x = 20, y = 20)
        pass_entry = Entry(self, font=('bold', 14), width = 40)
        pass_entry.place(x = 20, y = 50)

        pass_label = Label(self, text = 'Each time adds 10 characters', font=('bold', 14))
        pass_label.place(x = 20, y = 100)
        pass_many_entry = Entry(self, font=('bold', 14), width = 40)
        pass_many_entry.place(x = 20, y = 130)

        def pass_add(): 
            alphabet = string.ascii_letters + string.digits + string.punctuation
            while True:
                password = ''.join(secrets.choice(alphabet) for i in range(10))
                if (any(c.islower() for c in password)
                        and any(c.isupper() for c in password)
                        and sum(c.isdigit() for c in password) >= 3):
                    break

            if len(pass_entry.get()) == 0 or len(pass_entry.get()) != 0:
                pass_entry.delete(0, 'end')
                pass_entry.insert(0, password)
            pass_many_entry.insert(0, password)

        wczytaj_button = Button(self, text = 'Generate', activebackground = 'green', font=('bold', 14), command=pass_add)
        wczytaj_button.place(x = 192, y = 200)

# Start
app = App()
app.iconbitmap('lock.ico')
app.mainloop()