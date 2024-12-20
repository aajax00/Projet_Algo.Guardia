# from Assets.br_charge import *
from .gestion_csv_produit import *
import pandas as pnd
import hashlib
import os
import time
import getpass

GREEN = "\033[1;32m"
RED = "\033[31m"
BLUE = "\033[94m"
JAUNE = "\033[33m"
END = "\033[0m" 

def instance():
    os.system('cls' if os.name == 'nt' else 'clear')

def create_userfile():
    file_path = "./data/Utilisateurs.csv"
    if not os.path.exists(file_path):
        user_dataf = pnd.DataFrame(columns=["user_id", "username", "mot_de_passe", "sel"])
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
        return pnd.DataFrame(columns=["user_id", "username", "mot_de_passe", "sel"])
    
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
def add_users(username, mdp):
    users = load_users()
    if username in users["username"].values:
        print(f"\n{RED}Nom d'utilisateur ou mot de passe déja pris{END}")
        return
    user_id = users["user_id"].max() + 1 if not users.empty else 1
    hashed_mdp, salt = hash_mdp(mdp)
    users = users._append({"user_id": user_id, "username": username, "mot_de_passe": hashed_mdp, "sel": salt}, ignore_index=True)
    save_users(users)    
    print(f"{GREEN}\nUtilisateur ajouté avec succès{END}")

    
    
    
# supprimer un utilisateur   
def supp_users(username, mdp):
    dataf = load_users()
    dataf = dataf[dataf["username"] != username]
    save_users(dataf)

# supprimer un produit utilisateur     
def supp_produit_user(user_id):
    dataf = load_produits()
    dataf = dataf[dataf["user_id"] != user_id]
    save_produit(dataf)

# comparaison BDD hashage compromise
# def compromis(hash_a_verif, Bddhash_compromis="Hashes_compromis.txt"):
#     with open(Bddhash_compromis, 'r') as fichier:
#         hashes_compromis = fichier.read().splitlines()
#     return hash_a_verif in hashes_compromis

def load_mdp_compromis():
    filepath = "./data/rockyou.txt"
    try:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as file:
            return set(line.strip() for line in file)
    except FileNotFoundError:
        print(f"{RED}Fichier {filepath} introuvable ! Assurez-vous qu'il est dans le bon dossier.{END}")
        return set()
    


def modif_info_user(username, mdp_actuel):
    users = load_users()
    user = users[users["username"] == username]
    if user.empty:
        print(f"{RED}\nUtilisateur non trouvé.{END}")
        return username
    
    user = user.iloc[0]
    hashed_mdp, salt = user["mot_de_passe"], eval(user["sel"])
    if hash_mdp(mdp_actuel, salt)[0] != hashed_mdp:
        print(f"{RED}\nMot de passe actuel incorrect.{END}")
        return username
    
    print(f"{JAUNE}Laissez vide si vous ne souhaitez pas modifier un champ.\n{END}")
    nouveau_nom = input(f"{GREEN}Nouveau nom d'utilisateur : {END}").strip()
    nouveau_mdp = getpass.getpass(f"{GREEN}Nouveau mot de passe : {END}").strip()

    mdp_compromis = load_mdp_compromis()
    # Vérification si le mot de passe est compromis
    if nouveau_mdp in mdp_compromis:
        print(f"{RED}\nLe nouveau mot de passe fait partie d'une basse de donneé compromise.{END}")
        print(f"{RED}Veuiilez en utiliser un autre.{END}")
        time.sleep(3)
        instance()
        return username

    # Mise à jour du nom d'utilisateur
    if nouveau_nom:
        if nouveau_nom in users["username"].values:
            print(f"{RED}Nom d'utilisateur déjà pris.{END}")
            return username
        else:
            users.loc[users["username"] == username, "username"] = nouveau_nom
            username = nouveau_nom

    # Mise à jour du mot de passe
    if nouveau_mdp:
        hashed_mdp, salt = hash_mdp(nouveau_mdp)
        users.loc[users["username"] == (nouveau_nom if nouveau_nom else username), "mot_de_passe"] = hashed_mdp
        users.loc[users["username"] == (nouveau_nom if nouveau_nom else username), "sel"] = salt
        
    save_users(users)
    print(f"{GREEN}\nVos informations ont été mises à jour avec succès !{END}")
    instance()
    return username