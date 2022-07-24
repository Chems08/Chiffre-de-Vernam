import tkinter as tk
import functools
import operator

global t2, t1, kkey

window = tk.Tk()


window.title("Chiffrement de Vernam GUI")

Label010 = tk.Label(window, text = "").pack()
Label0 = tk.Label(window, text = "Veuillez entrer votre alphabet déchiffré, votre mot chiffré, ainsi que votre clé de chiffrement", font=("Courier", 14)).pack()  
Label01 = tk.Label(window, text = "_"*25).pack()
Label011 = tk.Label(window, text = "").pack()



# mot chiffré

Label021 = tk.Label(window, text = "Phrase chiffré :").pack()
mot = tk.Entry(window, width=10)
t1 = mot
mot.pack(padx = 5, pady = 10)

#Alphabet chiffré

Label025 = tk.Label(window, text = "Alphabet :").pack()
alphabet = tk.Entry(window, width=10)
t2 = alphabet
alphabet.pack(padx = 5, pady = 10)


#clé de chiffrement

Label022 = tk.Label(window, text = "Clé de chiffrement :").pack()
key = tk.Entry(window, width=10)
kkey = key
key.pack(padx = 5, pady = 10)



def Cliked():
    i = str(t2.get())
    r13 = list(t1.get())
    mot = r13
    a = kkey.get().split('-')
    results = [int(i) for i in a]
    

    i = i*max(results)    #rescale l'alphabet 


# Changement de la valeur des lettres de l'alphabet pour le mot chiffré

    r = []

    for l in mot:
        t = 0
        while t < len(mot):
            r.append(i[int(i.index(mot[t])) - int(a[t])])
            t = t+1
        break

    n = ''.join(r)

    Label6 = tk.Label(window, text = "Alphabet : ")
    Label6.pack(padx = 5, pady = 10)

    Label4 = tk.Label(window, text = "Key : ")
    Label4.pack(padx = 5, pady = 10)

    Label3 = tk.Label(window, text = "Mot en claire : ")
    Label3.pack(padx = 5, pady = 10)



    alphabet = "Alphabet : ", t2.get()
    alphabet1 = functools.reduce(operator.add, (alphabet))      # équivalent de "".join(alphabet) pour avoir tuple vers str
    print(alphabet1)

    key1  = "Key : ", kkey.get()
    key2 = functools.reduce(operator.add, (key1))       # équivalent de "".join(key1) pour avoir tuple vers str
    print(key2)

    word  = "Mot en claire : ", n   
    word1 = functools.reduce(operator.add, (word))      # équivalent de "".join(word) pour avoir tuple vers str
    print(word1)
    


    def Clik():
        res3 = functools.reduce(operator.add, (alphabet))
        Label6.config(text= res3)

        res = functools.reduce(operator.add, (word))
        Label3.config(text= res)

        res2 = functools.reduce(operator.add, (key1))  
        Label4.config(text= res2)
        

    


    bt = tk.Button(window, text = "Reveal", command = Clik)
    bt.pack(padx = 5, pady = 10)


bt = tk.Button(window, text = "Enter", command = Cliked)
bt.pack(padx = 5, pady = 10)

Label5 = tk.Label(window, text = "_"*int(1.5)*13).pack()
Label05 = tk.Label(window, text = "").pack()

window.mainloop()

# mot en chiffré

# mot = input(" mot chiffré : ") 


#clé de chiffrement

# t = input("Key : ")
# a = t.split('-')

# print("Key :", t)




# results = [int(i) for i in k]       # type passant de str à int

# i = k * max(results)        #rescale l'alphabet 



# Changement de la valeur des lettres de l'alphabet pour le mot chiffré


# r = []

# for l in mot:
#     t = 0
#     while t < len(mot):
#         r.append(i[int(i.index(mot[t])) - int(kkey[t])])
#         t = t+1
#     break

# print(r)



# print("Le mot chiffré est :","'", ''.join(r),"'")



#________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
#________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________



# import random



# L'alphabet avec caractères

# k = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
# "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
# "0","1","2","3","4","5","6","7","8","9",
# "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", ";", ":", ",", ".", "<", ">", "/", "?", "|", " "]


# i = "".join(random.sample(k, len(k)))
# np = i


# window = tk.Tk()

#z = "L'alphabet de chiffrement est : "


# window.title("Chiffrement de Vernam GUI")

# Label010 = tk.Label(window, text = "").pack()
# Label0 = tk.Label(window, text = "Veuillez entrer votre phrase à chiffrer, ainsi que votre clé de chiffrement", font=("Courier", 14)).pack()      #ceci est l'alphabet: 
# Label01 = tk.Label(window, text = "_"*25).pack()
# Label011 = tk.Label(window, text = "").pack()

# Label0 = tk.Label(window, text = z).pack()      #ceci est l'alphabet: 
# Label01 = tk.Label(window, text = "").pack()
# Label2 = tk.Label(window, text = i).pack()      #l'alphabet
# Label02 = tk.Label(window, text = "").pack()
# Label023 = tk.Label(window, text = "").pack()


# # mot en clair

# Label021 = tk.Label(window, text = "Phrase à chiffrer :").pack()
# mot = tk.Entry(window, width=10)
# t1 = mot
# mot.pack(padx = 5, pady = 10)


# #clé de chiffrement

# Label022 = tk.Label(window, text = "Clé de chiffrement :").pack()
# key = tk.Entry(window, width=10)
# kkey = key
# key.pack(padx = 5, pady = 10)

# def Cliked():
#     i = np
#     r13 = list(t1.get())
#     mot = r13
#     a = kkey.get().split('-')
#     results = [int(i) for i in a]
    

#     i = i * max(results)    #rescale l'alphabet 

# Changement de la valeur des lettres de l'alphabet pour le mot chiffré

    # r = []
    # k = list(mot)

    # for l in k:
    #     t = 0
    #     while t < len(k):
    #         r.append(i[int(i.index(k[t])) + int(a[t])])
    #         t = t+1
    #     break

    # n = ''.join(r)



    # alphabet = "Alphabet : ", np
    # alphabet1 = functools.reduce(operator.add, (alphabet))
    # print(alphabet1)

    # key1  = "Key : ", kkey.get()
    # key2 = functools.reduce(operator.add, (key1))
    # print(key2)

    # word  = "Mot chiffré : ", n
    # word1 = functools.reduce(operator.add, (word))
    # print(word1)
    


    # def Clik():
    #     res3 = functools.reduce(operator.add, (alphabet))
    #     Label6.config(text= res3)

    #     res = functools.reduce(operator.add, (word))
    #     Label3.config(text= res)

    #     res2 = functools.reduce(operator.add, (key1))  
    #     Label4.config(text= res2)
        

    # Label6 = tk.Label(window, text = "Alphabet : ")
    # Label6.pack(padx = 5, pady = 10)

    # Label4 = tk.Label(window, text = "Key : ")
    # Label4.pack(padx = 5, pady = 10)

    # Label3 = tk.Label(window, text = "Mot chiffré : ")
    # Label3.pack(padx = 5, pady = 10)



    # bt = tk.Button(window, text = "Reveal", command = Clik)
    # bt.pack(padx = 5, pady = 10)


# bt = tk.Button(window, text = "Enter", command = Cliked)
# bt.pack(padx = 5, pady = 10)

# Label5 = tk.Label(window, text = "_"*int(1.5)*len(i)).pack()
# Label05 = tk.Label(window, text = "").pack()