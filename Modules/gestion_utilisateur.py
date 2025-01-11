# from Assets.br_charge import *
from .gestion_csv_produit import *
from Modules.api import *
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
        user_dataf = pnd.DataFrame(columns=["user_id", "username", "mot_de_passe", "sel", "role", "email"])
        user_dataf.to_csv(file_path, index=False)
        print(f"{BLUE}Création de la Base de donnée utilisateur ...{END}\n")
        time.sleep(0.02)
        print(f"{GREEN}Base de donnée creé avec succès{END}\n{BLUE}Chargement du fichier 💾... !")
        # br_charge()
        print(f"{GREEN}-- Utilisateurs.csv --{END}\n")
        
        users = pnd.read_csv(file_path)
        if "email" not in users.columns:
            print("Ajout de la colonne 'email' au ficiuer existant.")
            users["email"] = ""
            save_users(users)

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
        return pnd.DataFrame(columns=["user_id", "username", "mot_de_passe", "sel", "role", "email"])
    
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
def add_users(username, mdp, email, role="user"):
    users = load_users()
    if email in users["email"].values:
        print(f"{RED}L'adresse email existe deja{END}")
        return
    if username in users["username"].values:
        print(f"\n{RED}Nom d'utilisateur ou mot de passe déja pris{END}")
        return
    user_id = users["user_id"].max() + 1 if not users.empty else 1
    hashed_mdp, salt = hash_mdp(mdp)
    users = users._append({"user_id": user_id, "username": username, "mot_de_passe": hashed_mdp, "sel": salt, "role": role, "email": email}, ignore_index=True)
    mdp_connect(mdp)
    time.sleep(2.5)
    save_users(users)    
    print(f"{GREEN}\nUtilisateur ajouté avec succès{END}")

add_users("admin", "admin.@.", "agardien001@gmailcom", "admin")
    
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
    current_email = user["email"]
    new_email = input(f"{GREEN}Nouvelle email (actuelle: {current_email}) :{END}").strip()
    
    nouveau_nom = input(f"{GREEN}Nouveau nom d'utilisateur : {END}").strip()
    nouveau_mdp = getpass.getpass(f"{GREEN}Nouveau mot de passe : {END}").strip()

    mdp_compromis = load_mdp_compromis()
    # Vérification si le mot de passe est compromis
    if nouveau_mdp in mdp_compromis:
        print(f"{RED}\nLe nouveau mot de passe fait partie d'une basse de donneé compromise.{END}")
        print(f"{RED}Veuiilez en utiliser un autre !{END}")
        time.sleep(3)
        instance()
        return username
    
    if new_email:
        if new_email in users["email"].values:
            print(f"{RED}Cet adresse email est déja utilisée.{END}")
            return username
        else:
            users.loc[users["username"] == (nouveau_nom if nouveau_nom else username), "email"] = new_email

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
    time.sleep(1.5)
    instance()
    return username



######ADIMN PANEL ##########################################
def aff_produits_admin(user_id):
    dataf = load_produits()
    produits = dataf[dataf["user_id"] == user_id]
    if not produits.empty:
        print(f"{GREEN}-{END}" * 30)
        print(produits[['nom' ,'prix' ,'quantité']].to_string(index=False))
        print(f"{GREEN}-{END}" * 30)
    else:
        print(f"{RED}Aucun produit trouvé pour l'utilisateur {END}{JAUNE}{user_id}{END}{RED}.{END}")

def afficher_tous_les_produits_admin():
    dataf = load_produits()
    if dataf.empty:
        print(f"{RED}Aucun produit trouvé dans la base de données.{END}")
    else:
        print(f"{GREEN}Liste des produits :{END}")
    print(dataf[['nom' ,'prix' ,'quantité', "user_id"]].to_string(index=False))

def aff_all_user():
    users = load_users()
    if users.empty:
        print(f"{RED}Aucun utilisateur trouvé.{END}")
        return
    
    else:
        print(f"{GREEN}--- Liste des utilisateurs ---{END}")  
        print(users[['user_id' ,'username' ,'role']].to_string(index=False))
    print("-" * 30)

def supp_user_admin(username):
    users = load_users()
    user = users[users["username"] == username]
    if user.empty:
        print(f"{RED}Utilisateur avec le nom {END}{JAUNE}{username}{END}{RED} non trouvé.{END}")
        return
    
    user_id = user["user_id"].values[0]
    supp_produit_user(user_id)
    print(f"{GREEN}Produits associés à l'utilisateur {username} supprimés.{END}")
    time.sleep(1)    
        
    users = users[users["username"] != username]
    save_users(users)
    print(f"{GREEN}L'utilisateur {username} a été supprimé avec succès.{END}")

def search_user_admin(username):
    users = load_users()
    user = users[users["username"] == username]
    if user.empty:
        print(f"{RED}Utilisateur non trouvé.{END}")
        return
    print(f"{GREEN}Utilisateur trouvé: {END}")
    print(user)
    user_id = user["user_id"].values[0]
    aff_produits_admin(user_id)
    
