import tkinter as tk

root = tk.Tk()
root.title("Changed Label")
root.geometry("300x200")
def changeText():
    label.config(text="Original Text")

label = tk.Label(root, text="Original Text)",font=("Arial",16))
label.pack(pady=20)

button = tk.Button(root, text="CHange Text", command=changeText)
button.pack(pady=10)


root.mainloop()