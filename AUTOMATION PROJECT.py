from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("clock")

def get_time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, get_time)

label = Label(root, font=("ds=digital", 80), background= "white", foreground = "purple")
label.pack(anchor ='center')

get_time()
mainloop()