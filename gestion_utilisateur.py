import pandas as pnd
import hashlib
import os

# charger les utilisateur depuis fichier csv
def load_users():
    try:
        return pnd.read_csv("Utilisateurs.csv")
    except FileNotFoundError:
        return pnd.DataFrame(columns=["nom", "mot_de_passe"])
    
# sauvegarder les utilisateur
def save_users(dataf):
    dataf.to_csv("Utilsateurs.csv", index=False)
    
# hachage mot de passe
def hash_mdp(mdp, salt=None):
    if not salt:
        salt = os.urandom(16)
    hash = hashlib.sha256(salt + mdp.encode()).hexdigest()
    return hash, salt
    
# ajouter un utilisateur
def add_users(nom, mdp):
    sel = os.urandom(16)
    hash = hash_mdp(mdp, sel)
    dataf = load_users()
    dataf = dataf._append({"nom": nom, "mot_de_passe": hash[0], "sel": hash[1]}, ignore_index=True)
    save_users(dataf)
    
# supprimer un utilisateur   
def supp_users(nom):
    dataf = load_users()
    dataf = dataf[dataf["nom"] != nom]
    save_users(dataf)
    
# verification de mot de passe haché
def verif_mdp(stock_hash, mdp, salt):
    return stock_hash == hash_mdp(mdp, salt)[0]