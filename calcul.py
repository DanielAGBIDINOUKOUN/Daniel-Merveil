nbr1 = float(input("Entrez le premier nombre : "))
nbr2 = float(input("Entrez le deuxième nombre : "))

while True:

    print("\n===== CALCULATRICE =====")
    print("1 pour l'addition")
    print("2 pour la soustraction")
    print("3 pour la multiplication")
    print("4 pour la division")
    print("0 pour quitter")

    signe = input("Entrez votre choix : ")

    if signe == "1":
        resultat = nbr1 + nbr2
        print("Résultat :", resultat)

    elif signe == "2":
        resultat = nbr1 - nbr2
        print("Résultat :", resultat)

    elif signe == "3":
        resultat = nbr1 * nbr2
        print("Résultat :", resultat)

    elif signe == "4":

        if nbr2 != 0:
            resultat = nbr1 / nbr2
            print("Résultat :", resultat)
        else:
            print("Impossible de diviser par zéro")

    elif signe == "0":
        print("Programme terminé")
        break
    else:
        print("Choix invalide")