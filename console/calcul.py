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
        
        
#=============================================

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
        age = input("Age : ")
        filiere = input("Filière : ")

        etudiant = {
            "nom": nom,
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
        
        
        
# =========================
#        TODO LIST
# =========================

taches = []

while True:

    print("\n===== MENU =====")
    print("1. Ajouter une tâche")
    print("2. Afficher les tâches")
    print("3. Supprimer une tâche")
    print("4. Marquer une tâche comme terminée")
    print("0. Quitter")

    choix = input("Entrez votre choix : ")

    # AJOUTER UNE TÂCHE
    if choix == "1":

        tache = input("Entrez la tâche : ")

        nouvelle_tache = {
            "nom": tache,
            "terminee": False
        }

        taches.append(nouvelle_tache)

        print("Tâche ajoutée avec succès")

    # AFFICHER LES TÂCHES
    elif choix == "2":

        if len(taches) == 0:
            print("Aucune tâche disponible")

        else:

            print("\n===== LISTE DES TÂCHES =====")

            for i, tache in enumerate(taches):

                statut = "✅ Terminée" if tache["terminee"] else "❌ Non terminée"

                print(f"{i + 1}. {tache['nom']} - {statut}")

    # SUPPRIMER UNE TÂCHE
    elif choix == "3":

        if len(taches) == 0:
            print("Aucune tâche à supprimer")

        else:

            numero = int(input("Numéro de la tâche à supprimer : "))

            if 1 <= numero <= len(taches):

                supprimer = taches.pop(numero - 1)

                print("Tâche supprimée :", supprimer["nom"])

            else:
                print("Numéro invalide")

    # MARQUER COMME TERMINÉE
    elif choix == "4":

        if len(taches) == 0:
            print("Aucune tâche disponible")

        else:

            numero = int(input("Numéro de la tâche terminée : "))

            if 1 <= numero <= len(taches):

                taches[numero - 1]["terminee"] = True

                print("Tâche marquée comme terminée")

            else:
                print("Numéro invalide")

    # QUITTER
    elif choix == "0":

        print("Programme terminé")
        break

    # ERREUR
    else:
        print("Choix invalide")