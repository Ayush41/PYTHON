import tkinter as tk

root = tk.Tk()
root.title("Button to Display Label")
root.geometry("400x400")

def greet():
    name = entry.get()
    result_label.config(text=f"Hello, {name}")

entry = tk.Entry(root, font=("Arial",14))
entry.pack(pady=20)

button = tk.Button(root, text="Submit", command=greet)
button.pack(pady=10)

result_label = tk.Label(root,text="")
result_label.pack(pady=20)

root.mainloop()