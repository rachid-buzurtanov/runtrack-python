def triangle(height):
    if height <= 0:
        raise ValueError("Hauter invalide: Hauter doit être au dessus de 0")
    l_diag = "/"  
    r_diag = "\\" 
    
    empty_side = height - 1
    
    empty_mid = height * 2 - empty_side * 2 - 2

   
    for i in range(height):

        empty_char = " " * empty_side
        empty_char_mid = " " * empty_mid

        if empty_mid == height * 2 - 2:
            empty_char_mid = "_" * empty_mid

        print(f"{empty_char}{l_diag}{empty_char_mid}{r_diag}")

        empty_side -= 1
        empty_mid += 2


triangle_height = input("Choisissez une hauteur pour le triangle: ")
triangle(int(triangle_height))