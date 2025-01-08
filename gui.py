from Modules.gestion_utilisateur import *
from Modules.gestion_csv_produit import *
from Modules.authentification import *
import tkinter as tk
from tkinter import messagebox
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
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
    root.title("PROJET ALGORITMIE 🧮")
    root.geometry("1000x1000")

    # Frame principale
    main_frame = tk.Frame(root)
    main_frame.pack(fill="both", expand=True)

    # Afficher le menu principal
    def show_menu():
        for widget in main_frame.winfo_children():
            widget.destroy()
        label = tk.Label(main_frame, text="====== MENU PRINCIPAL =====", font=("Helvetica", 70))
        label.pack(pady=10)

        # Boutons du menu principal
        btn_connexion = tk.Button(main_frame, text="CONNEXION", font=("Helvetica", 40), command=lambda: form_connexion())
        btn_connexion.pack(pady=5)

        btn_inscription = tk.Button(main_frame, text="INSCRIPTION", font=("Helvetica", 40), command=lambda: form_inscription())
        btn_inscription.pack(pady=5)

        btn_quitter = tk.Button(main_frame, text="QUITTER", width=20, command=root.quit)
        btn_quitter.pack(pady=5)

    show_menu()  # Afficher le menu principal

    # Formulaire de connexion
    def form_connexion():
        for widget in root.winfo_children():
            widget.destroy()
        form_connexion_window = tk.Frame(root)
        form_connexion_window.pack(pady=20)

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
    def form_inscription():
        for widget in main_frame.winfo_children():
            widget.destroy()
        form_inscription_window = tk.Frame(main_frame)
        form_inscription_window.pack(pady=20)

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
                show_menu()  # Retourner au menu principal après inscription
            else:
                messagebox.showwarning("Champs manquants", "Veuillez remplir tous les champs")

        btn_inscrire = tk.Button(form_inscription_window, text="S'inscrire", command=s_inscrire)
        btn_inscrire.pack(pady=10)

    # Fonction de session utilisateur
    def session(user_id, username, mdp):
        for widget in main_frame.winfo_children():
            widget.destroy()

        # Créer un frame de session
        session_frame = tk.Frame(main_frame)
        session_frame.pack(pady=20)

        label_session = tk.Label(session_frame, text=f"Bienvenue {username}", font=("Helvetica", 14))
        label_session.pack(pady=10)

        btn_gestion_produits = tk.Button(session_frame, text="Gérer mes produits", width=20, command=lambda: gestion_produits())
        btn_gestion_produits.pack(pady=5)

        btn_gestion_compte = tk.Button(session_frame, text="Gérer mon compte", width=20, command=lambda: gestion_compte())
        btn_gestion_compte.pack(pady=5)

        btn_deconnexion = tk.Button(session_frame, text="Déconnexion", width=20, command=root.quit)
        btn_deconnexion.pack(pady=5)

    # Gérer les produits
    def gestion_produits():
        for widget in main_frame.winfo_children():
            widget.destroy()

        gestion_produits_window = tk.Frame(main_frame)
        gestion_produits_window.pack(pady=20)

        tk.Label(gestion_produits_window, text="Choisissez une option de gestion des produits").pack(pady=10)

        # Exemple de gestion des produits
        btn_ajouter_produit = tk.Button(gestion_produits_window, text="Ajouter un Produit", width=20)
        btn_ajouter_produit.pack(pady=5)

        btn_afficher_produits = tk.Button(gestion_produits_window, text="Afficher tous les Produits", width=20)
        btn_afficher_produits.pack(pady=5)

        btn_retour = tk.Button(gestion_produits_window, text="Retour", width=20, command=show_menu)
        btn_retour.pack(pady=5)

    # Gérer le compte utilisateur
    def gestion_compte():
        for widget in main_frame.winfo_children():
            widget.destroy()

        gestion_compte_window = tk.Frame(main_frame)
        gestion_compte_window.pack(pady=20)

        tk.Label(gestion_compte_window, text="Choisissez une option de gestion du compte").pack(pady=10)

        # Exemple de gestion du compte
        btn_modifier_info = tk.Button(gestion_compte_window, text="Modifier mes informations", width=20)
        btn_modifier_info.pack(pady=5)

        btn_supprimer_compte = tk.Button(gestion_compte_window, text="Supprimer mon compte", width=20)
        btn_supprimer_compte.pack(pady=5)

        btn_retour = tk.Button(gestion_compte_window, text="Retour", width=20, command=show_menu)
        btn_retour.pack(pady=5)

    # Lancer l'application
    root.mainloop()

if __name__ == "__main__":
    menu_principal()