def search_produit_admin():
    nom_produit = input(f"{GREEN}Entrez le nom du produit à rechercher : {END}").strip().lower()
    produits = load_produits()
    
    
    produits_found = search_produit(produits, nom_produit, user_id)
    if produits_found.empty:
        print(f"{RED}Aucun produit trouvé avec le nom '{nom_produit}'.{END}")
        return
    print(f"{GREEN}--- Produits trouvés ---{END}")
    print(f"{'Produit':<20} {'Prix':<10} {'Quantité':<10} {'Utilisateur'}")
    print("-" * 60)
    
    for _, produit in produits_found.iterrows():
        user_id = produit["user_id"]
        users = load_users()
        user = users[users["user_id"] == user_id]
        if not user.empty:
            user_name = user.iloc[0]["username"]
        else:
            user_name = "Inconnu"
        
    print(f"{produit['nom']:<20} {produit['prix']:<10} {produit['quantité']:<10} {user_name}")
    print("-" * 60)



def is_admin(username, mdp):
    d_users = load_users()
    user = d_users[d_users["username"] == username]
    if user.empty:
        print(f"{RED}Utilisateur non trouvé.{END}")
        return False
    
    user = user.iloc[0]
    salt = eval(user["sel"])
    hashed_mdp_saisi, _ = hash_mdp(mdp, salt)
    
    if hashed_mdp_saisi != user["mot_de_passe"]:
        print(f"{RED}Vous n'êtes pas un administrateur, accès refusé.{END}")
        return False
    
    if user["user_id"] == 1:
        return True
    
    # else:
    #     print(f"{RED}\nL'utilisateur {username} n'est pas un admin.{END}")
    #     return False

    
    # return user["role"].values[0] == "admin"

def add_produit_admin():
    nom = input(f"{GREEN}Nom du produit : {END}")
    prix = float(input(f"{GREEN}Prix du produit : {END}"))
    quantité = int(input(f"{GREEN}Quantité du produit : {END}"))
    username = input(f"{GREEN}nom de l'utilisateur pour lequel ajouter le produit: {END}")
    
    users = load_users()
    # user_id = users[users["user_id"] == user_id]
    if username not in users["username"].values:
        print(f"{RED}Utilisateur {END}{JAUNE}{username} {END}{JAUNE}non trouvé.{END}")
        return
    add_produit(nom, prix, quantité, username)
    print(f"{GREEN}Produit ajouté avec succès pour l'utilisateur {END}{JAUNE}{username}{END}{GREEN}.{END}")

def supp_produit_admin():
    username = input(f"{GREEN}nom de l'utilisateur pour lequel supprimer un produit : {END}")
    users = load_users()
    if username not in users["username"].values:
        print(f"{RED}Utilisateur {END}{JAUNE}{username}{END}{RED} non trouvé.{END}")
        return
    
    produit_nom = input(f"{GREEN}Nom du produit à supprimer pour {username} : {END}")
    supp_produit(produit_nom)
    print(f"{GREEN}Produit {END}{BLUE}'{produit_nom}'{END}{GREEN} supprimé pour l'utilisateur {username}.{END}")
    
    
def trier_produits_admin():
    # Charger les produits
    produits = load_produits()
    
    if produits.empty:
        print(f"{RED}Aucun produit à trier.{END}")
        return
    
    print(f"{GREEN}--- Critères de tri ---{END}")
    print("1. Nom")
    print("2. Prix")
    print("3. Quantité")
    
    critere = input(f"{GREEN}Choisissez un critère de tri (1-3) : {END}")
    
    if critere not in ["1", "2", "3"]:
        print(f"{RED}Critère de tri invalide.{END}")
        return
    
    if critere == "1":
        critere_colonne = "nom"
    elif critere == "2":
        critere_colonne = "prix"
    elif critere == "3":
        critere_colonne = "quantité"

    print(f"{GREEN}--- Algorithmes de tri ---{END}")
    print("1. Tri à bulles")
    print("2. Tri rapide")
    
    algo = input(f"{GREEN}Choisissez un algorithme de tri (1-2) : {END}")
    
    if algo == "1":
        algo_type = "bulle"
    elif algo == "2":
        algo_type = "rapide"
    else:
        print(f"{RED}Algorithme de tri invalide.{END}")
        return
    
    # Trier les produits en fonction du critère et de l'algorithme
    produits_tries = sort_produit(algo_type, critere_colonne, user_id=None)
    
    # Afficher les produits triés
    print(f"{GREEN}--- Produits triés ---{END}")
    print(f"{'Nom':<20} {'Prix':<10} {'Quantité':<10} {'User ID':<10} {'Utilisateurs'}")
    print("-" * 60)
    
    for _, produit in produits_tries.iterrows():
        # Récupérer l'ID utilisateur qui a ajouté ce produit
        user_id = produit["user_id"]
        
        # Charger les informations de l'utilisateur
        utilisateurs = load_users()
        utilisateur = utilisateurs[utilisateurs["user_id"] == user_id]
        if not utilisateur.empty:
            user_name = utilisateur.iloc[0]["username"]
        else:
            user_name = "Inconnu"
        
        # Afficher les informations du produit et le nom de l'utilisateur
        print(f"{produit['nom']:<20} {produit['prix']:<10} {produit['quantité']:<10} {produit['user_id']:<10} {user_name}")
    
    print(f"{GREEN}--- Fin du tri des produits ---{END}")