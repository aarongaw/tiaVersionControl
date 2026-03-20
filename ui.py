import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.title("TIA Portal Version Control")
root.geometry("400x300")
root.wm_iconbitmap(bitmap=None)
root.grid_rowconfigure(10, weight=1)

# add listbox for project view
lb1 = tk.Listbox(root)
lb1.insert(0, "P04643 Nox 15 Pressfit")
lb1.insert(2, "P04643 Nox 15 Pressfit")
lb1.insert(3, "P04643 Nox 15 Pressfit")
lb1.insert(4, "P04643 Nox 15 Pressfit")
lb1.insert(5, "P04643 Nox 15 Pressfit")
lb1.grid_rowconfigure(2, weight=1)
lb1.grid_configure()
lb1.grid()

root.mainloop()
