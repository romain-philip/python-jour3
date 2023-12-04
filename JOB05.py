def calcule(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Erreur : Division par zéro"
    elif operator == '%':
        if num2 != 0:
            return num1 % num2
        else:
            return "Erreur : Division par zéro"
    else:
        return "Opérateur non reconnu"
resultat_addition = calcule(6, '+', 2)
resultat_soustraction = calcule(9, '-', 5)
resultat_multiplication = calcule(25, '*', 2)
resultat_division = calcule(36, '/', 5)

print("Somme:", resultat_addition)
print("Différence:", resultat_soustraction)
print("Produit:", resultat_multiplication)
print("Quotient:", resultat_division)