etudiants = []

while True:

    print("\n===== MENU =====")
    print("1. Ajouter un étudiant")
    print("2. Afficher les étudiants")
    print("3. Rechercher un étudiant")
    print("4. Supprimer un étudiant")
    print("0. Quitter")

    choix = input("Entrez votre choix : ")

    # AJOUTER
    if choix == "1":

        nom = input("Nom : ")
        prenom = input("Prénom : ")
        age = int(input("Age : "))
        filiere = input("Filière : ")

        etudiant = {
            "nom": nom,
            "prenom": prenom,
            "age": age,
            "filiere": filiere
        }

        etudiants.append(etudiant)

        print("Étudiant ajouté avec succès")

    # AFFICHER
    elif choix == "2":

        if len(etudiants) == 0:
            print("Aucun étudiant enregistré")

        else:
            print("\n===== LISTE DES ETUDIANTS =====")

            for i, etudiant in enumerate(etudiants):

                print(f"\nEtudiant {i + 1}")
                print("Nom :", etudiant["nom"])
                print("Prénom :", etudiant["prenom"])   
                print("Age :", etudiant["age"])
                print("Filière :", etudiant["filiere"])

    # RECHERCHER
    elif choix == "3":

        recherche = input("Entrez le nom de l'étudiant : ")

        trouve = False

        for etudiant in etudiants:

            if etudiant["nom"].lower() == recherche.lower():

                print("\nEtudiant trouvé")
                print("Nom :", etudiant["nom"])
                print("Prénom :", etudiant["prenom"])
                print("Age :", etudiant["age"])
                print("Filière :", etudiant["filiere"])

                trouve = True

        if trouve == False:
            print("Étudiant introuvable")

    # SUPPRIMER
    elif choix == "4":

        nom_supprimer = input("Entrez le nom à supprimer : ")

        trouve = False

        for etudiant in etudiants:

            if etudiant["nom"].lower() == nom_supprimer.lower():

                etudiants.remove(etudiant)

                print("Étudiant supprimé")
                trouve = True
                break

        if trouve == False:
            print("Étudiant introuvable")

    # QUITTER
    elif choix == "0":

        print("Programme terminé")
        break

    # ERREUR
    else:
        print("Choix invalide")
        
        