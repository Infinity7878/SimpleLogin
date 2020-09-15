import tkinter as tk
from tkinter import messagebox

app = tk.Tk()
app.geometry("300x50")

box1 = tk.Entry(app)
box1.grid(row=1, column=1)
box2 = tk.Entry(app)
box2.grid(row=2, column=1)

def signup():
    user = box1.get()
    passw = box2.get()
    file1 = open("users.txt", "a")
    info = user + passw
    file1.write("\n" + info)

def login():
    user = box1.get()
    passw = box2.get()
    file1 = open("users.txt", "r")
    info = user + passw
    if info in file1:
        tk.messagebox.showinfo("Success", "Success")
    else:
        tk.messagebox.showinfo("Error", "Incorrect Username or Password")

tk.Label(app, text="Username:").grid(row=1, column=0)
tk.Label(app, text="Password:").grid(row=2, column=0)

button1 = tk.Button(app, command=login, text="Login")
button1.place(x=200, y=10)
button2 = tk.Button(app, command=signup, text="SignUp")
button2.place(x=245, y=10)

app.mainloop()