import time
import sys

GREEN = "\033[1;32m"
RED = "\033[31m"
BLUE = "\033[94m"
END = "\033[0m" 

# Creation du fichier produit
def create_produit():
    try:
        with open("Produits.txt",'x') as produit:
            pass # si le fichier n'existe pas
    except FileExistsError:
        print(f"{GREEN}Le fichier existe deja.{END}\n{BLUE}Chargement du fichier ... !{END}")
        br_charge()

# Ajout de produit au fichier produit.txt
def add_produit(nom, prix, quantité):
    with open("Produits.txt", 'a') as produit: 
        produit.write(f"{nom},{prix},{quantité}\n")
        
        
# charger les produit depuis le fichier
def load_produits():
    produits = [] # liste vide
    try:
        with open("Produits.txt", 'r') as produit:
            lines = produit.readlines()
            for line in lines:
                try:
                    nom, prix, quantité = line.strip().split(",")
                    produits.append({"nom": nom, "prix": float(prix), "quantité": int(quantité)})
                except ValueError:
                    print(f"{RED}Erreur de format dans la ligne: {line}{END}")
    except FileNotFoundError:
        print(f"{RED}le fichier Produit.txt n'existe pas{END}")
    return produits


# supprimer un produit
def supp_produit(nom):
    produits = load_produits()
    produits = [p for p in produits if p["nom"] != nom]
    save_produit(produits)  


# sauvegarder les produits
def save_produit(produits):
    with open("Produits.txt", 'w') as produit:
        for p in produits:
            produit.write(f"{p['nom']},{p['prix']},{p['quantité']}\n")
            
            
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
    print(f"\n{GREEN}_____LISTE DES PRODUITS____:{END}\n")
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