import hashlib
import requests
import pandas as pd
from datetime import datetime
import os

GREEN = "\033[1;32m"
RED = "\033[31m"
BLUE = "\033[94m"
JAUNE = "\033[33m"
END = "\033[0m" 

def mdp_compromis(mdp):
    try:
        historique_df = pd.read_csv('./data/logs_mdp.csv')
    except FileNotFoundError:
        historique_df = pd.DataFrame(columns=["mdp", "date_verif", "compromis", "nbr_x_compromis"])
    
    sha1_hash = hashlib.sha1(mdp.encode('utf-8')).hexdigest().upper()
    
    hash_prefix = sha1_hash[:5]
    hash_suffix = sha1_hash[5:]
    
    url = f"https://api.pwnedpasswords.com/range/{hash_prefix}"
    date_verif = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    response = requests.get(url)
    compromis_L = []
    
    if response.status_code == 200:
        hashes = response.text.splitlines()
        for h in hashes:
            suffix, count = h.split(':')
            if suffix == hash_suffix:
                compromis = True
                nbr_x_compromis = int(count)
                new_data = {
                    "mdp":mdp,
                    "date_verif":date_verif,
                    "compromis":compromis,
                    "nbr_x_compromis":nbr_x_compromis
                }
                historique_df = historique_df._append(new_data, ignore_index=True)
                historique_df.to_csv('./data/logs_mdp.csv', index=False)
                compromis_L.append(compromis)
                compromis_L.append(nbr_x_compromis)
                return compromis_L
        else:
            compromis = False
            nbr_x_compromis = 0
            salt = os.urandom(16)
            mdp = hashlib.sha256(salt + mdp.encode('utf-8')).hexdigest()
            new_data = {
                "mdp":mdp,
                "date_verif":date_verif,
                "compromis":compromis,
                "nbr_x_compromis":nbr_x_compromis
                }
            historique_df = historique_df._append(new_data, ignore_index=True)
            historique_df.to_csv('./data/logs_mdp.csv', index=False)
            compromis_L.append(compromis)
            compromis_L.append(nbr_x_compromis)
            return compromis_L    
        
    else:
        print(f"{RED}Erreur lors de la vérification du mot de passe : {END}{BLUE}{response.status_code}{END}")
        return
    
    
def mdp_connect(mdp):
    
    sha1_hash = hashlib.sha1(mdp.encode('utf-8')).hexdigest().upper()
    
    hash_prefix = sha1_hash[:5]
    hash_suffix = sha1_hash[5:]
    
    url = f"https://api.pwnedpasswords.com/range/{hash_prefix}"
    response = requests.get(url)
    
    if response.status_code == 200:
        hashes = response.text.splitlines()
        for h in hashes:
            suffix, count = h.split(':')
            if suffix == hash_suffix:
                compromis = True
                nombre_fois_compromis = int(count)
                print(f"{JAUNE}\nCe mot de passe a été compromis{END} {RED}{nombre_fois_compromis}{END} {JAUNE}fois !{END}")
                print(f"{JAUNE}Modification conseillée ⚠️!{END}")
                return compromis
    else:
        print(f"{RED}Erreur lors de la vérification du mot de passe : {END}{BLUE}{response.status_code}{END}")
        return

