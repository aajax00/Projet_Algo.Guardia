from Modules.gestion_utilisateur import *
from Modules.gestion_csv_produit import *
from Modules.authentification import *
import getpass
import time
import os

GREEN = "\033[1;32m"
RED = "\033[31m"
BLUE = "\033[94m"
JAUNE = "\033[33m"
END = "\033[0m" 
art = '''
╔═╗╦═╗╔═╗ ╦╔═╗╔╦╗  ╔═╗╦  ╔═╗╔═╗╦═╗╦╔╦╗╦ ╦╔╦╗╦╔═╗
╠═╝╠╦╝║ ║ ║║╣  ║   ╠═╣║  ║ ╦║ ║╠╦╝║ ║ ╠═╣║║║║║╣ 
╩  ╩╚═╚═╝╚╝╚═╝ ╩   ╩ ╩╩═╝╚═╝╚═╝╩╚═╩ ╩ ╩ ╩╩ ╩╩╚═╝'''

session_utilisateur = None

def instance():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_principal():
    instance()
    print(f"{JAUNE}{art}{END}\n")
    # br_charge()

    while True:
        print(f"\n{GREEN}====== MENU PRINCIPAL ====={END}")
        print("+--------------------------------------------------+")
        print("| 1. CONNEXION                                     |")
        print("| 2. INSCRIPTION                                   |")
        print("+--------------------------------------------------+")
        print(f"\nq. {RED}QUITTER{END}\n")
        choix = input(f"{BLUE}CHOISISSEZ UNE OPTION: {END}")
        
        if choix == "q":
            print(f"{RED}Fermeture du menu..., Au revoir !{END} 👋🏾")
            time.sleep(1)
            break
        
        elif choix == "1":
            print(f"\n{GREEN}=== FORMULAIRE DE CONNEXION ==={END}\n")
            nom = input(f"{BLUE}Nom d'utilisateur: {END}")
            mdp = getpass.getpass(f"{BLUE}Mot de passe: {END}")
            userid = login_user(nom, mdp)
            if userid:
                session(userid, nom)
            
        
        
        elif choix == "2":
            create_userfile()
            nom = input(f"{BLUE}Nom d'utilisateur: {END}")
            mdp = input(f"{BLUE}Mot de passe: {END}")
            add_users(nom, mdp)
            time.sleep(1.8)
            instance()
            
        else: 
            print(f"{RED}Choix invalide. Réessayez.{END}")
            choix = input(f"{BLUE}CHOISISSEZ UNE OPTION: {END}")

            
# -------------------------------------------------------------------    
# def menu_produit():
#     print(f"{JAUNE}{art}{END}\n")
#     create_produit()
#     print("Bienvenue xxx")
    
#     while True:
#         print(f"\n{GREEN}====== GESTION DES PRODUITS ====={END}")
#         print("+--------------------------------------------------+")
#         print("| 1. [+]Ajouter un Produit                         |")
#         print("| 2. [-]Supprimer un Produit                       |")
#         print("| 3. Rechercher un Produit                         |")
#         print("| 4. Afficher tous les Produits                    |")
#         print("| 5. Trier les Produits                            |")
#         print("| s. Sauvegarder les produits                      |")
#         print("+--------------------------------------------------+")
#         print(f"\n{GREEN}====== MENU UTILISATEURS ====={END}")
#         print("+--------------------------------------------------+")
#         print("| 6. [+]Ajouter un utilisateur                     |")
#         print("| 7. [-]Supprimer un utilisateur                   |")
#         print("+--------------------------------------------------+")
#         print(f"\nq. {RED}QUITTER{END}\n")
#         choix = input(f"{BLUE}CHOISISSEZ UNE OPTION: {END}")
        # print(f"\n{GREEN}====== GESTION DES PRODUITS ====={END}")
        # print("+--------------------------------------------------+")
        # print("| 1. [+]Ajouter un Produit                         |")
        # print("| 2. [-]Supprimer un Produit                       |")
        # print("| 3. Rechercher un Produit                         |")
        # print("| 4. Afficher tous les Produits                    |")
        # print("| 5. Trier les Produits                            |")
        # print("| s. Sauvegarder les produits                      |")
        # print("+--------------------------------------------------+")
        # print(f"\n{GREEN}====== MENU UTILISATEURS ====={END}")
        # print("+--------------------------------------------------+")
        # print("| 6. Modifier mes informations                     |")
        # print("| 7. [-]Supprimer mon compte                       |")
        # print("+--------------------------------------------------+")


def session(user_id, nom):
    instance()
    while True:
        print(f"\n{GREEN}====== SESSION UTILISATEUR {END}{JAUNE}👤 : [{nom}]{END}{GREEN} ====={END}")
        print("+--------------------------------------------------+")
        print("| 1. Gérer mes produits                            |")
        print("| 2. Gérer mon compte                              |")
        print("+--------------------------------------------------+")
        print(f"\nd. {RED}DECONNEXION{END}\n")
        choix = input(f"{BLUE}CHOISISSEZ UNE OPTION: {END}")
        
        if choix == "d":
            print(f"{RED}\nDéconnexion de la session...{END} {JAUNE}{nom}{END}")
            time.sleep(2)
            instance()
            break
        
        elif choix == "1":
            menu_produit(user_id, nom)
            
        elif choix == "2":
            menu_user(user_id, nom)
        
        else:
            print(f"{RED}Choix invalide! Réessayez.{END}")


