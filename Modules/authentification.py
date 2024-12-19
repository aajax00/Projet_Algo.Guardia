from .gestion_utilisateur import *
import pandas as pnd
import hashlib

# login form
def login_user(nom, mdp):
    dataf_users = load_users()
    user = dataf_users[dataf_users["nom"] == nom]
    
    if user.empty:
        print("utilisateur non trouvé")
        return False
    
    user = user.iloc[0]
    mdp_hashed, salt = user['mot_de_passe'], eval(user["sel"])
    
    if hash_mdp(mdp, salt)[0] == mdp_hashed:
        print("connexion reussi")
        return user["user_id"]
    else:
        print("mdp incorrect")
        return False

    
    
    
    
    # if verif_users(nom, mot_de_passe):
    #     print("Connexion Reussie\nBienvenue {nom}.")
    # else:
    #     print("nom ou mdp incorrect")
    

# verification de mot de passe haché
    def verif_mdp(stock_hash, mdp, salt):
        return stock_hash == hash_mdp(mdp, salt)[0]


# verifier un utilisateur
def verif_users(nom, mot_de_passe):
    dataf_users = pnd.read_csv("../data/Utilisateurs.csv")
    sorted_user = dataf_users[dataf_users["nom"] == nom]
    
    if sorted_user.empty:
        print("Utilisateur introuvable")
        return False
    
    mdp_hashed = sorted_user.iloc[0]['mot_de_passe']
    salt = sorted_user.iloc[0]['sel']
    
    if not verif_mdp(mdp_hashed, mot_de_passe, salt):
        print("Mot de passe incorrect")
        return False
    return True
        

        
    print ("Authentification reussi")

