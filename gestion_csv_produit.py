import time
import sys
import pandas as pnds

GREEN = "\033[1;32m"
RED = "\033[31m"
BLUE = "\033[94m"
END = "\033[0m" 

# Ajout de produit au fichier csv
def add_produit(nom, prix, quantité):
    dataf = load_produits()
    dataf = dataf._append({"nom": nom, "prix": prix, "quantité": quantité}, ignore_index=True)
    save_produit(dataf)

        
        
# charger les produit depuis le csv
def load_produits():
    try:
        return pnds.read_csv("Produits.txt")
    except FileNotFoundError:
        return pnds.DataFrame(columns=["nom", "prix", "quantité"])



# supprimer un produit dans csv
def supp_produit(nom):
    dataf = load_produits()
    dataf = dataf[dataf["nom"].str.contains(nom, case=False)]
    save_produit(dataf)


# sauvegarder les produits
def save_produit(dataf):
    dataf.to_csv("Produits.csv", index=False)
            
            
# recherche de produit par nom
def search_produit(produits, nom):
    for produit in produits:
        if produit["nom"].lower() == nom.lower():
            return produit
    return None


# Recherche binaire (après tri des produits par nom)
def binaire(produits, nom):
    produits_trie = sorted(produits, key=lambda x: x["nom"])
    left, right = 0, len(produits_trie) - 1
    while left <= right:
        mid = (left + right) // 2
        if produits_trie[mid]["nom"].lower() == nom.lower():
            return produits_trie[mid]
        elif produits_trie[mid]["nom"].lower() < nom.lower():
            left = mid + 1
        else:
            right = mid - 1
    return None


# tri a bulles
def tri_bulle(produits, key):
    n = len(produits)
    for i in range(n):
        for j in range(0, n - i - 1):
            if produits[j][key] > produits[j + 1][key]:
                produits[j], produits[j + 1] = produits[j + 1], produits[j]
    return produits
            
            
# tri rapide
def tri_rapide(produits, key):
    if len(produits) <= 1:
        return produits
    pivot = produits[0]
    moins = [p for p in produits[1:] if p[key] <= pivot[key]]
    plus = [p for p in produits[1:] if p[key] > pivot[key]]
    return tri_rapide(moins, key) + [pivot] + tri_rapide(plus, key)



# Afficher les Produits
def aff_produits(produits):
    br_charge()
    print(f"\n{GREEN}_____Liste des produits____:{END}\n")
    for p in produits:
        print(f"Nom: {p['nom']}, Prix: {p['prix']}€, Quantité: {p['quantité']}")
        
    while True:  
        partir = input(f"\nPressez {RED}E{END} pour quitter : ").lower()
        if partir == "e":
            print(f"{GREEN}Vous quittez la liste des produits.{END}")
            time.sleep(1)
            return


# barre de chargement
def br_charge():
    for i in range(1, 21):
        sys.stdout.write(f"\rChargement : [{GREEN}{'#' * i}{'.' * (20 - i)}{END}] {GREEN}{i * 5}%{END}")
        sys.stdout.flush()
        time.sleep(0.05)
    print()