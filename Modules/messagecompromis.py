import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pnds
from Modules.gestion_utilisateur import *

def mail_mdp_compromis (user_id) :
    user = load_users()
    x = user_id - 1
    expediteur = user['email'].values[0]
    destinataire = user['email'].values[x]
    mot_de_passe = 'kvxp quas ytqd nqhi'

    msg = MIMEMultipart()
    msg['From'] = expediteur
    msg['To'] = destinataire
    msg['Subject'] = "Mot de passe Compromis"
    
    corps = ("Votre mot de passe a été retrouvé dans une base de données de mot de passe compromis.\nVeuillez changer de mot de passse afin d'éviter toutes fuites de données.")
    msg.attach(MIMEText(corps, 'plain'))
    try:
        serveur = smtplib.SMTP('smtp.gmail.com', 587)
        serveur.starttls()
        serveur.login(expediteur, mot_de_passe)
        texte = msg.as_string()
        serveur.sendmail(expediteur, destinataire, texte)
        serveur.quit()
    except Exception as e:
        print(f"Erreur lors de l'envoi de l'e-mail : {e}")