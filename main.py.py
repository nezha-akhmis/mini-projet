from models import Produit, Client
import sqlite_dao as dao
# pour MySQL : import mysql_dao as dao

dao.create_tables()

while True:
    print("\n===== MENU =====")
    print("1. Ajouter produit")
    print("2. Lister produits")
    print("3. Ajouter client")
    print("4. Lister clients")
    print("5. Chercher client par email")
    print("6. Modifier prix produit")
    print("0. Quitter")

    choix = input("Choix : ")

    if choix == "1":
        nom = input("Nom produit : ")
        prix = float(input("Prix : "))
        dao.ajouter_produit(Produit(None, nom, prix))

    elif choix == "2":
        for p in dao.lister_produits():
            print(p)

    elif choix == "3":
        nom = input("Nom client : ")
        email = input("Email : ")
        dao.ajouter_client(Client(None, nom, email))

    elif choix == "4":
        for c in dao.lister_clients():
            print(c)

    elif choix == "5":
        email = input("Email : ")
        client = dao.chercher_client_par_email(email)
        print(client if client else "Client non trouvé")

    elif choix == "6":
        idp = int(input("ID produit : "))
        prix = float(input("Nouveau prix : "))
        dao.modifier_prix_produit(idp, prix)

    elif choix == "0":
        break

    else:
        print("Choix invalide")
