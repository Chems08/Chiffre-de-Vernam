
# L'algorithme doit respecter les conditions suivantes : 

#   - le mot choisit ne doit pas excéder 5 lettres
#   - le nombre pour la clé d'une lettre ne doit pas excéder 52


# Testé avec le mot 'hello' et la clé de chiffrement : [1 10 2 15 3]
# --> Résultat attendu : 'ionar'

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

# Pb de l'algorithme :

#   - impossibilité de choisir la taille du mot et de la clé par conséquent (5 lettres requises)
#   - impossibilité d'excéder un certain nombre pour la clé d'une lettre (max 52)  

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

# 3 fois l'alphabet

i = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t","u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t","u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t","u", "v", "w", "x", "y", "z","a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t","u", "v", "w", "x", "y", "z"]

# mot en clair

mot = input("Ecrire un mot en 5 lettres : ") 
print("Le mot choisit est :","'", mot,"'")
mot = list(mot)

# mot = ["h","e","l","l","o"]

# la clés doit être égale au nombre de lettres dans le mot (5)
a = []
a1 = input("Donner la clé de chiffrement pour la lettre 1 : ")
a.append(a1)
a2 = input("Donner la clé de chiffrement pour la lettre 2 : ")
a.append(a2)
a3 = input("Donner la clé de chiffrement pour la lettre 3 : ")
a.append(a3)
a4 = input("Donner la clé de chiffrement pour la lettre 4 : ")
a.append(a4)
a5 = input("Donner la clé de chiffrement pour la lettre 5 : ")
a.append(a5)
print('La clé de chiffrement est : ', a)

#a = [1, 10, 2, 15, 3]

# Option dictionnaire (à étudier)

#m = {"h":1, "e":10, "l":2, "l":15, "o":3}

w = []

# Changement de la valeur des lettres de l'alphabet pour le mot

r1 = int(i.index(mot[0])) + int(a[0])
r2= int(i.index(mot[1])) + int(a[1])
r3= int(i.index(mot[2])) + int(a[2])
r4 = int(i.index(mot[3])) + int(a[3])
r5 = int(i.index(mot[4])) + int(a[4])

w.append(i[r1])
w.append(i[r2])
w.append(i[r3])
w.append(i[r4])
w.append(i[r5])


print("Le mot chiffré est :","'", ''.join(w),"'")


