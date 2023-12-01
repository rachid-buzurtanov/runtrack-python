def creation_liste_fruits():
    fruits = ["pomme", "cerise", "orange", "Melon"]
    fruits.pop(2)
    fruits.insert(2, "Mangue")
    return fruits

liste_de_fruits = creation_liste_fruits()
print(liste_de_fruits)
