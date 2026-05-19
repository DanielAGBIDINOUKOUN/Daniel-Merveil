taches = []

while True:

    print("\n===== GESTION DES TÂCHES =====")
    print("1. Ajouter une tâche")
    print("2. Afficher les tâches")
    print("3. Supprimer une tâche")
    print("4. Marquer une tâche comme terminée")
    print("0. Quitter")

    choix = input("Entrez votre choix : ")

    # AJOUTER UNE TÂCHE
    if choix == "1":

        nombre = int(input("Combien de tâches voulez-vous ajouter ? "))

        for i in range(nombre):

            nom_tache = input(f"Tâche {i + 1} : ").strip()

            if nom_tache == "":
                print("La tâche ne peut pas être vide")

            else:

                nouvelle_tache = {
                    "nom": nom_tache,
                    "terminee": False
                }

                taches.append(nouvelle_tache)

        print("\nTâche(s) ajoutée(s) avec succès")

    # AFFICHER LES TÂCHES
    elif choix == "2":

        if len(taches) == 0:

            print("\nAucune tâche disponible")

        else:

            print("\n===== LISTE DES TÂCHES =====")

            for i, tache in enumerate(taches, start=1):

                statut = (
                    "✅ Terminée"
                    if tache["terminee"]
                    else "❌ Non terminée"
                )

                print(f"{i}. {tache['nom']} - {statut}")

    # SUPPRIMER UNE TÂCHE
    elif choix == "3":

        if len(taches) == 0:

            print("\nAucune tâche à supprimer")

        else:

            numero = int(input("Numéro de la tâche : "))

            if 1 <= numero <= len(taches):

                tache_supprimee = taches.pop(numero - 1)

                print(f"\nTâche supprimée : {tache_supprimee['nom']}")

            else:

                print("\nNuméro invalide")

    # MARQUER COMME TERMINÉE
    elif choix == "4":

        if len(taches) == 0:

            print("\nAucune tâche disponible")

        else:

            numero = int(input("Numéro de la tâche : "))

            if 1 <= numero <= len(taches):

                taches[numero - 1]["terminee"] = True

                print("\nTâche marquée comme terminée")

            else:

                print("\nNuméro invalide")

    # QUITTER
    elif choix == "0":

        print("\nProgramme terminé")
        break

    # CHOIX INVALIDE
    else:

        print("\nChoix invalide")
