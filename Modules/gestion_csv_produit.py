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
    dataf = load_produits(user_id)
    new_produit = {"nom": nom, "prix": prix, "quantité": quantité, "user_id":user_id}  
    dataf = dataf._append(new_produit, ignore_index=True)
    save_produit(dataf)

        
        
# charger les produit depuis le csv
def load_produits(user_id):
    try:
        produits = pnds.read_csv("./data/Produits.csv")
        return produits[produits["user_id"] == user_id]
    except FileNotFoundError:
        return pnds.DataFrame(columns=["nom", "prix", "quantité", "user_id"])



# supprimer un produit dans csv
def supp_produit(nom):
    dataf = load_produits()
    dataf = dataf[dataf["nom"] != nom]
    save_produit(dataf)


# sauvegarder les produits
def save_produit(dataf):
    dataf.to_csv("./data/Produits.csv", index=False)
            
            
# recherche de produit par nom
def search_produit(dataf, nom, user_id=None):
    if user_id:
        dataf = dataf[dataf["user_id"] == user_id]
    
    recherche = dataf[dataf["nom"].str.lower().str.contains(nom, na=False)]
    return recherche



# tri a bulles / rapide csv
def sort_produit(algo, key, user_id):
    dataf = load_produits()
    mes_produits = dataf[dataf["user_id"] == user_id]
    if mes_produits.empty:
        print(f"{RED}Vous n'avez aucun produit à trier.{END}")
        return mes_produits
    
    if algo == 'bulle':
        mes_produits = mes_produits.sort_values(by=key)
    elif algo == 'rapide':
        mes_produits = mes_produits.sort_values(by=key, kind="quicksort")
    else:
        print(f"{RED}Algorithme de tri invalide !{END}")
        return mes_produits
    save_produit(dataf)
    return mes_produits
        