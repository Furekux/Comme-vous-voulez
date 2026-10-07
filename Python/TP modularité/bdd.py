# bdd.py
import sqlite3

def connecter(chemin):
    """Ouvre (ou crée) la base et la table contact. Renvoie la connexion."""
    connexion = sqlite3.connect(chemin)
    connexion.execute("""
        CREATE TABLE IF NOT EXISTS contact (
            nom TEXT PRIMARY KEY,
            telephone TEXT NOT NULL
        )
    """)
    connexion.commit()
    return connexion

def charger(connexion):
    """Renvoie la liste des contacts triée par nom."""
    curseur = connexion.execute("SELECT nom, telephone FROM contact ORDER BY nom")
    return curseur.fetchall()

def inserer(connexion, nom, telephone):
    """Insère un contact dans la base."""
    connexion.execute(
        "INSERT INTO contact (nom, telephone) VALUES (?, ?)", (nom, telephone)
    )
    connexion.commit()

def supprimer(connexion, nom):
    """Supprime un contact de la base."""
    connexion.execute("DELETE FROM contact WHERE nom = ?", (nom,))
    connexion.commit()