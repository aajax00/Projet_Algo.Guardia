from Modules.gestion_utilisateur import *
from Modules.gestion_csv_produit import *
from Modules.authentification import *
import tkinter as tk
from tkinter import messagebox
import getpass
import time
import os

GREEN = "\033[1;32m"
RED = "\033[31m"
BLUE = "\033[94m"
JAUNE = "\033[33m"
END = "\033[0m" 

def instance():
    os.system('cls' if os.name == 'nt' else 'clear')
    

def menu_principal():
    root = tk.Tk()
    root.title("PROJET ALGORITMIE")
    root.geometry("400x300") 
    # root.configure(bg="black")
    
    label = tk.Label(root, text="====== MENU PRINCIPAL =====", font=("Helvetica", 14))
    label.pack(pady=10)
    
    # Boutons
    btn_connexion = tk.Button(root, text="Connexion", width=20, command=lambda: form_connexion(root))
    btn_connexion.pack(pady=5)
    
    btn_inscription = tk.Button(root, text="Inscription", width=20, command=lambda: form_inscription(root))
    btn_inscription.pack(pady=5)
    
    btn_quitter = tk.Button(root, text="Quitter", width=20, command=root.quit)
    btn_quitter.pack(pady=5)
    
    root.mainloop()
    
# Formulaire de connexion
def form_connexion(root):
    form_connexion_window = tk.Toplevel(root)
    form_connexion_window.title("=== FORMULAIRE DE CONNEXION ===")
    form_connexion_window.geometry("300x200")
        
    tk.Label(form_connexion_window, text="Nom d'utilisateur:").pack(pady=5)
    username_entry = tk.Entry(form_connexion_window)
    username_entry.pack(pady=5)

    tk.Label(form_connexion_window, text="Mot de passe:").pack(pady=5)
    mdp_entry = tk.Entry(form_connexion_window, show="*")
    mdp_entry.pack(pady=5)
        
    def se_connecter():
        username = username_entry.get()
        mdp = mdp_entry.get()
        if username and mdp:
            login_user(username, mdp)
            user_id = "exemple_user_id"  # Remplace par un appel réel à login_user()

            if user_id:
                form_connexion_window.destroy()
                session(user_id, username, mdp)
            else:
                messagebox.showerror("Erreur", "Nom d'utilisateur ou mot de passe incorrect")
        else:
            messagebox.showwarning("Champs manquants", "Veuillez remplir tous les champs")

    btn_connexion = tk.Button(form_connexion_window, text="Se connecter", command=se_connecter)
    btn_connexion.pack(pady=10)

# Formulaire d'inscription
def form_inscription(root):
    form_inscription_window = tk.Toplevel(root)
    form_inscription_window.title("Inscription")
    form_inscription_window.geometry("300x200")

    tk.Label(form_inscription_window, text="Nom d'utilisateur:").pack(pady=5)
    username_entry = tk.Entry(form_inscription_window)
    username_entry.pack(pady=5)

    tk.Label(form_inscription_window, text="Mot de passe:").pack(pady=5)
    mdp_entry = tk.Entry(form_inscription_window, show="*")
    mdp_entry.pack(pady=5)

    def s_inscrire():
        username = username_entry.get()
        mdp = mdp_entry.get()
        if username and mdp:
            # Utiliser la fonction pour ajouter l'utilisateur
            # add_users(username, mdp)
            messagebox.showinfo("Succès", "Inscription réussie !")
            form_inscription_window.destroy()
        else:
            messagebox.showwarning("Champs manquants", "Veuillez remplir tous les champs")

    btn_inscrire = tk.Button(form_inscription_window, text="S'inscrire", command=s_inscrire)
    btn_inscrire.pack(pady=10)

# Fonction de session utilisateur
def session(user_id, username, mdp):
    # Créer une nouvelle fenêtre de session
    session_window = tk.Tk()
    session_window.title(f"Session - {username}")
    session_window.geometry("400x300")
    
    # Affichage des informations
    label_session = tk.Label(session_window, text=f"Bienvenue {username}", font=("Helvetica", 14))
    label_session.pack(pady=10)

    btn_gestion_produits = tk.Button(session_window, text="Gérer mes produits", width=20, command=lambda: gestion_produits(session_window, user_id, username))
    btn_gestion_produits.pack(pady=5)

    btn_gestion_compte = tk.Button(session_window, text="Gérer mon compte", width=20, command=lambda: gestion_compte(session_window, user_id, username))
    btn_gestion_compte.pack(pady=5)

    btn_deconnexion = tk.Button(session_window, text="Déconnexion", width=20, command=session_window.quit)
    btn_deconnexion.pack(pady=5)

    session_window.mainloop()

# Gérer les produits
def gestion_produits(session_window, user_id, username):
    gestion_produits_window = tk.Toplevel(session_window)
    gestion_produits_window.title("Gestion des Produits")
    gestion_produits_window.geometry("300x200")

    tk.Label(gestion_produits_window, text="Choisissez une option de gestion des produits").pack(pady=10)

    # Exemple de gestion des produits
    btn_ajouter_produit = tk.Button(gestion_produits_window, text="Ajouter un Produit", width=20)
    btn_ajouter_produit.pack(pady=5)

    btn_afficher_produits = tk.Button(gestion_produits_window, text="Afficher tous les Produits", width=20)
    btn_afficher_produits.pack(pady=5)

    btn_retour = tk.Button(gestion_produits_window, text="Retour", width=20, command=gestion_produits_window.destroy)
    btn_retour.pack(pady=5)

# Gérer le compte utilisateur
def gestion_compte(session_window, user_id, username):
    gestion_compte_window = tk.Toplevel(session_window)
    gestion_compte_window.title("Gestion du Compte")
    gestion_compte_window.geometry("300x200")

    tk.Label(gestion_compte_window, text="Choisissez une option de gestion du compte").pack(pady=10)

    # Exemple de gestion du compte
    btn_modifier_info = tk.Button(gestion_compte_window, text="Modifier mes informations", width=20)
    btn_modifier_info.pack(pady=5)

    btn_supprimer_compte = tk.Button(gestion_compte_window, text="Supprimer mon compte", width=20)
    btn_supprimer_compte.pack(pady=5)

    btn_retour = tk.Button(gestion_compte_window, text="Retour", width=20, command=gestion_compte_window.destroy)
    btn_retour.pack(pady=5)
    
    
    
if __name__ == "__main__":
    menu_principal()