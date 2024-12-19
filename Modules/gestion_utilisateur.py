# from Assets.br_charge import *
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
        user_dataf = pnd.DataFrame(columns=["user_id", "nom", "mot_de_passe", "sel"])
        user_dataf.to_csv(file_path, index=False)
        print(f"{BLUE}Création de la Base de donnée utilisateur ...{END}\n")
        time.sleep(0.02)
        print(f"{GREEN}Base de donnée creé avec succès{END}\n{BLUE}Chargement du fichier 💾... !")
        # br_charge()
        print(f"{GREEN}-- Utilisateurs.csv --{END}\n")

    else:
        print(f"{GREEN}-- CREATION D'UTILISATEUR --{END}\n")
        user_dataf = pnd.read_csv(file_path)
        if "user_id" not in user_dataf.columns:
            print("ajout de la colonne 'user_id'")
            user_dataf["user_id"] = range(1, len(user_dataf) + 1)
            save_users(user_dataf)
        

# charger les utilisateur depuis fichier csv
def load_users():
    try:
        return pnd.read_csv("./data/Utilisateurs.csv")
    except FileNotFoundError:
        return pnd.DataFrame(columns=["user_id", "nom", "mot_de_passe", "sel"])
    
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
    users = load_users()
    if nom in users["nom"].values:
        print(f"\n{RED}Nom d'utilisateur ou mot de passe déja pris{END}")
        return
    user_id = users["user_id"].max() + 1 if not users.empty else 1
    hashed_mdp, salt = hash_mdp(mdp)
    users = users._append({"user_id": user_id, "nom": nom, "mot_de_passe": hashed_mdp, "sel": salt}, ignore_index=True)
    save_users(users)    
    print("Utilisateur ajouté avec succès")

    
    
    
# supprimer un utilisateur   
def supp_users(nom, mdp):
    dataf = load_users()
    dataf = dataf[dataf["nom"] != nom]
    save_users(dataf)

# comparaison BDD hashage compromise
def compromis(hash_a_verif, Bddhash_compromis="Hashes_compromis.txt"):
    with open(Bddhash_compromis, 'r') as fichier:
        hashes_compromis = fichier.read().splitlines()
    return hash_a_verif in hashes_compromis