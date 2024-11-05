def trier_liste(liste):
    taille = 0
    for element in liste:
        taille += 1 
    for i in range(taille):
        index_min = i
        for j in range(i + 1, taille):
            if liste[j] < liste[index_min]:
                index_min = j
       
        if index_min != i: 
            temp = liste[i]
            liste[i] = liste[index_min]
            liste[index_min] = temp
L = [7, 11, 42, 39, 2]
print("Liste avant tri :", L)
trier_liste(L)
print("Liste après tri :", L)