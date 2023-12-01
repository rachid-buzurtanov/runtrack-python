def my_sort(lst):
    coups = 0 
    
    for i in range(len(lst)):
        min_index = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
        
        lst[i], lst[min_index] = lst[min_index], lst[i]
        coups += 1  
    
    print(f"Nombre total de coups nécessaires : {coups}")
    
    return lst 

ma_liste = [4, 2, 7, 1, 9, 5]
resultat = my_sort(ma_liste)
print("Liste triée :", resultat)