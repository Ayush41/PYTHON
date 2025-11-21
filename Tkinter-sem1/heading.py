import tkinter as tk


root = tk.Tk()
root.title("Label Example")

label = tk.Label(root, text="Hello, Tkinter!", font=("Arial", 16))
label.pack()

root.geometry("300x200")


root.mainloop()
