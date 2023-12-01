# Itération sur les nombres de 1 à 100
for i in range(1, 101):
    # Vérifier si le nombre est à la fois un multiple de trois et de cinq
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    # Vérifier si le nombre est un multiple de trois
    elif i % 3 == 0:
        print("Fizz")
    # Vérifier si le nombre est un multiple de cinq
    elif i % 5 == 0:
        print("Buzz")
    # Si le nombre n'est pas un multiple de trois ni de cinq, imprimer le nombre lui-même
    else:
        print(i)