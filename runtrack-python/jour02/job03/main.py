# La boucle for itère à travers une séquence de nombres de 0 à 100
for i in range(101):
    # Exclut les nombres 26, 37 et 88
    if i not in [26, 37, 88]:
        # Affiche la valeur actuelle de la variable i dans le terminal
        print(i)