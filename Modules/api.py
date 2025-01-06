import hashlib
import requests
import pandas as pd
from datetime import datetime

GREEN = "\033[1;32m"
RED = "\033[31m"
BLUE = "\033[94m"
JAUNE = "\033[33m"
END = "\033[0m" 

def mdp_compromis(mdp):
    
    sha1_hash = hashlib.sha1(mdp.encode('utf-8')).hexdigest().upper()
    
    hash_prefix = sha1_hash[:5]
    hash_suffix = sha1_hash[5:]
    
    url = f"https://api.pwnedpasswords.com/range/{hash_prefix}"
    response = requests.get(url)
    compromis_L = []
    
    if response.status_code == 200:
        hashes = response.text.splitlines()
        for h in hashes:
            suffix, count = h.split(':')
            if suffix == hash_suffix:
                compromis = True
                nombre_fois_compromis = int(count)
                compromis_L.append(compromis)
                compromis_L.append(nombre_fois_compromis)
                return compromis_L
        else:
            compromis = False
            nombre_fois_compromis = 0
            compromis_L.append(compromis)
            compromis_L.append(nombre_fois_compromis)
            return compromis_L    
        
    else:
        print(f"{RED}Erreur lors de la vérification du mot de passe : {END}{BLUE}{response.status_code}{END}")
        return
    
    
# def mdp_connect(mdp):
    
#     sha1_hash = hashlib.sha1(mdp.encode('utf-8')).hexdigest().upper()
    
#     hash_prefix = sha1_hash[:5]
#     hash_suffix = sha1_hash[5:]
    
#     url = f"https://api.pwnedpasswords.com/range/{hash_prefix}"
#     response = requests.get(url)
    
#     if response.status_code == 200:
#         hashes = response.text.splitlines()
#         for h in hashes:
#             suffix, count = h.split(':')
#             if suffix == hash_suffix:
#                 compromis = True
#                 nombre_fois_compromis = int(count)
#                 print(f"{JAUNE}votre mot de passe a été compromis{END} {RED}{nombre_fois_compromis}{END} {JAUNE}fois !{END}")
#                 print(f"{JAUNE}Modification conseillé !{END}")
#                 return compromis
#     else:
#         print(f"{RED}Erreur lors de la vérification du mot de passe : {END}{BLUE}{response.status_code}{END}")
#         return

