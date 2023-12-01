L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]

somme_des_paires = 0

for NB in L:
    if NB % 2 == 0:
        somme_des_paires += NB

print("somme_des_valeurs_paires:", somme_des_paires)