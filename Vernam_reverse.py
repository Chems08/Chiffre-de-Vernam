import random

k = input("Alphabet chiffré : ")


print("L'alphabet chiffré est :", k)

# mot en chiffré

mot = input("mot chiffré : ") 

#clé de chiffrement

t = input("Key : ")
a = t.split('-')

print("Key :", t)



results = [int(i) for i in a]       # type passant de str à int

i = k * max(results)        #rescale l'alphabet 


# Changement de la valeur des lettres de l'alphabet pour le mot chiffré

r = []

for l in mot:
    t = 0
    while t < len(mot):
        r.append(i[int(i.index(mot[t])) - int(a[t])])
        t = t+1
    break

print(r)



print("Le mot chiffré est :","'", ''.join(r),"'")
