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


# Definit deux fonctions pour que les bouttons apparaissent

def selection1():
        print("Chiffrer")
        call(["python3", './Vernam.py'])
#        exit()

def selection2():
        print("Déchiffrer")
        call(["python3", './gui_vernam_reverse.py'])
#        exit()


radio = IntVar()
Label(text="").pack()
Label(text="Que souhaites-tu faire ?", font=('Aerial 20')).pack()
Label(text="").pack()

# Definit des bouttons pour chaque option

r1 = tk.Button(window, text="Chiffrer", command=selection1)
r1.pack(anchor=N)

Label(text="").pack()

r2 = tk.Button(window, text="Déchiffrer", command=selection2)
r2.pack(anchor=N)



label = Label(window)
label.pack()


 
window.mainloop()