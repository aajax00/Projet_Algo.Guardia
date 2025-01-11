import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import getpass
import time
import os
import pandas as pnd
from Modules.gestion_utilisateur import *
from Modules.gestion_csv_produit import *
from Modules.authentification import *
from gui_modules import *
from Modules.messagecompromis import *



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
        frame = tk.Frame(self, bg="#1E1E1E")
        frame.pack(padx=20, pady=20, fill="both", expand=True)

        self.header_label = tk.Label(frame, text=" MENU PRINCIPAL ", font=("Helvetica", 50), bg="black", fg='#39FF14')
        self.header_label.pack(pady=20)

        self.connexion_button = tk.Button(frame, text="Connexion", command=self.open_connexion, width=15, fg='#014421', font=("Helvetica", 30))
        self.connexion_button.pack(pady=10)

        self.inscription_button = tk.Button(frame, text="Inscription", command=self.open_inscription, width=15, fg='#014421', font=("Helvetica", 30))
        self.inscription_button.pack(pady=10)

        self.quit_button = tk.Button(frame, text="Quitter", command=self.quit, width=10, fg="#FF0000", font=("Helvetica", 15))
        self.quit_button.pack(pady=10)

    def clear_window(self):
        # Efface tous les widgets de la fenêtre actuelle.
        for widget in self.winfo_children():
            widget.destroy()

    def open_connexion(self):
        # Ouvre la fenêtre de connexion.
        self.clear_window()
        frame = tk.Frame(self, bg="#1E1E1E")
        frame.pack(padx=20, pady=20, fill="both", expand=True)

        self.connexion_label = tk.Label(frame, text=" FORMULAIRE DE CONNEXION ", font=("Helvetica", 25), bg="black", fg='#39FF14')
        self.connexion_label.pack(pady=20)

        self.username_label = tk.Label(frame, text="Nom d'utilisateur", fg='white', bg="#1E1E1E")
        self.username_label.pack()
        self.username_entry = tk.Entry(frame)
        self.username_entry.pack(pady=5)

        self.password_label = tk.Label(frame, text="Mot de passe", fg='white', bg="#1E1E1E")
        self.password_label.pack()
        self.password_entry = tk.Entry(frame, show="*")
        self.password_entry.pack(pady=5)

        self.login_button = tk.Button(frame, text="Se connecter", command=self.login, width=15, bg="white", fg='#014421', font=("Helvetica", 20))
        self.login_button.pack(pady=10)

        self.back_button = tk.Button(frame, text="Retour", command=self.create_widgets, width=10, fg="#FF0000", font=("Helvetica", 15))
        self.back_button.pack(pady=10)
        
        self.update_idletasks()

    def login(self):
        # Gère l'authentification des utilisateurs.
        username = self.username_entry.get()
        mdp = self.password_entry.get()

        result = login_user(username, mdp)
        if result:
            self.user_id = result
            self.username = username
            self.mdp = mdp
            # Si l'utilisateur est administrateur
            if is_admin(username, mdp):
                self.admin_panel(username)
            else:
                self.session(result, username, mdp)
        else:
            messagebox.showerror("Erreur", "Nom d'utilisateur ou mot de passe incorrect")

    def open_inscription(self):
        # Ouvre la fenêtre d'inscription.
        self.clear_window()
        frame = tk.Frame(self, bg="#1E1E1E")
        frame.pack(padx=20, pady=20, fill="both", expand=True)

        self.inscription_label = tk.Label(frame, text=" INSCRIPTION ", font=("Helvetica", 25), bg="black", fg="#39FF14")
        self.inscription_label.pack(pady=20)

        self.email_label = tk.Label(frame, text="Adresse email", fg="white", bg="#1E1E1E")
        self.email_label.pack()
        self.email_entry = tk.Entry(frame)
        self.email_entry.pack(pady=5)

        self.nom_label = tk.Label(frame, text="Nom d'utilisateur", fg="white", bg="#1E1E1E")
        self.nom_label.pack()
        self.nom_entry = tk.Entry(frame)
        self.nom_entry.pack(pady=5)

        self.mdp_label = tk.Label(frame, text="Mot de passe", fg="white", bg="#1E1E1E")
        self.mdp_label.pack()
        self.mdp_entry = tk.Entry(frame, show="*")
        self.mdp_entry.pack(pady=5)

        self.inscription_button = tk.Button(frame, text="S'inscrire", command=self.inscription, width=15, bg="white", fg='#014421', font=("Helvetica", 20))
        self.inscription_button.pack(pady=10)

        self.back_button = tk.Button(frame, text="Retour", command=self.create_widgets, width=10, bg="white", fg="#FF0000", font=("Helvetica", 15))
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
        frame = tk.Frame(self, bg="#1E1E1E")
        frame.pack(padx=20, pady=20, fill="both", expand=True)

        self.admin_label = tk.Label(frame, text=" * PANNEAU D'ADMINISTRATION | 👤: [ADMIN] * ", font=("Helvetica", 25), bg="black", fg="#FF0000")
        self.admin_label.pack(pady=20)

        self.gestion_user_button = tk.Button(frame, text="Gestion des utilisateurs", command=self.gestion_user, width=20, bg="black", fg='#014421', font=("Helvetica", 30))
        self.gestion_user_button.pack(pady=10)

        self.gestion_produit_button = tk.Button(frame, text="Gestion des produits", width=20, bg="black", fg='#014421', font=("Helvetica", 30))
        self.gestion_produit_button.pack(pady=10)

        self.back_button = tk.Button(frame, text="Déconnexion", command=self.logout, width=10, bg="black", fg="#FF0000", font=("Helvetica", 15))
        self.back_button.pack(pady=10)
        
        self.update_idletasks()
        
    def gestion_user(self):
        self.clear_window()
        frame = tk.Frame(self, bg="#1E1E1E")
        frame.pack(padx=20, pady=20, fill="both", expand=True)

        self.admin_label = tk.Label(frame, text=" * PANNEAU D'ADMINISTRATION | 👤: [ADMIN] * ", font=("Helvetica", 25), bg="black", fg="#FF0000")
        self.admin_label.pack(pady=20)

        # Ajoutez ici les boutons pour l'administration (ajouter un utilisateur, supprimer un utilisateur, etc.)
        self.add_user_button = tk.Button(frame, text="[+]Ajouter un utilisateur", command=self.add_user_admin, width=15, bg="black", fg='#014421', font=("Helvetica", 15))
        self.add_user_button.pack(pady=10)

        self.delete_user_button = tk.Button(frame, text="[-]Supprimer un utilisateur", command=self.delete_user_adm, width=15, bg="black", fg='#014421', font=("Helvetica", 15))
        self.delete_user_button.pack(pady=10)

        self.back_button = tk.Button(frame, text="Retour", command=self.admin_panel, width=10, bg="black", fg="#FF0000", font=("Helvetica", 20))
        self.back_button.pack(pady=10)
        
        self.update_idletasks()

    def add_user_admin(self):
        # ajouter un utilisateur
        # Ajouter ici la logique d'ajout d'un utilisateur
        self.clear_window()
        frame = tk.Frame(self, bg="#1E1E1E")
        frame.pack(padx=20, pady=20, fill="both", expand=True)

        self.inscription_label = tk.Label(frame, text=" [+]Ajouter un utilisateur ", font=("Helvetica", 25), bg="black", fg="#39FF14")
        self.inscription_label.pack(pady=20)

        self.admin_email_label = tk.Label(frame, text="Adresse email", fg="white", bg="#1E1E1E")
        self.admin_email_label.pack()
        self.admin_email_entry = tk.Entry(frame)
        self.admin_email_entry.pack(pady=5)

        self.admin_nom_label = tk.Label(frame, text="Nom d'utilisateur", fg="white", bg="#1E1E1E")
        self.admin_nom_label.pack()
        self.admin_nom_entry = tk.Entry(frame)
        self.admin_nom_entry.pack(pady=5)
        
        self.role = tk.Label(frame, text="Rôle (admin/user)", fg="white", bg="#1E1E1E")
        self.role.pack()
        self.role = tk.Entry(frame)
        self.role.pack(pady=5)

        self.admin_mdp_label = tk.Label(frame, text="Mot de passe", fg="white", bg="#1E1E1E")
        self.admin_mdp_label.pack()
        self.admin_mdp_entry = tk.Entry(frame, show="*")
        self.admin_mdp_entry.pack(pady=5)

        self.inscription_button = tk.Button(frame, text="Ajouter", command=self.admin_user, width=15, bg="white", fg='#014421', font=("Helvetica", 20))
        self.inscription_button.pack(pady=10)

        self.back_button = tk.Button(frame, text="Retour", command=self.create_widgets, width=10, bg="white", fg="#FF0000", font=("Helvetica", 15))
        self.back_button.pack(pady=10)
        
        self.update_idletasks()
        
    def admin_user(self):
        email = self.admin_email_entry.get()
        username = self.admin_nom_entry.get()
        mdp = self.admin_mdp_entry.get()
        role = self.role.get()
        
        add_users(username, mdp, email, role)
        messagebox.showinfo("Succès", "Utilisateur ajouté avec succès !")
        self.create_widgets()

    def delete_user_adm(self):
        """Logique pour supprimer un utilisateur"""
        # Ajouter ici la logique de suppression d'un utilisateur
        pass

    def session(self, user_id, username, mdp):
        # Gère la session utilisateur
        self.clear_window()
        self.check_password_compromise(username, mdp)
        
        frame = tk.Frame(self, bg="#1E1E1E")
        frame.pack(padx=20, pady=20, fill="both", expand=True)
        
        self.current_user = {"user_id": user_id, "username": username, "mdp": mdp}

        self.session_label = tk.Label(frame, text=f" SESSION UTILISATEUR - 👤: [{self.username}] ", font=("Helvetica", 25), bg="black", fg="#39FF14")
        self.session_label.pack(pady=20)

        self.manage_products_button = tk.Button(frame, text="Gérer mes produits", command=self.menu_produit, width=15, bg="white", fg='#014421', font=("Helvetica", 30))
        self.manage_products_button.pack(pady=10)

        self.manage_account_button = tk.Button(frame, text="Gérer mon compte", command=self.manage_account, width=15, bg="white", fg='#014421', font=("Helvetica", 30))
        # self.manage_account_button = tk.Button(self, text="Gérer mon compte", command=self.manage_account, width=30, bg="white", fg="black", font=("Helvetica", 15))
        self.manage_account_button.pack(pady=10)

        self.logout_button = tk.Button(frame, text="Se déconnecter", command=self.logout, width=10, bg="white", fg="#FF0000", font=("Helvetica", 20))
        self.logout_button.pack(pady=10)

    
        

    def menu_produit(self):
    #     """Gère la logique pour gérer les produits."""
    #     # Gérer les produits ici
        self.clear_window()
        frame = tk.Frame(self, bg="#1E1E1E")
        frame.pack(padx=20, pady=20, fill="both", expand=True)
        
        
        self.menu_produit_label = tk.Label(frame, text=f" GESTION DES PRODUITS - 👤: [{self.username}] ", font=("Helvetica", 25), bg="black", fg="#39FF14")
        self.menu_produit_label.pack(pady=20)
                
        self.add_product_button = tk.Button(frame, text="[+]Ajouter un produit", command=self.add_product, width=20, bg="white", fg='#014421', font=("Helvetica", 15))
        self.add_product_button.pack(pady=10)

        # self.delete_product_button = tk.Button(self, text="Supprimer un produit", width=20, bg="white", fg="black", font=("Helvetica", 15))
        self.delete_product_button = tk.Button(frame, text="[-]Supprimer un produit", command=self.delete_product, width=20, bg="white", fg='#014421', font=("Helvetica", 15))
        self.delete_product_button.pack(pady=10)
        
        # self.products_listbox = tk.Listbox(self, height=18, width=80, font=("Helvetica", 12))
        # self.products_listbox.pack(pady=10)
        
        self.products_tree = ttk.Treeview(frame, columns=("Nom", "Prix (€)", "Quantité"), show="headings", height=15)       
        # Configurer les en-têtes sans utiliser de style directement
        self.products_tree.heading("Nom", text="Nom")
        self.products_tree.heading("Prix (€)", text="Prix (€)")
        self.products_tree.heading("Quantité", text="Quantité")

        # Configurer les en-têtes pour qu'ils soient cliquables et triables
        self.products_tree.heading("Nom", text="Nom", command=lambda: self.sort_products("nom"))
        self.products_tree.heading("Prix (€)", text="Prix (€)", command=lambda: self.sort_products("prix"))
        self.products_tree.heading("Quantité", text="Quantité", command=lambda: self.sort_products("quantité"))

        
        # Création du Treeview pour afficher les produits
        self.products_tree.column("Nom", anchor=tk.W, width=200)
        self.products_tree.column("Prix (€)", anchor=tk.CENTER, width=100)
        self.products_tree.column("Quantité", anchor=tk.CENTER, width=100)
        self.products_tree.pack(pady=10)
        
        self.back_button = tk.Button(frame, text="Retour", command=lambda: self.session(self.user_id, self.username, self.mdp), width=10, bg="white", fg="#FF0000", font=("Helvetica", 20))
        self.back_button.pack(pady=10)

        
        produits = self.load_produits(user_id=self.current_user.get("user_id"))  # Charge les produits depuis le CSV
        # produits_user = produits[produits["user_id"] == self.user_id]
        
        if produits is None:
            self.products_tree.insert("", "end", values=("Aucun produit trouvé.", "", ""))
            return
        else:
            for index, product in produits.iterrows():
                self.products_tree.insert("", "end", values=(product['nom'], product['prix'], product['quantité']))
        
        self.update_idletasks()   
        
    def load_produits(self, user_id=None):
        try:
            produits = pnds.read_csv("./data/Produits.csv")
            if user_id is not None:
                return produits[produits["user_id"] == user_id]
        except FileNotFoundError:
            return pnds.DataFrame(columns=["nom", "prix", "quantité", "user_id"])



    def sort_products(self, key):
        # Variable pour mémoriser l'ordre de tri (ascendant ou descendant)
        if not hasattr(self, 'sort_order'):
            self.sort_order = {"nom": False, "prix": False, "quantité": False}
            
        # Alterner l'ordre de tri
        self.sort_order[key] = not self.sort_order[key]
        
        produits = self.load_produits(user_id=self.current_user.get("user_id"))
        
        if key == "nom":
            produits = produits.sort_values(by="nom", ascending=self.sort_order[key])
        elif key == "prix":
            produits = produits.sort_values(by="prix", ascending=self.sort_order[key])
        elif key == "quantité":
            produits = produits.sort_values(by="quantité", ascending=self.sort_order[key])
            
        for item in self.products_tree.get_children():
            self.products_tree.delete(item)
        
        for index, product in produits.iterrows():
            self.products_tree.insert("", "end", values=(product['nom'], product['prix'], product['quantité']))
            
        self.update_header_with_arrows(key)

        self.update_idletasks()
        
    def update_header_with_arrows(self, sorted_column):
    # Enlever les flèches existantes et les réinitialiser
        for col in ["Nom", "Prix (€)", "Quantité"]:
            text = col
            self.products_tree.heading(col, text=text)

    # Ajouter la flèche à la colonne triée
        if self.sort_order[sorted_column]:
            arrow = "⬇"  # Flèche croissante
        else:
            arrow = "⬆"  # Flèche descroissante

    # Mettre à jour l'en-tête avec la flèche
        if sorted_column == "nom":
            self.products_tree.heading("Nom", text=f"Nom {arrow}")
        elif sorted_column == "prix":
            self.products_tree.heading("Prix (€)", text=f"Prix (€) {arrow}")
        elif sorted_column == "quantité":
            self.products_tree.heading("Quantité", text=f"Quantité {arrow}")
        

    def add_product(self):
    # """Ouvre un formulaire pour ajouter un produit."""
        self.clear_window()
        frame = tk.Frame(self, bg="#1E1E1E")
        frame.pack(padx=20, pady=20, fill="both", expand=True)

        self.add_product_label = tk.Label(frame, text=" [+]NOUVEAU PRODUIT ", font=("Helvetica", 25), bg="black", fg="#39FF14")
        self.add_product_label.pack(pady=20)

        self.namep_label = tk.Label(frame, text="Nom du produit", fg="white", bg="#1E1E1E")
        self.namep_label.pack()
        self.namep_entry = tk.Entry(frame)
        self.namep_entry.pack(pady=5)

        self.price_label = tk.Label(frame, text="Prix du produit (€)", fg="white", bg="#1E1E1E")
        self.price_label.pack()
        self.price_entry = tk.Entry(frame)
        self.price_entry.pack(pady=5)
        
        self.quantite_label = tk.Label(frame, text="Qauntité", fg="white", bg="#1E1E1E")
        self.quantite_label.pack()
        self.quantite_entry = tk.Entry(frame)
        self.quantite_entry.pack(pady=5)

        self.save_button = tk.Button(frame, text="Ajouter le produit", command=self.save_product, width=15, bg="white", fg="#014421", font=("Helvetica", 15))
        self.save_button.pack(pady=10)

        self.back_button = tk.Button(frame, text="Retour", command=self.menu_produit, width=10, bg="white", fg="#FF0000", font=("Helvetica", 20))
        self.back_button.pack(pady=10)
        
        self.update_idletasks()
        
    
    def save_product(self):
        # sauvegarde les produit
        nom = self.namep_entry.get()
        prix = self.price_entry.get()
        quantite = self.quantite_entry.get()
        
        if not nom or not prix or not quantite:
            messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")
            return
        
        try:
            prix = float(prix)  # Convertit le prix en float
            quantite = int(quantite)  # Convertit la quantité en entier
        except ValueError:
            messagebox.showerror("Erreur", "Prix ou quantité invalide.")
            return
        
        add_produit(nom, prix, quantite, user_id=self.user_id)
        messagebox.showinfo("Succès", "Produit ajouté avec succès !")
        



    def manage_account(self):
        """Gère la logique pour gérer le compte utilisateur."""
        # Gérer le compte utilisateur ici 
        self.clear_window()
        frame = tk.Frame(self, bg="#1E1E1E")
        frame.pack(padx=20, pady=20, fill="both", expand=True)
        

        self.manage_account_label = tk.Label(frame, text=f" MENU UTILISATEURS - 👤: [{self.username}] ", font=("Helvetica", 25), bg="black", fg="#39FF14")
        self.manage_account_label.pack(pady=20)

        # # Ajoutez ici les boutons pour l'administration (ajouter un utilisateur, supprimer un utilisateur, etc.)
        self.edit_account_button = tk.Button(frame, text="Modifier mes informations", command=self.open_modify_user, width=20, bg="black", fg='#014421', font=("Helvetica", 25))
        self.edit_account_button.pack(pady=10)

        self.delete_account_button = tk.Button(frame, text="[-]Supprimer mon compte", command=self.open_delete_user, width=20, bg="black", fg='#014421', font=("Helvetica", 25))
        self.delete_account_button.pack(pady=10)

        self.back_button = tk.Button(frame, text="Retour", command=lambda: self.session(self.user_id, self.username, self.mdp), width=10, bg="black", fg="#FF0000", font=("Helvetica", 20))
        self.back_button.pack(pady=10)
        
        self.update_idletasks()

    def open_modify_user(self):
        self.clear_window()
        frame = tk.Frame(self, bg="#1E1E1E")
        frame.pack(padx=20, pady=20, fill="both", expand=True)

        header_label = tk.Label(frame, text=" Modifier mes Infos ", font=("Helvetica", 25), bg="black", fg="#39FF14")
        header_label.pack(pady=20)

        username_label = tk.Label(frame, text="Nom d'utilisateur", fg="white", bg="#1E1E1E")
        username_label.pack()
        self.username_entry = tk.Entry(frame)
        self.username_entry.pack(pady=5)

        email_label = tk.Label(frame, text="Nouvelle adresse email", fg="white", bg="#1E1E1E")
        email_label.pack()
        self.email_entry = tk.Entry(frame)
        self.email_entry.pack(pady=5)

        new_username_label = tk.Label(frame, text="Nouveau nom d'utilisateur", fg="white", bg="#1E1E1E")
        new_username_label.pack()
        self.new_username_entry = tk.Entry(frame)
        self.new_username_entry.pack(pady=5)
        
        current_password_label = tk.Label(frame, text="Mot de passe actuel", fg="white", bg="#1E1E1E")
        current_password_label.pack()
        self.current_password_entry = tk.Entry(frame, show="*")
        self.current_password_entry.pack(pady=5)

        new_password_label = tk.Label(frame, text="Nouveau mot de passe", fg="white", bg="#1E1E1E")
        new_password_label.pack()
        self.new_password_entry = tk.Entry(frame, show="*")
        self.new_password_entry.pack(pady=5)

        submit_button = tk.Button(frame, text="Modifier", command=lambda: self.modify_user(self.username), width=15, bg="white", fg="#014421", font=("Helvetica", 15))
        submit_button.pack(pady=10)

        back_button = tk.Button(frame, text="Retour", command=self.manage_account, width=10, bg="white", fg="#FF0000", font=("Helvetica", 20))
        back_button.pack(pady=10)
        
        self.update_idletasks()

    def modify_user(self,username):
        users = load_users()
        user = users[users["username"] == username]
        username = self.username_entry.get()
        current_password = self.current_password_entry.get()
        new_email = self.email_entry.get()
        new_username = self.new_username_entry.get()
        new_password = self.new_password_entry.get()

        if user.empty:
            messagebox.showerror("Erreur", "Utilisateur non trouvé.")
            return

        user = user.iloc[0]
        hashed_mdp, salt = user["mot_de_passe"], eval(user["sel"])
        if hash_mdp(current_password, salt)[0] != hashed_mdp:
            messagebox.showerror("Erreur", "Mot de passe actuel incorrect.")
            return username

        if new_email and new_email in users["email"].values:
            messagebox.showerror("Erreur", "Adresse email déjà utilisée.")
            return username

        if new_username:
            if new_username in users["username"].values:
                messagebox.showerror("Erreur", "Nom d'utilisateur déjà utilisé.")
                return username
            else:
                users.loc[users["username"] == username, "username"] = new_username
                self.username = new_username

        if new_email:
            users.loc[users["username"] == username, "email"] = new_email

        if new_password:
            hashed_mdp, salt = hash_mdp(new_password)
            users.loc[users["username"] == (new_username if new_username else username), "mot_de_passe"] = hashed_mdp
            users.loc[users["username"] == (new_username if new_username else username), "sel"] = salt

        save_users(users)
        messagebox.showinfo("Succès", "Les informations ont été mises à jour avec succès !")
        self.logout()

    def open_delete_user(self):
        self.clear_window()
        frame = tk.Frame(self, bg="#1E1E1E")
        frame.pack(padx=20, pady=20, fill="both", expand=True)

        header_label = tk.Label(frame, text="Supprimer un Utilisateur", font=("Helvetica", 25), bg="black", fg="#39FF14")
        header_label.pack(pady=20)

        username_label = tk.Label(frame, text="Nom d'utilisateur", fg="white", bg="black")
        username_label.pack()
        self.username_entry = tk.Entry(frame)
        self.username_entry.pack(pady=5)

        password_label = tk.Label(frame, text="Mot de passe", fg="white", bg="black")
        password_label.pack()
        self.password_entry = tk.Entry(frame, show="*")
        self.password_entry.pack(pady=5)

        submit_button = tk.Button(frame, text="Supprimer", command=self.delete_user, width=15, bg="white", fg="black", font=("Helvetica", 15))
        submit_button.pack(pady=10)

        back_button = tk.Button(frame, text="Retour", command=self.manage_account, width=15, bg="white", fg="black", font=("Helvetica", 15))
        back_button.pack(pady=10)
        
        self.update_idletasks()


    def delete_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        supp_produit_user(self.user_id)
        supp_users(username, password)
        messagebox.showinfo("Succès", f"{username} : Votre compte a été supprimé avec succès !")
        self.logout()

        


    def logout(self):
        """Déconnecte l'utilisateur et retourne à la page de connexion."""
        self.session_utilisateur = None
        self.create_widgets()


    def delete_product(self):
        """Supprime un produits"""
        self.clear_window()
        frame = tk.Frame(self, bg="#1E1E1E")
        frame.pack(padx=20, pady=20, fill="both", expand=True)

        self.delete_product_label = tk.Label(frame, text=" Supprimer un produit ", font=("Helvetica", 25), bg="black", fg="red")
        self.delete_product_label.pack(pady=20)

        self.produit_label = tk.Label(frame, text="Nom du produit à supprimer", bg="black", fg="white")
        self.produit_label.pack()
        self.produit_entry = tk.Entry(frame)
        self.produit_entry.pack(pady=5)

        self.delete_product_button = tk.Button(frame, text="Supprimer", command=self.supp_produits, width=20, bg="white", fg="black", font=("Helvetica", 15))
        self.delete_product_button.pack(pady=10)

        self.back_button = tk.Button(frame, text="Retour", command=self.menu_produit, width=15, bg="white", fg="black", font=("Helvetica", 15))
        self.back_button.pack(pady=10)

        self.update_idletasks()

    def supp_produits(self):
        nom = self.produit_entry.get()

        if not nom:
            messagebox.showerror("Erreur","Veuillez remplir tous les champs ")
            return
        supp_produit(nom)
        
        messagebox.showinfo("Succès", "Produit supprimé avec succès !")

    def logout(self):
        """Déconnecte l'utilisateur et retourne à la page de connexion."""
        self.session_utilisateur = None
        self.create_widgets()


    def delete_product(self):
        """Supprime un produits"""
        self.clear_window()
        frame = tk.Frame(self, bg="#1E1E1E")
        frame.pack(padx=20, pady=20, fill="both", expand=True)

        self.delete_product_label = tk.Label(frame, text=" [-]SUPPRIMER UN PRODUIT ", font=("Helvetica", 25), bg="black", fg="#39FF14")
        self.delete_product_label.pack(pady=20)

        self.produit_label = tk.Label(frame, text="Nom du produit à supprimer", bg="#1E1E1E", fg="white")
        self.produit_label.pack()
        self.produit_entry = tk.Entry(frame)
        self.produit_entry.pack(pady=5)

        self.delete_product_button = tk.Button(frame, text="Supprimer", command=self.supp_produits, width=20, bg="white", fg="#014421", font=("Helvetica", 15))
        self.delete_product_button.pack(pady=10)

        self.back_button = tk.Button(frame, text="Retour", command=self.menu_produit, width=10, bg="white", fg="#FF0000", font=("Helvetica", 20))
        self.back_button.pack(pady=10)

        self.update_idletasks()

    def supp_produits(self):
        nom = self.produit_entry.get()

        if not nom:
            messagebox.showerror("Erreur","Veuillez remplir tous les champs ")
            return
        supp_produit(nom)
        
        messagebox.showinfo("Succès", "Produit supprimé avec succès !")

    def check_password_compromise(self, username, mdp):
        user = load_users()[load_users()["username"] == username]
        if user.empty:
            return

        compromis_data = mdp_compromis(mdp)

        if compromis_data[0]:
            count = compromis_data[1]
            messagebox.showwarning("Mot de passe compromis", f"Votre mot de passe a été compromis {count} fois. Veuillez le changer immédiatement !")
            mail_mdp_compromis(self.user_id)
    

# Lancer l'application
if __name__ == "__main__":
    app = Application()
    app.mainloop()