def menu_produit(user_id, nom):
    instance()
    while True:
        print(f"\n{GREEN}====== GESTION DES PRODUITS {END}{JAUNE}👤 : [{nom}]{END}{GREEN} ====={END}")
        print("+--------------------------------------------------+")
        print("| 1. [+]Ajouter un Produit                         |")
        print("| 2. [-]Supprimer un Produit                       |")
        print("| 3. Rechercher un Produit                         |")
        print("| 4. Afficher tous les Produits                    |")
        print("| 5. Trier les Produits                            |")
        print("| s. Sauvegarder les produits                      |")
        print("+--------------------------------------------------+")
        print(f"\nr. {RED}RETOUR{END}\n")
        choix = input(f"{BLUE}CHOISISSEZ UNE OPTION: {END}")
        
        if choix == "r":
            print(f"{RED}Retour à la session...{END}")
            time.sleep(1)
            break
        
        # Ajouter un Produit
        elif choix == "1":
            nom = input(f"{GREEN}Nom du Produit: {END}")
            prix = float(input(f"{GREEN}Prix: {END}"))
            quantité = int(input(f"{GREEN}Quantité: {END}"))
            add_produit(nom, prix, quantité, user_id)
            print(f"{GREEN}Produit ajouté avec succès !{END}")
            time.sleep(1)
            
        # Supprimer un Produit
        elif choix == "2":
            dataf = load_produits()
            mes_produits = dataf[dataf["user_id"] == user_id]
            # dataf_search = search_produit(dataf, nom)
            
            if not mes_produits.empty:
                nom = input(f"{RED}Nom du produit a supprimer: {END}")
                if nom in mes_produits["nom"].values:
                    supp_produit(nom, user_id)
                    print(f"\n{GREEN}Produit supprimé !{END}")  
            # if not dataf_search.empty:
            #     supp_produit(nom, user_id)
            #     print(f"\n{GREEN}Produit supprimé !{END}")
                else:
                    print(f"\n{RED}Produit introuvable !{END}")
            else:
                print("Aucun produit a supprimer")
            

        # Rechercher un Produit  
        elif choix == "3":
            dataf = load_produits()
            nom = input(f"{GREEN}Nom du produit à chercher: {END}")
            produit = search_produit(dataf, nom)
            if not dataf.empty:
                print(f"{GREEN}Produit trouvé : {END}\n{produit}")
            else:
                print(f"{RED}Produit non trouvé.{END}")
            while True:  
                partir = input(f"\nPressez {RED}E{END} pour quitter : ").lower()
                if partir == "e":
                    print(f"{GREEN}Retour au menu principale.{END}")
                time.sleep(1)
                # return menu()
    
    
            # Trier les Produits
        elif choix == "5":
            produits = load_produits()
            key = input(f"{GREEN}Trier par {END}{JAUNE}'prix'{END}{GREEN} ou {END}{BLUE}'quantité': {END}").lower()
            algo = input(f"{BLUE}Algorithme ('bulle' ou 'rapide'): {END}").lower()
            if key in ["prix", "quantité"]:
                if algo in ["bulle", "rapide"]:
                    produits = sort_produit(algo, key)
                    print(f"{produits}")
                    print(f"{GREEN}Produits triés avec succès !\n{END}")
                else:
                    print(f"{RED}Algorithme invalide !{END}")
                    continue 
            else:
                print(f"{RED}Clé de tri invalide !{END}")
                
            while True:  # retour au menu
                partir = input(f"\nAppuyez sur {RED}E{END} pour quitter : ").lower()
                if partir == "e":
                    print(f"{GREEN}Retour au menu principale.{END}\n")
                    time.sleep(1)
                    # return menu()
                
                
        
        # Sauvegarder les produits
        elif choix == "s":
            produits = load_produits()
            save_produit(produits)
            print(f"{GREEN}Données sauvegardeés avec succès.{END}")
            
            while True:  # reoiur au menu
                partir = input(f"\nAppuyez sur {RED}E{END} pour quitter : ").lower()
                if partir == "e":
                    print(f"{GREEN}Retour au menu principale.{END}\n")
                    time.sleep(1)
                    # return menu()

        
        # Afficher les Produits   
        elif choix == "4":
            produits = load_produits()
            mes_produits = produits[produits["nom"] == nom]
            if not mes_produits.empty:
                aff_produits(mes_produits)
            else:
                print(f"{RED}Vous n'avez aucun produit disponible.{END}")

        


def menu_user(user_id, nom):
    instance()
    while True:
        print(f"\n{GREEN}====== MENU UTILISATEURS {END}{JAUNE}👤 : [{nom}]{END}{GREEN} ====={END}")
        print("+--------------------------------------------------+")
        print("| 6. Modifier mes informations                     |")
        print("| 7. [-]Supprimer mon compte                       |")
        print("+--------------------------------------------------+")
        print(f"\nr. {RED}RETOUR{END}\n")
        choix = input(f"{BLUE}CHOISISSEZ UNE OPTION: {END}")
        
        
if __name__ == "__main__":
    menu_principal()