from Modules.gestion_utilisateur import *
from Modules.gestion_csv_produit import *
from Modules.authentification import *
from Modules.messagecompromis import *
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
            result = login_user(username, mdp)
            instance()
            if is_admin(username, mdp):
                time.sleep(1.5)
                # Animation de chargement avec les symboles
                print(f"{JAUNE}Connections au Panel Administrateur", end="")
                sys.stdout.flush()  # Pour s'assurer que le texte est imprimé immédiatement
                duration = 1.2
                symbols = ['/', '-', '\\', '|']
                start_time = time.time()
                # Boucle d'animation
                while time.time() - start_time < duration:
                    for symbol in symbols:
                        # Afficher "chargement..." avec le symbole actuel
                        sys.stdout.write(f"\rConnections au Panel Administrateur...... {symbol}")
                        sys.stdout.flush()
                        time.sleep(0.1)
                admin_panel(username)
            elif result:
                session(result, username, mdp)
            else:
                print(f"{RED}Échec de la connexion. Veuillez réessayer.{END}")
            
            
        
        
        elif choix == "2":
            create_userfile()
            print(f"\n{GREEN}=== INSCRIPTION ==={END}\n")
            email = input(f"{BLUE}Adresse email: {END}")
            nom = input(f"{BLUE}Nom d'utilisateur: {END}")
            mdp = getpass.getpass(f"{BLUE}Mot de passe: {END}")
            add_users(nom, mdp, email, role="user")
            time.sleep(1.8)
            instance()
            
        else: 
            print(f"{RED}Choix invalide. Réessayez.{END}")
            choix = input(f"{BLUE}CHOISISSEZ UNE OPTION: {END}")

def admin_panel(username):
    instance()
    # if not is_admin(username, mdp):
    #     print(f"{RED}Vous n'êtes pas un administrateur, accès refusé.{END}")
    #     return
    
    while True:
        print(f"\n{RED}====== PANNEAU D'ADMINISTRATION{END} {JAUNE}👤 : [ADMIN]{END}{RED} ====={END}")
        print(f"{GREEN}+--------------------------------------------------+{END}")
        print(f"{GREEN}| 1. [+]Ajouter un utilisateur                     |{END}")
        print(f"{GREEN}| 2. {END}{RED}[-]Supprimer un utilisateur{END}{GREEN}                   |{END}")
        print(f"{GREEN}| 3. Afficher tous les utilisateurs                |{END}")
        print(f"{GREEN}| 4. [=]Rechercher un utilisateur                  |{END}")
        print(f"{GREEN}|{END}{RED}--------------------------------------------------{END}{GREEN}|{END}")
        print(f"{GREEN}| 5. [+]Ajouter un produit pour un utilisateur     |{END}")
        print(f"{GREEN}| 6. {END}{RED}[-]Supprimer un produit pour un utilisateur{END}{GREEN}   |{END}")
        print(f"{GREEN}| 7. [=]Rechercher un Produit                      |{END}")
        print(f"{GREEN}| 8. Afficher les produits d'un utilisateur        |{END}")
        print(f"{GREEN}| 9. Afficher tous les Produits                    |{END}")
        print(f"{GREEN}| 10. Trier les Produits                           |{END}")
        print(f"{GREEN}+--------------------------------------------------+{END}")
        print(f"\nd. {RED}DECONNEXION{END}\n")
        choix = input(f"{BLUE}CHOISISSEZ UNE OPTION: {END}")
        
        if choix == "d":
            print(f"{RED}Déconnexion ...{END}")
            time.sleep(1)
            instance()
            break
        
        # Ajouter un utilisateur
        elif choix == "1":
            print(f"\n{GREEN}=== CREATION D'UTILISATEUR ==={END}\n")
            email =  input(f"{BLUE}Entrez l'email': {END}")
            username = input(f"{BLUE}Entrez le nom d'utilisateur: {END}")
            mdp = getpass.getpass(f"{BLUE}Attribuez un mot de passe: {END}")
            role = input(f"{BLUE}Donnez lui un rôle (admin/user): {END}")
            add_users(username, mdp, email, role)
            time.sleep(1.8)
            instance()
        
        # Supprimer un utilisateur
        elif choix == "2":
            username = input(f"{BLUE}Entrez le nom d'utilisateur à supprimer: {END}")
            supp_user_admin(username)
            
        # Afficher tous les utilisateurs
        elif choix == "3":
            aff_all_user()
            
        # Rechercher un utilisateur
        elif choix == "4":
            username = input(f"{BLUE}Entrez le nom d'utilisateur à chercher: {END}")
            search_user_admin(username)
            
        # Ajouter un produit utilisateur
        elif choix == "5":
            add_produit_admin()
            
        # Supprimer un produit utilisateur
        elif choix == "6":
            supp_produit_admin()
            
        # Rechercher un produit utilisateur  
        elif choix == "7":
            search_produit_admin()
            
        # Afficher les Produits d'un utilisateur spécifique
        elif choix == "8":
            username = input(f"{GREEN}Entrez le nom de l'utilisateur dont vous souhaitez voir les produits: {END}")
            aff_produits_admin(username)
                
        # Afficher tous les produits
        elif choix == "9":
            afficher_tous_les_produits_admin()
            
        # Trier les produits
        elif choix == "10":
            trier_produits_admin()

        else:
            print(f"{RED}Choix invalide.{END}")
            
                
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
            mail_mdp_compromis (user_id)    
            print(f"\n{GREEN}====== SESSION UTILISATEUR {END}{JAUNE}👤 : [{username}]{END}{GREEN} ====={END}")
            print("+--------------------------------------------------+")
            print("| 1. Gérer mes produits                            |")
            print("| 2. Gérer mon compte                              |")
            print("+--------------------------------------------------+")
            print(f"{JAUNE}Votre mot de passe a été compromis {END}{RED}{compromis[1]}{END} {JAUNE}fois!{END}")
            print(f"{JAUNE}Modification conseillée ⚠️ !{END}")
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
        print("| 3. [=]Rechercher un Produit                      |")
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
                print(f"\n{GREEN}=== MES PRODUITS ===:{END}\n")
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
            return menu_principal()
        
            
        
        
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