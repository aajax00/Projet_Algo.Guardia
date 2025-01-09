import tkinter as tk
from tkinter import messagebox
import getpass
import time
import os
import pandas as pnd
from Modules.gestion_utilisateur import *
from Modules.gestion_csv_produit import *
from Modules.authentification import *

# Classe principale de l'application
class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        # Configuration de la fenêtre principale
        self.title("🧮 PROJET ALGORITHMIE - Gestion d'Utilisateurs et Produits")
        self.geometry("800x600")
        self.configure(bg='black')

        self.session_utilisateur = None
        self.current_user = None

        self.create_widgets()
        
        
# Crée les widgets de la fenêtre principale (connexion et inscription)
    def create_widgets(self):
        self.clear_window()
        frame = tk.Frame(self, bg="lightblue")
        frame.pack(padx=20, pady=20, fill="both", expand=True)

        self.header_label = tk.Label(frame, text="====== MENU PRINCIPAL =====", font=("Helvetica", 50), bg="black", fg='white')
        self.header_label.pack(pady=20)

        self.connexion_button = tk.Button(frame, text="Connexion", command=self.open_connexion, width=15, fg="black", font=("Helvetica", 30))
        self.connexion_button.pack(pady=10)

        self.inscription_button = tk.Button(frame, text="Inscription", command=self.open_inscription, width=15, fg="black", font=("Helvetica", 30))
        self.inscription_button.pack(pady=10)

        self.quit_button = tk.Button(frame, text="Quitter", command=self.quit, width=10, fg="black", font=("Helvetica", 15))
        self.quit_button.pack(pady=10)

    def clear_window(self):
        # Efface tous les widgets de la fenêtre actuelle.
        for widget in self.winfo_children():
            widget.destroy()

    def open_connexion(self):
        # Ouvre la fenêtre de connexion.
        self.clear_window()

        self.connexion_label = tk.Label(self, text="=== FORMULAIRE DE CONNEXION ===", font=("Helvetica", 25), bg="black", fg='white')
        self.connexion_label.pack(pady=20)

        self.username_label = tk.Label(self, text="Nom d'utilisateur", fg="white", bg="black")
        self.username_label.pack()
        self.username_entry = tk.Entry(self)
        self.username_entry.pack(pady=5)

        self.password_label = tk.Label(self, text="Mot de passe", fg="white", bg="black")
        self.password_label.pack()
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack(pady=5)

        self.login_button = tk.Button(self, text="Se connecter", command=self.login, width=15, bg="white", fg="black", font=("Helvetica", 15))
        self.login_button.pack(pady=10)

        self.back_button = tk.Button(self, text="Retour", command=self.create_widgets, width=15, bg="white", fg="black", font=("Helvetica", 15))
        self.back_button.pack(pady=10)
        
        self.update_idletasks()

    def login(self):
        # Gère l'authentification des utilisateurs.
        username = self.username_entry.get()
        mdp = self.password_entry.get()

        result = login_user(username, mdp)
        if result:
            # Si l'utilisateur est administrateur
            if is_admin(username, mdp):
                self.admin_panel(username)
            else:
                self.username = username
                self.mdp = mdp
                self.session(result, username, mdp)
        else:
            messagebox.showerror("Erreur", "Nom d'utilisateur ou mot de passe incorrect")

    def open_inscription(self):
        # Ouvre la fenêtre d'inscription.
        self.clear_window()

        self.inscription_label = tk.Label(self, text="=== INSCRIPTION ===", font=("Helvetica", 25), bg="black", fg="white")
        self.inscription_label.pack(pady=20)

        self.email_label = tk.Label(self, text="Adresse email", fg="white", bg="black")
        self.email_label.pack()
        self.email_entry = tk.Entry(self)
        self.email_entry.pack(pady=5)

        self.nom_label = tk.Label(self, text="Nom d'utilisateur", fg="white", bg="black")
        self.nom_label.pack()
        self.nom_entry = tk.Entry(self)
        self.nom_entry.pack(pady=5)

        self.mdp_label = tk.Label(self, text="Mot de passe", fg="white", bg="black")
        self.mdp_label.pack()
        self.mdp_entry = tk.Entry(self, show="*")
        self.mdp_entry.pack(pady=5)

        self.inscription_button = tk.Button(self, text="S'inscrire", command=self.inscription, width=15, bg="white", fg="black", font=("Helvetica", 15))
        self.inscription_button.pack(pady=10)

        self.back_button = tk.Button(self, text="Retour", command=self.create_widgets, width=15, bg="white", fg="black", font=("Helvetica", 15))
        self.back_button.pack(pady=10)
        
        self.update_idletasks()

    def inscription(self):
        # Gère l'inscription des utilisateurs.
        email = self.email_entry.get()
        nom = self.nom_entry.get()
        mdp = self.mdp_entry.get()

        add_users(nom, mdp, email, role="user")
        messagebox.showinfo("Succès", "Inscription réussie !")
        self.create_widgets()

    def admin_panel(self, username):
        # Affiche le panneau d'administration.
        self.clear_window()

        self.admin_label = tk.Label(self, text="=== * PANNEAU D'ADMINISTRATION * ===", font=("Helvetica", 35), bg="black", fg="red")
        self.admin_label.pack(pady=20)

        # Ajoutez ici les boutons pour l'administration (ajouter un utilisateur, supprimer un utilisateur, etc.)
        self.add_user_button = tk.Button(self, text="Ajouter un utilisateur", command=self.add_user_adm, width=15, bg="black", fg="white", font=("Helvetica", 15))
        self.add_user_button.pack(pady=10)

        self.delete_user_button = tk.Button(self, text="Supprimer un utilisateur", command=self.delete_user_adm, width=15, bg="black", fg="white", font=("Helvetica", 15))
        self.delete_user_button.pack(pady=10)

        self.back_button = tk.Button(self, text="Retour", command=self.create_widgets, width=15, bg="black", fg="white", font=("Helvetica", 15))
        self.back_button.pack(pady=10)
        
        self.update_idletasks()

    def add_user_adm(self):
        # ajouter un utilisateur
        # Ajouter ici la logique d'ajout d'un utilisateur
        pass

    def delete_user_adm(self):
        """Logique pour supprimer un utilisateur"""
        # Ajouter ici la logique de suppression d'un utilisateur
        pass

    def session(self, user_id, username, mdp):
        # Gère la session utilisateur
        self.clear_window()

        self.session_label = tk.Label(self, text=f"====== SESSION UTILISATEUR 👤 : [{username}] ======", font=("Helvetica", 25), bg="black", fg="white")
        self.session_label.pack(pady=20)

        self.manage_products_button = tk.Button(self, text="Gérer mes produits", command=self.menu_produit, width=30, bg="white", fg="black", font=("Helvetica", 15))
        self.manage_products_button.pack(pady=10)

        self.manage_account_button = tk.Button(self, text="Gérer mon compte", width=30, bg="white", fg="black", font=("Helvetica", 15))
        # self.manage_account_button = tk.Button(self, text="Gérer mon compte", command=self.manage_account, width=30, bg="white", fg="black", font=("Helvetica", 15))
        self.manage_account_button.pack(pady=10)

        self.logout_button = tk.Button(self, text="Se déconnecter", command=self.logout, width=30, bg="white", fg="black", font=("Helvetica", 15))
        self.logout_button.pack(pady=10)
        

    def menu_produit(self):
    #     """Gère la logique pour gérer les produits."""
    #     # Gérer les produits ici
        self.clear_window()
        self.menu_produit_label = tk.Label(self, text=f"====== GESTION DES PRODUITS 👤 : [{self.username}] ======", font=("Helvetica", 25), bg="black", fg="white")
        self.menu_produit_label.pack(pady=20)
                
        self.add_product_button = tk.Button(self, text="Ajouter un produit", command=self.add_product, width=20, bg="white", fg="black", font=("Helvetica", 15))
        self.add_product_button.pack(pady=10)

        self.edit_product_button = tk.Button(self, text="Modifier un produit", width=20, bg="white", fg="black", font=("Helvetica", 15))
    #     self.edit_product_button = tk.Button(self, text="Modifier un produit", command=self.edit_product, width=20, bg="white", fg="black", font=("Helvetica", 15))
        self.edit_product_button.pack(pady=10)

        self.delete_product_button = tk.Button(self, text="Supprimer un produit", width=20, bg="white", fg="black", font=("Helvetica", 15))
    #     self.delete_product_button = tk.Button(self, text="Supprimer un produit", command=self.delete_product, width=20, bg="white", fg="black", font=("Helvetica", 15))
        self.delete_product_button.pack(pady=10)

        self.back_button = tk.Button(self, text="Retour", command=lambda: self.session(self.username, self.mdp), width=15, bg="white", fg="black", font=("Helvetica", 15))
        self.back_button.pack(pady=10)
        
    #     produits = load_produits()  # Charge les produits depuis le CSV
    #     if produits.empty:
    #         messagebox.showinfo("Info", "Aucun produit trouvé.")
    #         return
        
    #     self.products_listbox = tk.Listbox(self, height=10, width=50, font=("Helvetica", 12))
    #     self.products_listbox.pack(pady=10)
        
    #     for idx, product in produits.iterrows():
    #         self.products_listbox.insert(tk.END, f"{product['nom']} - {product['prix']}€ - {product['quantité']}")




    # def get_all_products():
    # # """Simule la récupération des produits depuis une base de données ou un fichier CSV."""
    # # Exemple statique, vous devrez remplacer par une vraie fonction de récupération
    #     return [
    #         {'id': 1, 'name': 'Produit A', 'price': 15},
    #         {'id': 2, 'name': 'Produit B', 'price': 20},
    #         {'id': 3, 'name': 'Produit C', 'price': 30}
    #     ]



    def add_product(self):
    # """Ouvre un formulaire pour ajouter un produit."""
        self.clear_window()

        self.add_product_label = tk.Label(self, text="=== Nouveau Produit ===", font=("Helvetica", 25), bg="black", fg="white")
        self.add_product_label.pack(pady=20)

        self.namep_label = tk.Label(self, text="Nom du produit", fg="white", bg="black")
        self.namep_label.pack()
        self.namep_entry = tk.Entry(self)
        self.namep_entry.pack(pady=5)

        self.price_label = tk.Label(self, text="Prix du produit (€)", fg="white", bg="black")
        self.price_label.pack()
        self.price_entry = tk.Entry(self)
        self.price_entry.pack(pady=5)
        
        self.quantite_label = tk.Label(self, text="Qauntité", fg="white", bg="black")
        self.quantite_label.pack()
        self.quantite_entry = tk.Entry(self)
        self.quantite_entry.pack(pady=5)

        self.save_button = tk.Button(self, text="Ajouter", command=self.save_product, width=20, bg="white", fg="black", font=("Helvetica", 15))
        # self.save_button = tk.Button(self, text="Enregistrer", command=self.save_product, width=20, bg="white", fg="black", font=("Helvetica", 15))
        self.save_button.pack(pady=10)

        self.back_button = tk.Button(self, text="Retour", command=self.menu_produit, width=20, bg="white", fg="black", font=("Helvetica", 15))
        self.back_button.pack(pady=10)
        
        self.update_idletasks()
        
    
    def save_product(self, user):
        # sauvegarde les produit
        nom = self.namep_entry.get()
        prix = self.price_entry.get()
        quantite = self.quantite_entry.get()
        
        add_produit(nom, prix, quantite)
        



    def manage_account(self):
        """Gère la logique pour gérer le compte utilisateur."""
        # Gérer le compte utilisateur ici
        pass

    def logout(self):
        """Déconnecte l'utilisateur et retourne à la page de connexion."""
        self.session_utilisateur = None
        self.create_widgets()

    def delete_product(self):
        """Supprime un produits"""
        self.clear_window()

        self.delete_product_label = tk.Label(self, text="=== Supprimer un produit ===", font=("Helvetica", 25), bg="black", fg="white")
        self.delete_product_label.pack(pady=20)

        self.produit_label = tk.Label(self, text="Nom du produit à supprimer", bg="black", fg="white")
        self.produit_label.pack()
        self.produit_entry = tk.Entry(self)
        self.produit_entry.pack(pady=5)

        produit = self.produit_entry.get()

        result = supp_produit(produit)

# Lancer l'application
if __name__ == "__main__":
    app = Application()
    app.mainloop()
