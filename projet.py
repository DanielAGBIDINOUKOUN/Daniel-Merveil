# =========================================
#     PROJET PYTHON MULTI PROGRAMMES
# =========================================
# 1. Calculatrice
# 2. Gestion Etudiant
# 3. Todo List
# Sauvegarde des données dans des fichiers
# =========================================

import json
import os


# =========================================
#           FONCTIONS FICHIERS
# =========================================

def charger_fichier(nom_fichier):

    if os.path.exists(nom_fichier):

        with open(nom_fichier, "r") as fichier:
            return json.load(fichier)

    return []


def sauvegarder_fichier(nom_fichier, donnees):

    with open(nom_fichier, "w") as fichier:
        json.dump(donnees, fichier, indent=4)


# =========================================
#             CALCULATRICE
# =========================================

def calculatrice():

    while True:

        print("\n===== CALCULATRICE =====")

        nbr1 = float(input("Entrez le premier nombre : "))
        nbr2 = float(input("Entrez le deuxième nombre : "))

        print("\n1. Addition")
        print("2. Soustraction")
        print("3. Multiplication")
        print("4. Division")
        print("0. Retour")

        choix = input("Choisissez une opération : ")

        if choix == "1":
            print("Résultat :", nbr1 + nbr2)

        elif choix == "2":
            print("Résultat :", nbr1 - nbr2)

        elif choix == "3":
            print("Résultat :", nbr1 * nbr2)

        elif choix == "4":

            if nbr2 != 0:
                print("Résultat :", nbr1 / nbr2)

            else:
                print("Division impossible")

        elif choix == "0":
            break

        else:
            print("Choix invalide")


# =========================================
#          GESTION ETUDIANT
# =========================================

def gestion_etudiant():

    fichier = "etudiants.json"

    etudiants = charger_fichier(fichier)

    while True:

        print("\n===== GESTION ETUDIANT =====")

        print("1. Ajouter un étudiant")
        print("2. Afficher les étudiants")
        print("3. Rechercher un étudiant")
        print("4. Supprimer un étudiant")
        print("0. Retour")

        choix = input("Votre choix : ")

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

            sauvegarder_fichier(fichier, etudiants)

            print("Étudiant ajouté")

        # AFFICHER
        elif choix == "2":

            if len(etudiants) == 0:
                print("Aucun étudiant")

            else:

                for i, etudiant in enumerate(etudiants):

                    print(f"\nEtudiant {i + 1}")

                    print("Nom :", etudiant["nom"])
                    print("Age :", etudiant["age"])
                    print("Filière :", etudiant["filiere"])

        # RECHERCHER
        elif choix == "3":

            recherche = input("Nom à rechercher : ")

            trouve = False

            for etudiant in etudiants:

                if etudiant["nom"].lower() == recherche.lower():

                    print("\nÉtudiant trouvé")

                    print("Nom :", etudiant["nom"])
                    print("Age :", etudiant["age"])
                    print("Filière :", etudiant["filiere"])

                    trouve = True

            if trouve == False:
                print("Étudiant introuvable")

        # SUPPRIMER
        elif choix == "4":

            nom_supprimer = input("Nom à supprimer : ")

            trouve = False

            for etudiant in etudiants:

                if etudiant["nom"].lower() == nom_supprimer.lower():

                    etudiants.remove(etudiant)

                    sauvegarder_fichier(fichier, etudiants)

                    print("Étudiant supprimé")

                    trouve = True
                    break

            if trouve == False:
                print("Étudiant introuvable")

        # RETOUR
        elif choix == "0":
            break

        else:
            print("Choix invalide")


# =========================================
#               TODO LIST
# =========================================

def todo_list():

    fichier = "taches.json"

    taches = charger_fichier(fichier)

    while True:

        print("\n===== TODO LIST =====")

        print("1. Ajouter une tâche")
        print("2. Afficher les tâches")
        print("3. Supprimer une tâche")
        print("4. Marquer comme terminée")
        print("0. Retour")

        choix = input("Votre choix : ")

        # AJOUTER
        if choix == "1":

            nom = input("Entrez la tâche : ")

            tache = {
                "nom": nom,
                "terminee": False
            }

            taches.append(tache)

            sauvegarder_fichier(fichier, taches)

            print("Tâche ajoutée")

        # AFFICHER
        elif choix == "2":

            if len(taches) == 0:
                print("Aucune tâche")

            else:

                for i, tache in enumerate(taches):

                    statut = "Terminée" if tache["terminee"] else "Non terminée"

                    print(f"{i + 1}. {tache['nom']} - {statut}")

        # SUPPRIMER
        elif choix == "3":

            numero = int(input("Numéro à supprimer : "))

            if 1 <= numero <= len(taches):

                taches.pop(numero - 1)

                sauvegarder_fichier(fichier, taches)

                print("Tâche supprimée")

            else:
                print("Numéro invalide")

        # TERMINER
        elif choix == "4":

            numero = int(input("Numéro terminé : "))

            if 1 <= numero <= len(taches):

                taches[numero - 1]["terminee"] = True

                sauvegarder_fichier(fichier, taches)

                print("Tâche terminée")

            else:
                print("Numéro invalide")

        # RETOUR
        elif choix == "0":
            break

        else:
            print("Choix invalide")


# =========================================
#             MENU PRINCIPAL
# =========================================

while True:

    print("\n=================================")
    print("       PROJET PYTHON")
    print("=================================")

    print("1. Calculatrice")
    print("2. Gestion Etudiant")
    print("3. Todo List")
    print("0. Quitter")

    choix = input("Votre choix : ")

    if choix == "1":
        calculatrice()

    elif choix == "2":
        gestion_etudiant()

    elif choix == "3":
        todo_list()

    elif choix == "0":

        print("Programme terminé")
        break

    else:
        print("Choix invalide")