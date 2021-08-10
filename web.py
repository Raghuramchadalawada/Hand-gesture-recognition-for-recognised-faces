import tkinter as tk
import os
from tkinter import ttk
win = tk.Tk()
win.title("Python GUI App")# Label
Lbl = ttk.Label(win, text = "Click for gesture control ")
Lbl.pack()# Click event
def click():
    os.system('python IdentifyingFaces.py')
    action.configure(text = "Clicked")
Lbl.configure(foreground = 'red')
Lbl = ttk.Label(win, text = "Button  Click ")
Lbl.configure(text = 'Button Clicked')# Adding Button
action = ttk.Button(win, text = "Click Me", command = click)
action.pack()
win.mainloop()
