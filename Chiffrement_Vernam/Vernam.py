
import random
import tkinter as tk
import functools
import operator


# L'alphabet avec caractères

k = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
"0","1","2","3","4","5","6","7","8","9",
"~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", ";", ":", ",", ".", "<", ">", "/", "?", "|", " "]

global np
i = "".join(random.sample(k, len(k)))
np = i


window = tk.Tk()



window.title("Chiffrement de Vernam GUI")

Label010 = tk.Label(window, text = "").pack()
Label0 = tk.Label(window, text = "Veuillez entrer votre phrase à chiffrer, ainsi que votre clé de chiffrement", font=("Courier", 14)).pack()      #ceci est l'alphabet: 
Label01 = tk.Label(window, text = "_"*25).pack()
Label011 = tk.Label(window, text = "").pack()



# mot en clair

Label021 = tk.Label(window, text = "Phrase à chiffrer :").pack()
mot = tk.Entry(window, width=10)
t1 = mot
mot.pack(padx = 5, pady = 10)


#clé de chiffrement

Label022 = tk.Label(window, text = "Clé de chiffrement :").pack()
key = tk.Entry(window, width=10)
kkey = key
key.pack(padx = 5, pady = 10)

def Cliked():
    i = np
    r13 = list(t1.get())
    mot = r13
    a = kkey.get().split('-')
    results = [int(i) for i in a]
    

    i = i * max(results)    #rescale l'alphabet 

# Changement de la valeur des lettres de l'alphabet pour le mot chiffré

    r = []
    k = list(mot)

    for l in k:
        t = 0
        while t < len(k):
            r.append(i[int(i.index(k[t])) + int(a[t])])
            t = t+1
        break

    n = ''.join(r)



    alphabet = "Alphabet : ", np
    alphabet1 = functools.reduce(operator.add, (alphabet))
    print(alphabet1)

    key1  = "Key : ", kkey.get()
    key2 = functools.reduce(operator.add, (key1))
    print(key2)

    word  = "Mot chiffré : ", n
    word1 = functools.reduce(operator.add, (word))
    print(word1)
    


    def Clik():
        res3 = functools.reduce(operator.add, (alphabet))
        Label6.config(text= res3)

        res = functools.reduce(operator.add, (word))
        Label3.config(text= res)

        res2 = functools.reduce(operator.add, (key1))  
        Label4.config(text= res2)
        

    Label6 = tk.Label(window, text = "Alphabet : ")
    Label6.pack(padx = 5, pady = 10)

    Label4 = tk.Label(window, text = "Key : ")
    Label4.pack(padx = 5, pady = 10)

    Label3 = tk.Label(window, text = "Mot chiffré : ")
    Label3.pack(padx = 5, pady = 10)



    bt = tk.Button(window, text = "Reveal", command = Clik)
    bt.pack(padx = 5, pady = 10)


bt = tk.Button(window, text = "Enter", command = Cliked)
bt.pack(padx = 5, pady = 10)

Label5 = tk.Label(window, text = "_"*int(1.5)*len(i)).pack()
Label05 = tk.Label(window, text = "").pack()




window.mainloop()
