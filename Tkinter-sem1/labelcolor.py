import tkinter as tk

root = tk.Tk()
root.title("Colored Label")

label = tk.Label(root,text="This is colored label",fg="red",bg="yellow",font=("Arial",20))
label.pack(padx=50,pady=40)


root.mainloop()