nbr1 = float(input('Entrez le premier nombre : '))
nbr2 = float(input('Entrez le deuxième nombre : '))

for i in range(5):

    signe = input(
        "Entrez le signe de l'opération :\n"
        "1 pour l'addition\n"
        "2 pour la soustraction\n"
        "3 pour la multiplication\n"
        "4 pour la division\n"
        "0 pour quitter\n"
    )

    if signe == "1":
        print(nbr1 + nbr2)
        

    elif signe == "2":
        print(nbr1 - nbr2)

    elif signe == "3":
        print(nbr1 * nbr2)

    elif signe == "4":
        print(nbr1 / nbr2)

    elif signe == "0":
        break

    else:
        print("Choix invalide")
        
