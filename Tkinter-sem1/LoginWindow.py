import tkinter as tk

root = tk.Tk()
root.title("Login Window")
root.geometry("300x200")

def login():
    username= entry_user.get()
    password= entry_pswd.get()
    result_label.config(text="Login Successful")


#username
tk.Label(root, text="Username:").pack()
entry_user = tk.Entry(root)
entry_user.pack()

#password
tk.Label(root, text="Password:").pack()
entry_pswd = tk.Entry(root, show="*")
entry_pswd.pack()


#Login Button
tk.Button(root, text="Login", command=login).pack(pady=10)

#Result Label
result_label = tk.Label(root,text="")
result_label.pack()


root.mainloop()