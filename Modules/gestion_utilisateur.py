from Assets.br_charge import *
import pandas as pnd
import hashlib
import os
import time

GREEN = "\033[1;32m"
RED = "\033[31m"
BLUE = "\033[94m"
END = "\033[0m" 

def create_userfile():
    file_path = "./data/Utilisateurs.csv"
    if not os.path.exists(file_path):
        produit_dataf = pnd.DataFrame(columns=["nom", "mot_de_passe"])
        produit_dataf.to_csv(file_path, index=False)
        print(f"{BLUE}Création de la Base de donnée utilisateur ...{END}\n")
        time.sleep(0.02)
        print(f"{GREEN}Base de donnée creé avec succès{END}\n{BLUE}Chargement du fichier 💾... !")
        br_charge()
        print(f"{GREEN}-- Utilisateurs.csv --{END}\n")

    else:
        print(f"{GREEN}-- Utilisateurs.csv --{END}\n")
        produit_dataf = pnd.read_csv(file_path)
        

# charger les utilisateur depuis fichier csv
def load_users():
    try:
        return pnd.read_csv("./data/Utilisateurs.csv")
    except FileNotFoundError:
        return pnd.DataFrame(columns=["nom", "mot_de_passe"])
    
# sauvegarder les utilisateur
def save_users(dataf):
    dataf.to_csv("./data/Utilisateurs.csv", index=False)
    
# hachage mot de passe
def hash_mdp(mdp, salt=None):
    if not salt:
        salt = os.urandom(16)
    hash = hashlib.sha256(salt + mdp.encode('utf-8')).hexdigest()
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

# comparaison BDD hashage compromise
def compromis(hash_a_verif, Bddhash_compromis="Hashes_compromis.txt"):
    with open(Bddhash_compromis, 'r') as fichier:
        hashes_compromis = fichier.read().splitlines()
    return hash_a_verif in hashes_compromis