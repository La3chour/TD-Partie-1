taches = []
choix = ""

while choix != "0":
    print("=== GESTION DES TACHES ===")
    print("1. Ajouter une tache")
    print("2. Afficher les taches")
    print("3. Rechercher une tache")
    print("0. Quitter")
    choix = input("Votre choix : ")

    if choix == "1":
        titre = input("Titre de la tache : ")
        if titre == "":
            print("Erreur : titre vide")
        else:
            taches.append(titre)
            print("Tache ajoutee avec succes.")

    elif choix == "2":
        if len(taches) == 0:
            print("Aucune tache.")
        else:
            i = 0
            while i < len(taches):
                print(i + 1, "-", taches[i])
                i = i + 1

    elif choix == "3":
        mot = input("Mot-cle : ")
        i = 0
        trouve = False
        while i < len(taches):
            if mot in taches[i]:
                print(i + 1, "-", taches[i])
                trouve = True
            i = i + 1
        if trouve == False:
            print("Aucune tache trouvee.")

    elif choix == "0":
        print("Au revoir")

    else:
        print("Erreur : option invalide")