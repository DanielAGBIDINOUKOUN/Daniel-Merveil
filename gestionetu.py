etudiants = []

while True:

    print("\n===== GESTION DES ÉTUDIANTS =====")
    print("1. Ajouter des étudiants")
    print("2. Afficher les étudiants")
    print("3. Rechercher un étudiant")
    print("4. Supprimer un étudiant")
    print("0. Quitter")

    choix = input("Entrez votre choix : ")

    # AJOUTER DES ÉTUDIANTS
    if choix == "1":

        nombre = int(input("Combien d'étudiants voulez-vous ajouter ? "))

        for i in range(nombre):

            print(f"\n===== Étudiant {i + 1} =====")

            nom = input("Nom : ").strip()
            prenom = input("Prénom : ").strip()
            age = int(input("Âge : "))
            filiere = input("Filière : ").strip()

            etudiant = {
                "nom": nom,
                "prenom": prenom,
                "age": age,
                "filiere": filiere
            }

            etudiants.append(etudiant)

        print("\nÉtudiants ajoutés avec succès")

    # AFFICHER LES ÉTUDIANTS
    elif choix == "2":

        if len(etudiants) == 0:

            print("\nAucun étudiant enregistré")

        else:

            print("\n===== LISTE DES ÉTUDIANTS =====")

            for i, etudiant in enumerate(etudiants, start=1):

                print(f"\nÉtudiant {i}")
                print("-" * 20)
                print("Nom :", etudiant["nom"])
                print("Prénom :", etudiant["prenom"])
                print("Âge :", etudiant["age"])
                print("Filière :", etudiant["filiere"])

    # RECHERCHER UN ÉTUDIANT
    elif choix == "3":

        recherche = input("Entrez le nom de l'étudiant : ").strip()

        trouve = False

        for etudiant in etudiants:

            if etudiant["nom"].lower() == recherche.lower():

                print("\n===== ÉTUDIANT TROUVÉ =====")
                print("Nom :", etudiant["nom"])
                print("Prénom :", etudiant["prenom"])
                print("Âge :", etudiant["age"])
                print("Filière :", etudiant["filiere"])

                trouve = True
                break

        if not trouve:

            print("\nÉtudiant introuvable")

    # SUPPRIMER UN ÉTUDIANT
    elif choix == "4":

        nom_supprimer = input("Entrez le nom à supprimer : ").strip()

        trouve = False

        for etudiant in etudiants:

            if etudiant["nom"].lower() == nom_supprimer.lower():

                etudiants.remove(etudiant)

                print("\nÉtudiant supprimé avec succès")

                trouve = True
                break

        if not trouve:

            print("\nÉtudiant introuvable")

    # QUITTER
    elif choix == "0":

        print("\nProgramme terminé")
        break

    # CHOIX INVALIDE
    else:

        print("\nChoix invalide")