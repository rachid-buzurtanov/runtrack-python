# Définition de la chaîne en multipliant "abcdefghijklmnopqrstuvwxyz" par 10
chaine = "abcdefghijklmnopqrstuvwxyz" * 10

# Définition de la variable n avec la valeur 40
n = 40

# Boucle for qui itère sur les valeurs de i de 1 à 29 avec un pas de 2
for i in range(1, 30, 2):
    # Création d'un motif en extrayant les premiers i caractères de la chaîne
    motif = chaine[:i]

    # Affichage du motif actuel
    print(motif)
