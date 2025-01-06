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
            username = input(f"{BLUE}Nom d'utilisateur: {END}")
            mdp = getpass.getpass(f"{BLUE}Mot de passe: {END}")
            userid = login_user(username, mdp)
            instance()
            if userid:
                session(userid, username, mdp)
            
        
        
        elif choix == "2":
            create_userfile()
            nom = input(f"{BLUE}Nom d'utilisateur: {END}")
            mdp = getpass.getpass(f"{BLUE}Mot de passe: {END}")
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


def session(user_id, username, mdp):
    instance()
    compromis = mdp_compromis(mdp)
    
    while True:
        if compromis[0] == True :    
            print(f"\n{GREEN}====== SESSION UTILISATEUR {END}{JAUNE}👤 : [{username}]{END}{GREEN} ====={END}")
            print("+--------------------------------------------------+")
            print("| 1. Gérer mes produits                            |")
            print("| 2. Gérer mon compte                              |")
            print("+--------------------------------------------------+")
            print(f"{JAUNE}Votre mot de passe a été compromis {END}{RED}{compromis[1]}{END} {JAUNE}fois!{END}")
            print(f"{JAUNE}Modification conseillez !{END}")
            print(f"\nd. {RED}DECONNEXION{END}\n")
        else:
            print(f"\n{GREEN}====== SESSION UTILISATEUR {END}{JAUNE}👤 : [{username}]{END}{GREEN} ====={END}")
            print("+--------------------------------------------------+")
            print("| 1. Gérer mes produits                            |")
            print("| 2. Gérer mon compte                              |")
            print("+--------------------------------------------------+")
            print(f"\nd. {RED}DECONNEXION{END}\n")
            
        choix = input(f"{BLUE}CHOISISSEZ UNE OPTION: {END}")
        
        if choix == "d":
            print(f"{RED}\nDéconnexion de la session...{END} {JAUNE}{username}{END}")
            time.sleep(2)
            instance()
            break
        
        elif choix == "1":
            menu_produit(user_id, username)
            
        elif choix == "2":
            menu_user(user_id, username)
        
        else:
            print(f"{RED}Choix invalide! Réessayez.{END}")
            



