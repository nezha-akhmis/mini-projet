import mysql.connector
from models import Produit, Client


def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="boutique"
    )


def ajouter_produit(produit):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO produit (nom, prix) VALUES (%s, %s)",
        (produit.nom, produit.prix)
    )
    conn.commit()
    conn.close()


def lister_produits():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM produit")
    rows = cur.fetchall()
    conn.close()
    return [Produit(*row) for row in rows]


def modifier_prix_produit(id_produit, nouveau_prix):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE produit SET prix=%s WHERE id=%s",
        (nouveau_prix, id_produit)
    )
    conn.commit()
    conn.close()


def ajouter_client(client):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO client (nom, email) VALUES (%s, %s)",
        (client.nom, client.email)
    )
    conn.commit()
    conn.close()


def lister_clients():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM client")
    rows = cur.fetchall()
    conn.close()
    return [Client(*row) for row in rows]


def chercher_client_par_email(email):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM client WHERE email=%s", (email,))
    row = cur.fetchone()
    conn.close()
    return Client(*row) if row else None
