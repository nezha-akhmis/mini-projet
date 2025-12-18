import sqlite3
from models import Produit, Client

DB_NAME = "boutique.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def create_tables():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS produit (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT,
            prix REAL
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS client (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT,
            email TEXT UNIQUE
        )
    """)

    conn.commit()
    conn.close()


def ajouter_produit(produit):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO produit (nom, prix) VALUES (?, ?)",
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
        "UPDATE produit SET prix=? WHERE id=?",
        (nouveau_prix, id_produit)
    )
    conn.commit()
    conn.close()


def ajouter_client(client):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO client (nom, email) VALUES (?, ?)",
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
    cur.execute("SELECT * FROM client WHERE email=?", (email,))
    row = cur.fetchone()
    conn.close()
    return Client(*row) if row else None
