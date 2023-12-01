def calcule(num1, operator, num2):
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Erreur : Division par zéro"
    elif operator == '%':
        if num2 != 0:
            result = num1 % num2
        else:
            return "Erreur : Modulo par zéro"
    else:
        return "Opérateur non reconnu"

    return result

result1 = calcule(34, '+', 10)
result2 = calcule(19, '*', 3)
result3 = calcule(22, '/', 2)

print("Résultat 1:", result1)
print("Résultat 2:", result2)
print("Résultat 3:", result3)