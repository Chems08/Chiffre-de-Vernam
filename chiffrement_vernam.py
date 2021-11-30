

# Testé avec le mot 'hello' et la clé de chiffrement : [1 10 2 15 3] et l'alphabet dans l'ordre : 
# --> Résultat attendu : 'ionar'

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

import random
# 2 fois l'alphabet avec caractères

k = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9","@","&","!","-","#","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9","@","&","!","-","#"]
i = "".join(random.sample(k, len(k)))
print("L'alphabet de chiffrement est :", i)

# mot en clair

mot = input("Ecrire un mot en 5 lettres : ") 
print("Le mot choisit est :","'", mot,"'")
mot = list(mot)

# mot = ["h","e","l","l","o"]

# la clés doit être égale au nombre de lettres dans le mot (5)

#a = []
#a1 = input("Donner la clé de chiffrement pour la lettre 1 : ")
#a.append(a1)
#a2 = input("Donner la clé de chiffrement pour la lettre 2 : ")
#a.append(a2)
#a3 = input("Donner la clé de chiffrement pour la lettre 3 : ")
#a.append(a3)
#a4 = input("Donner la clé de chiffrement pour la lettre 4 : ")
#a.append(a4)
#a5 = input("Donner la clé de chiffrement pour la lettre 5 : ")
#a.append(a5)

t = input("Donner la clé de chiffrement (espacé de '-') :")

a = t.split('-')

print('La clé de chiffrement est : ', t)


#a = [1, 10, 2, 15, 3]

# Option dictionnaire (à étudier)

#m = {"h":1, "e":10, "l":2, "l":15, "o":3}

#w = []

# Changement de la valeur des lettres de l'alphabet pour le mot

#r1 = int(i.index(mot[0])) + int(a[0])
#r2= int(i.index(mot[1])) + int(a[1])
#r3= int(i.index(mot[2])) + int(a[2])
#r4 = int(i.index(mot[3])) + int(a[3])
#r5 = int(i.index(mot[4])) + int(a[4])

#w.append(i[r1])
#w.append(i[r2])
#w.append(i[r3])
#w.append(i[r4])
#w.append(i[r5])

r = []
for l in mot:
    t = 0
    while t < len(mot):
        r.append(i[int(i.index(mot[t])) + int(a[t])])
        t = t+1
    break

print(r)



print("Le mot chiffré est :","'", ''.join(r),"'")


