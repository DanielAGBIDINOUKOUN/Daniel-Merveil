
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