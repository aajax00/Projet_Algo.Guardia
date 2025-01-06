from .gestion_utilisateur import *
from Modules.api import *
import pandas as pnd
import hashlib
import time
import sys

JAUNE = "\033[33m"

# login form
def login_user(username, mdp):
    dataf_users = load_users()
    user = dataf_users[dataf_users["username"] == username]
    
    if user.empty:
        time.sleep(0.8)
        print(f"{RED}\nUtilisateur non trouvé{END}")
        time.sleep(1.5)
        return False
    
    user = user.iloc[0]
    mdp_hashed, salt = user['mot_de_passe'], eval(user["sel"])
    
    if hash_mdp(mdp, salt)[0] == mdp_hashed:
        time.sleep(1.3)
        print(f"{GREEN}\nConnexion reussi{END}")
        time.sleep(0.5)
        # Animation de chargement avec les symboles
        print(f"{JAUNE}Chargement de la session", end="")
        sys.stdout.flush()  # Pour s'assurer que le texte est imprimé immédiatement
        duration = 1.2
        symbols = ['/', '-', '\\', '|']
        start_time = time.time()
        # Boucle d'animation
        while time.time() - start_time < duration:
            for symbol in symbols:
        # Afficher "chargement..." avec le symbole actuel
                sys.stdout.write(f"\rChargement de la session... {symbol}")
                sys.stdout.flush()
                time.sleep(0.1)
        return user["user_id"]
    else:
        print(f"{RED}\nMot de passe incorrect{END}")
        return False

    
    
    
    
    # if verif_users(nom, mot_de_passe):
    #     print("Connexion Reussie\nBienvenue {nom}.")
    # else:
    #     print("nom ou mdp incorrect")
    

# verification de mot de passe haché
def verif_mdp(stock_hash, mdp, salt):
        return stock_hash == hash_mdp(mdp, salt)[0]


# verifier un utilisateur
def verif_users(username, mot_de_passe):
    dataf_users = pnd.read_csv("../data/Utilisateurs.csv")
    sorted_user = dataf_users[dataf_users["username"] == username]
    
    if sorted_user.empty:
        print(f"{RED}Utilisateur introuvable{END}")
        return False
    
    mdp_hashed = sorted_user.iloc[0]['mot_de_passe']
    salt = sorted_user.iloc[0]['sel']
    
    if not verif_mdp(mdp_hashed, mot_de_passe, salt):
        print(f"{RED}Mot de passe incorrect{END}")
        return False
    return True
        

        
    print ("Authentification reussi")

