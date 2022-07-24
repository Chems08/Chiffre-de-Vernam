import tkinter as tk
from tkinter import *
import functools
import operator
from subprocess import call

window = tk.Tk()

window.title("Chiffrement de Vernam GUI")

window.geometry("500x250")
frame = Frame(window)
frame.pack()

def click():
    if str(radio.get()) == "1":
        print("Chiffrer")
        call(["python3", './Vernam.py'])
        exit()

    elif str(radio.get()) == "2":
        print("Déchiffrer")
        call(["python3", './gui_vernam_reverse.py'])
        exit()

# Definit une fonction pour que le boutton apparaisse

def selection():
    bt = tk.Button(window, text = "Enter", command = click)
    bt.pack(padx = 5, pady = 10)

radio = IntVar()
Label(text="").pack()
Label(text="Que souhaites-tu faire ?", font=('Aerial 20')).pack()
Label(text="").pack()

# Definit des radiobutton pour chaque option

r1 = Radiobutton(window, text="Chiffrer", variable=radio, value=1, command=selection)
r1.pack(anchor=N)

r2 = Radiobutton(window, text="Déchiffrer", variable=radio, value=2, command=selection)
r2.pack(anchor=N)



label = Label(window)
label.pack()


 
window.mainloop()