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


class InterfaceGraphique(tk.Tk):
    def __init__(self):
        super().__init__()
        
        # Fenêtre principale
        self.title("PROJET ALGORITHMIE - Gestion d'Utilisateurs et Produits")
        self.geometry("1000x1000")
        # self.configure(bg='white')
        
        self.session_utilisateur = None
        self.current_user = None
        
        self.create_widgets()
        
    def create_widgets(self):
        # self.clear_windows()
        
        self.header_label = tk.Label(self, text="MENU D'AUTHENTIFICATION", font=("Arial", 16))
        
        
        
        
        
# Lancer l'application
if __name__ == "__main__":
    app = InterfaceGraphique()
    app.mainloop()