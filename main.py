from gestion_produits import *
# from gestion_utilisateur import *
from gestion_csv_produit import *
import time

GREEN = "\033[1;32m"
RED = "\033[31m"
BLUE = "\033[94m"
JAUNE = "\033[33m"
END = "\033[0m" 
art = '''
╔═╗╦═╗╔═╗ ╦╔═╗╔╦╗  ╔═╗╦  ╔═╗╔═╗╦═╗╦╔╦╗╦ ╦╔╦╗╦╔═╗
╠═╝╠╦╝║ ║ ║║╣  ║   ╠═╣║  ║ ╦║ ║╠╦╝║ ║ ╠═╣║║║║║╣ 
╩  ╩╚═╚═╝╚╝╚═╝ ╩   ╩ ╩╩═╝╚═╝╚═╝╩╚═╩ ╩ ╩ ╩╩ ╩╩╚═╝'''

def menu():
    print(f"{JAUNE}{art}{END}\n")
    create_produit()
    
    while True:
        print(f"\n{GREEN}====== MENU PRINCIPALE ====={END}")
        print("+--------------------------------------------------+")
        print("| 1. [+]Ajouter un Produit                         |")
        print("| 2. [-]Supprimer un Produit                       |")
        print("| 3. Rechercher un Produit                         |")
        print("| 4. Afficher tous les Produits                    |")
        print("| 5. Trier les Produits                            |")
        print("| s. Sauvegarder les produits                      |")
        print("+--------------------------------------------------+")
        print(f"\n{GREEN}====== MENU UTILISATEURS ====={END}")
        print("+--------------------------------------------------+")
        print("| 6. [+]Ajouter un utilisateur                     |")
        print("| 7. [-]Supprimer un utilisateur                   |")
        print("+--------------------------------------------------+")
        print(f"\nq. {RED}QUITTER{END}\n")
        choix = input(f"{BLUE}CHOISISSEZ UNE OPTION: {END}")
        
    
    
        
        if choix == "q":
            print(f"{RED}Fermeture du menu..., Au revoir !{END} 👋🏾")
            time.sleep(1)
            break
        
        # Ajouter un Produit
        elif choix == "1":
            nom = input(f"{GREEN}Nom du Produit: {END}")
            prix = float(input(f"{GREEN}Prix: {END}"))
            quantité = int(input(f"{GREEN}Quantité: {END}"))
            add_produit(nom, prix, quantité)
            print(f"{GREEN}Produit ajouté avec succès !{END}")
            time.sleep(1)
            
        # Supprimer un Produit
        elif choix == "2":
            dataf = load_produits()
            nom = input(f"{RED}Nom du produit a supprimer: {END}")
            dataf_search = search_produit(dataf, nom)
            if not dataf_search.empty:
                supp_produit(nom)
                print(f"\n{GREEN}Produit supprimé !{END}")
            else:
                print(f"\n{RED}Produit introuvable !{END}")
        
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
                return menu()
        #########################################################################################
        # elif choix == "3":
        #     dataf = load_produits()
        #     nom = input(f"{GREEN}Nom du produit à chercher: {END}")
        #     print(f"\n{BLUE}s. Recherche Sequentielle\nb. Recherche Binaire{END}")
        #     method = input(f"{BLUE}Choisissez une methode de recherche (s ou b): {END}")
        #     if method == "s":
        #         recherche = search_produit(dataf, nom)
        #         if recherche:
        #             print(f"{GREEN}Produit trouvé : {END}{recherche}")
        #         else:
        #             print(f"{RED}Produit non trouvé.{END}")
        #     elif method == "b":
        #         recherche = binaire(dataf, nom)
        #         if recherche:
        #             print(f"{GREEN}Produit trouvé avec la methode Binaire : \n{END}{recherche}")
        #         else:
        #             print(f"{RED}Produit non trouvé avec la methode Binaire.{END}")
        #     else:
        #         print(f"{RED}Méthode invalide !{END}")
        #     while True:  # reoiur au menu
        #         partir = input(f"\nAppuyez sur {RED}E{END} pour quitter : ").lower()
        #         if partir == "e":
        #             print(f"{GREEN}Retour au menu principale.{END}\n")
        #             time.sleep(1)
        #             return menu()
                
        # Afficher les Produits   
        elif choix == "4":
            produits = load_produits()
            if not produits.empty:
                aff_produits(produits)
            else:
                print(f"{RED}Aucun produit disponible.{END}")
                
                                
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
                    return menu()
                
                
        
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
                    return menu()
            
        # ajouter utilisateur
        elif choix == "6":
            nom = input(f"{GREEN}Nom de l'utilisateur: {END}")
            mdp = input(f"{GREEN}Mot de passe: {END}")
            add_users(nom, mdp)
            print(f"{GREEN}Utilisateur ajouté avec succès !{END}")
            
        # ajouter utilisateur
        elif choix == "7":
            nom = input(f"{GREEN}Nom de l'utilisateur à supprimé: {END}")
            supp_users(nom)
            print(f"{GREEN}Utilisateur supprimé avec succès !{END}")
        
        else:
            print(f"{RED}Choix invalide. Réessayez.{END}")
            
if __name__ == "__main__":
    menu()
