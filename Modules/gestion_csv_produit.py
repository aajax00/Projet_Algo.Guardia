# from Assets.br_charge import *
import time
import pandas as pnds
import os

GREEN = "\033[1;32m"
RED = "\033[31m"
BLUE = "\033[94m"
END = "\033[0m" 


# creation de produit  
def create_produit():
    file_path = "./data/Produits.csv"
    if not os.path.exists(file_path):
        produit_dataf = pnds.DataFrame(columns=["nom", "prix", "quantité", "user_id"])
        produit_dataf.to_csv(file_path, index=False)
        print(f"{GREEN}Le fichier à eté cree avec succès{END}")
    else:
        print(f"{GREEN}-- Produit.csv --{END}\n{BLUE}Chargement du fichier 💾... !{END}")
        produit_dataf = pnds.read_csv(file_path)
        # br_charge()
        



# Ajout de produit au fichier csv
def add_produit(nom, prix, quantité, user_id):
    dataf = load_produits()
    dataf = dataf._append({"nom": nom, "prix": prix, "quantité": quantité, "user_id":user_id}, ignore_index=True)
    save_produit(dataf)

        
        
# charger les produit depuis le csv
def load_produits():
    try:
        return pnds.read_csv("./data/Produits.csv")
    except FileNotFoundError:
        return pnds.DataFrame(columns=["nom", "prix", "quantité", "user_id"])



# supprimer un produit dans csv
def supp_produit(nom, user_id):
    dataf = load_produits()
    dataf = dataf[dataf["nom"] != nom]
    save_produit(dataf)


# sauvegarder les produits
def save_produit(dataf):
    dataf.to_csv("./data/Produits.csv", index=False)
            
            
# recherche de produit par nom
def search_produit(dataf, nom):
    recherche = dataf[dataf["nom"].str.lower().str.contains(nom, na=False)]
    return recherche



# tri a bulles / rapide csv
def sort_produit(algo, key):
    dataf = load_produits()
    if algo == 'bulle':
        dataf = dataf.sort_values(by=key)
    elif algo == 'rapide':
        dataf = dataf.sort_values(by=key, kind="quicksort")
    save_produit(dataf)
    return dataf




# Afficher les Produits
def aff_produits(produits):
    # br_charge()
    print(f"\n{GREEN}===== MES PRODUITS ====:{END}\n")
    dataf = pnds.DataFrame(produits)
    print(dataf[['nom' ,'prix' ,'quantité', 'user_id']].to_string(index=False))
        
    while True:  
        partir = input(f"\nPressez {RED}E{END} pour quitter : ").lower()
        if partir == "e":
            print(f"{GREEN}Vous quittez la liste des produits.{END}")
            time.sleep(1)
            return
        
        