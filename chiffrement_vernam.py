

import random

# L'alphabet avec caractères

k = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
"0","1","2","3","4","5","6","7","8","9",
"~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", ";", ":", ",", ".", "<", ">", "/", "?", "|"]

i = "".join(random.sample(k, len(k)))
print("L'alphabet de chiffrement est :", i)

# mot en clair

mot = input("Ecrire un mot en 5 lettres : ") 
print("Le mot choisit est :","'", mot,"'")
mot = list(mot)

#clé de chiffrement

t = input("Donner la clé de chiffrement (espacé de '-') :")

a = t.split('-')

print('La clé de chiffrement est : ', t)

#rescale l'alphabet 

results = [int(i) for i in a]

i = i * max(results)

# Changement de la valeur des lettres de l'alphabet pour le mot chiffré


r = []
for l in mot:
    t = 0
    while t < len(mot):
        r.append(i[int(i.index(mot[t])) + int(a[t])])
        t = t+1
    break

print(r)



print("Le mot chiffré est :","'", ''.join(r),"'")


