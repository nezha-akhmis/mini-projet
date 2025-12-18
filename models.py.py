class Produit:
    def __init__(self, id, nom, prix):
        self.id = id
        self.nom = nom
        self.prix = prix

    def __str__(self):
        return f"Produit(id={self.id}, nom={self.nom}, prix={self.prix} DH)"


class Client:
    def __init__(self, id, nom, email):
        self.id = id
        self.nom = nom
        self.email = email

    def __str__(self):
        return f"Client(id={self.id}, nom={self.nom}, email={self.email})"
