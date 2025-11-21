import tkinter as tk

root = tk.Tk()
root.title("Colored Label")
root.geometry("400x200")

label = tk.Label(root,text="This is colored label",fg="red",bg="yellow",font=("Arial",20))
label.pack(padx=50,pady=40)
root.configure(bg="light blue")

root.mainloop()