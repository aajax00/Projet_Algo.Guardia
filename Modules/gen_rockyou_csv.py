import hashlib
import pandas as pnd

def hash_pswd(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def gen_rockyou_csv(input_file="../data/rockyou.txt", output_file="../data/rockyou.csv"):
    try:
        # Charger les mots de passe depuis le fichier texte
        with open(input_file, "r", encoding="utf-8", errors="ignore") as file:
            passwords = [line.strip() for line in file.readlines()]
        
        # Créer un DataFrame avec les mots de passe en clair
        data = pnd.DataFrame(passwords, columns=["mot_de_passe"])

        # Ajouter une colonne avec les mots de passe hashés
        data["mot_de_passe_hash"] = data["mot_de_passe"].apply(hash_pswd)

        # Sauvegarder le fichier CSV
        data.to_csv(output_file, index=False, encoding="utf-8")
        print(f"Fichier CSV généré avec succès : {output_file}")

    except FileNotFoundError:
        print(f"Erreur : Le fichier {input_file} est introuvable.")

# Générer le fichier CSV
gen_rockyou_csv()