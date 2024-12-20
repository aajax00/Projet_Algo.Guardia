import hashlib
import requests
import pandas as pd
from datetime import datetime

def mdp_compromis(mdp):
    
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
                print(f"Ce mot de passe a été compromis {nombre_fois_compromis} fois !")
                return compromis
        else:
            compromis = False
            nombre_fois_compromis = 0
            print("Ce mot de passe n'a pas été trouvé dans les violations de données.")
    else:
        print(f"Erreur lors de la vérification du mot de passe : {response.status_code}")
        return

