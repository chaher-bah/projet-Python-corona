from Gest_pes import *
from Gest_meledi import *
from datetime import datetime
def enreg_p(chemin):
    global personnes
    with open(chemin, 'w') as f:
        f.write("Fichier Infected:\n")
        f.write("{:<10} {:<10} {:<10} {:<12} {:<12} {:<5} {:<7} {:<6} {:<5} {:<7}\n".format("CIN", "Nom", "Prenom", "Telephone", "Nationalite", "Age", "Jour", "Mois", "Annee", "Decede"))
        for personne in personnes:
            cin = personne['CIN']
            nom = personne['Nom']
            prenom = personne['Prenom']
            tel = personne['Telephone']
            nationalite = personne['Nationalite']
            age = personne['Age']
            date_infection = datetime.strptime(personne['Date_infection'], '%d/%m/%Y')
            jour = date_infection.day
            mois = date_infection.month
            annee = date_infection.year
            decede = personne['Decede']
            f.write("{:<10} {:<10} {:<10} {:<12} {:<12} {:<5} {:<7} {:<6} {:<5} {:<7}\n".format(cin, nom, prenom, tel, nationalite, age, jour, mois, annee, decede))
    print("Le fichier a été enregistré avec succès.")
#______________________________
def enreg_m(chemin):
    global Maladies
    with open(chemin, 'w') as f:
        f.write("Fichier Maladies:\n")
        f.write("{:<5} {:<10} {:<12} {:<5} \n".format("Code", "CIN", "Maladie", "Nombre d'Annee"))
        for maladie in Maladies:
            code=maladie['Code']
            cin = maladie['CIN']
            nom = maladie['nom_maladie']
            annee = maladie['num_annees']
            f.write("{:<5} {:<10} {:<12} {:<5} \n".format(code,cin, nom, annee))
    print("Le fichier a été enregistré avec succès.")
#______________________________
def recup_p(fichier):
    with open(fichier, 'r') as f:
        f.readline()
        f.readline()
        while True:
            ligne=f.readline()
            if not ligne:
                break
            cin, nom, prenom, tel, nationalite, age, jour, mois, annee, decede = ligne.strip().split()
            #print(nom)
            age = int(age)
            jour = int(jour)
            mois = int(mois)
            annee = int(annee)
            decede = int(decede)
            personne = {'CIN': cin, 'Nom': nom, 'Prenom': prenom, 'Telephone': tel, 'Nationalite': nationalite, 'Age': age, 'Date_infection': (jour,mois,annee), 'Decede': decede}
            aff_personne(personne)
#_________________________________
def recup_m(fichier):
    with open(fichier, 'r') as f:
        f.readline()
        f.readline()
        while True:
            ligne=f.readline()
            if not ligne:
                break
            code,cin, nom,annee= ligne.strip().split()
            m={'Code':code,'CIN':cin,'nom_maladie':nom,'num_annees':annee}
            aff_maladie(m)
"""for i in range (2):
    print(f"info de personne {i+1}")
    personne = ajout_personne()  
    personnes.append(personne)
    print(f"info du maladie {i+1}")
    m=ajout_maladie()
    Maladies.append(m)"""
#enreg_m("C:/Users/bahri/OneDrive/Documents/L 1 sem 2/Prog Python/Project/Maladie.txt")
recup_m("C:/Users/bahri/OneDrive/Documents/L 1 sem 2/Prog Python/Project/Maladie.txt")

