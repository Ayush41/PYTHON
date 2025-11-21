import tkinter as tk

root = tk.Tk()
root.title("Button Function Example")
root.geometry("300x300")

def on_Btn_Pressed():
    print("Button Pressed!") #Output will be shown in terminal/console

lable = tk.Label(root,text="Click Me")
lable.pack()

button = tk.Button(root, text="Press Me", command=on_Btn_Pressed)
button.pack()


root.mainloop()