def menu_produit(user_id, username):
    instance()
    while True:
        print(f"\n{GREEN}====== GESTION DES PRODUITS {END}{JAUNE}👤 : [{username}]{END}{GREEN} ====={END}")
        print("+--------------------------------------------------+")
        print("| 1. [+]Ajouter un Produit                         |")
        print(f"| 2. {RED}[-]Supprimer un Produit{END}                       |")
        print("| 3. Rechercher un Produit                         |")
        print("| 4. Afficher tous les Produits                    |")
        print("| 5. Trier les Produits                            |")
        print("| s. Sauvegarder les produits                      |")
        print("+--------------------------------------------------+")
        print(f"\nr. {RED}RETOUR{END}\n")
        choix = input(f"{BLUE}CHOISISSEZ UNE OPTION: {END}")
        
        if choix == "r":
            print(f"{RED}Retour au menu de session...{END}")
            time.sleep(1)
            instance()
            break
        
        # Ajouter un Produit
        elif choix == "1":
            nom = input(f"{GREEN}Nom du Produit: {END}")
            prix = float(input(f"{GREEN}Prix: {END}"))
            quantité = int(input(f"{GREEN}Quantité: {END}"))
            add_produit(nom, prix, quantité, user_id)
            print(f"{GREEN}Produit ajouté avec succès !{END}")
            time.sleep(1.5)
            instance()
            
        # Supprimer un Produit
        elif choix == "2":
            dataf = load_produits()
            mes_produits = dataf[dataf["user_id"] == user_id]
            # dataf_search = search_produit(dataf, nom)
            
            if not mes_produits.empty:
                nom_produit = input(f"{RED}Nom du produit a supprimer: {END}")
                if nom_produit in mes_produits["nom"].values:
                    supp_produit(nom_produit, user_id)
                    print(f"\n{GREEN}Produit supprimé !{END}")
                    time.sleep(1.5)
                    instance()
            # if not dataf_search.empty:
            #     supp_produit(nom, user_id)
            #     print(f"\n{GREEN}Produit supprimé !{END}")
                else:
                    print(f"\n{RED}Produit introuvable !{END}")
                    time.sleep(1.5)
                    instance()
            else:
                print(f"{JAUNE}\nAucun produit a supprimer{END}")
                time.sleep(1.5)
                instance()
            

        # Rechercher un Produit  
        elif choix == "3":
            dataf = load_produits()
            nom = input(f"{GREEN}Nom du produit à chercher: {END}")
            produit = search_produit(dataf, nom, user_id)
            if not produit.empty:
                produit_aff = produit.drop(columns=["user_id"])
                print(f"{GREEN}Produit trouvé : {END}\n{produit_aff}")
            else:
                print(f"{RED}Produit non trouvé.{END}")
            while True:  
                partir = input(f"\nPressez {RED}E{END} pour quitter : ").lower()
                if partir == "e":
                    print(f"{GREEN}Retour au menu principale.{END}")
                time.sleep(1)
                instance()
                return menu_produit(user_id, username)
            
            
        # Afficher les Produits   
        elif choix == "4":
            produits = load_produits()
            mes_produits = produits[produits["user_id"] == user_id]
            if not mes_produits.empty:
                print(f"\n{GREEN}===== MES PRODUITS ====:{END}\n")
                print(mes_produits[['nom' ,'prix' ,'quantité']].to_string(index=False))
            else:
                print(f"{RED}Vous n'avez aucun produit disponible.{END}")
                
            while True:  
                quitter = input(f"\nPressez {RED}E{END} pour quitter : ").lower()
                if quitter == "e":
                    print(f"{GREEN}Vous quittez la liste des produits.{END}")
                    time.sleep(1)
                    instance()
                    return menu_produit(user_id, username)
                
    
    
            # Trier les Produits
        elif choix == "5":
            produits = load_produits()
            key = input(f"{GREEN}Trier par {END}{JAUNE}'prix'{END}{GREEN} ou {END}{BLUE}'quantité': {END}").lower()
            algo = input(f"{BLUE}Algorithme ('bulle' ou 'rapide'): {END}").lower()
            if key in ["prix"]:
                if algo in ["bulle", "rapide"]:
                    mes_produits = sort_produit(algo, key, user_id)
                    print(mes_produits[['nom' ,'prix' ,'quantité']].to_string(index=False))
                    print(f"{GREEN}Produits triés par PRIX avec succès !\n{END}")
                else:
                    print(f"{RED}Algorithme invalide !{END}")
                    continue 
                
            if key in ["quantité"]:
                if algo in ["bulle", "rapide"]:
                    mes_produits = sort_produit(algo, key, user_id)
                    print(mes_produits[['nom' ,'prix' ,'quantité']].to_string(index=False))
                    print(f"{GREEN}Produits triés par QUANTITE avec succès !\n{END}")
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
                    instance()
                    return menu_produit(user_id, username)
                
                
        
        # Sauvegarder les produits
        elif choix == "s":
            produits = load_produits()
            save_produit(produits)
            print(f"{GREEN}Données sauvegardeés avec succès.{END}")
            
            while True:  # reoiur au menu
                partir = input(f"\nAppuyez sur {RED}E{END} pour quitter : ").lower()
                if partir == "e":
                    print(f"{GREEN}Retour au menu de gestion des produits.{END}\n")
                    time.sleep(1)
                    instance()
                    return menu_produit(user_id, username)

                
        else: 
            print(f"{RED}Choix invalide. Réessayez.{END}")
            choix = input(f"{BLUE}CHOISISSEZ UNE OPTION: {END}")

        


def menu_user(user_id, username):
    instance()
    while True:
        print(f"\n{GREEN}====== MENU UTILISATEURS {END}{JAUNE}👤 : [{username}]{END}{GREEN} ====={END}")
        print("+--------------------------------------------------+")
        print("| 1. Modifier mes informations                     |")
        print(f"| 2. {RED}[-]Supprimer mon compte{END}                       |")
        print("+--------------------------------------------------+")
        print(f"\nr. {RED}RETOUR{END}\n")
        choix = input(f"{BLUE}CHOISISSEZ UNE OPTION: {END}")
        
        if choix == "r":
            print(f"{RED}Retour au menu de session...{END}")
            time.sleep(1)
            instance()
            break
        
        elif choix == "1":
            print(f"{GREEN}=== MODIFIER MES INFORMATIONS ==={END}")
            mdp_actuel = getpass.getpass(f"{BLUE}Entrez votre mot de passe actuel: {END}")
            username = modif_info_user(username, mdp_actuel)
            break
        
            
        
        
        elif choix == "2":
            print(f"{RED}=== SUPPRIMER MON COMPTE ==={END}")
            confirm_uname = input(f"{GREEN}Confirmez votre nom d'utilisateur: {END}")
            mdp = getpass.getpass(f"{GREEN}Confirmez votre mot de passe: {END}")
            if confirm_uname == username:
                supp_produit_user(user_id)
                supp_users(username, mdp)
                print(f"{RED}\nSuppression du compte...{END} {JAUNE}{username}{END}")
                time.sleep(1.5)
                print(f"{GREEN}Votre compte a été supprimé avec succès. Déconnexion...{END}")
                time.sleep(2)
            else:
                print(f"{RED}Nom d'utilisateur incorrect.{END}")
            return menu_principal()
        
        
        
        
if __name__ == "__main__":
    menu_principal()