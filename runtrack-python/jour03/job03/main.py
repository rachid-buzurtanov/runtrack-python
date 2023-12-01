def Add(a, b):
    # Vérifie si les nombres sont des entiers
    if a % 1 != 0 or b % 1 != 0:
        print('Nombre invalide. Veuillez entrer des nombres entiers.')
    else:
        # Ajoute les deux nombres s'ils sont des entiers
        result = a + b
        print(f"La somme de {a} et {b} est : {result}")


# Appels de la fonction avec différents jeux de nombres
Add(1, 1) 
Add(40, 2)  
Add(954, 238) 
Add(25.4, 21.8) 
