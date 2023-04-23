from Gest_pes import*
from datetime import datetime, timedelta
from Gest_meledi import *
def aff_nation(nationalite):
    for personne in personnes:
        if personne['Nationalite'] == nationalite:
            print(f"le personne ayant le nationalite {nationalite}")
            aff_personne(personne)
#______________________________
def p_quarantaine():
    today = (datetime.now()).date()
    q_date = today - timedelta(days=14)
    
    p_quarantaine = []
    for personne in personnes:
        date_infection = datetime.strptime(personne['Date_infection'],'%d/%m/%Y').date()
        if date_infection >= q_date:
            p_quarantaine.append(personne)
    
    if len(p_quarantaine) == 0:
        print("Aucune personne en quarantaine pour le moment.")
    else:
        print("Liste des personnes en quarantaine :")
        for personne in p_quarantaine:
            print(f"CIN : {personne['CIN']},\n Nom : {personne['Nom']},\n Prénom : {personne['Prenom']},\n Date d'infection : {personne['Date_infection']}")
#________________________________________
def aff_deces():
    nb_total = len(personnes)
    nb_decedees = 0
    p_decedees = []
    for personne in personnes:
        if personne['Decede'] == 1:
            nb_decedees += 1
            p_decedees.append(personne)
    pourcentage_deces = (nb_decedees / nb_total) * 100
    print(f"**Pourcentage de décès : {pourcentage_deces}%")
    print("Liste des personnes décédées :")
    for personne in p_decedees:
        print(f"CIN : {personne['CIN']},\nNom : {personne['Nom']},\nPrénom : {personne['Prenom']}")
#__________________________________________
def risque():
    risques = []
    for personne in personnes:
        pourcentage_r = 0            
        if personne['Age'] > 70:
            pourcentage_r += 20
        elif 50 <= personne['Age'] <= 70:
            pourcentage_r += 10
        
        for maladie in personne['maladie']:
            if maladie['nom_maladie'] == 'diabete':
                pourcentage_r += 15
            elif maladie['nom_maladie'] == 'hypertension':
                pourcentage_r += 20
            elif maladie['nom_maladie'] == 'asthme':
                pourcentage_r += 20
        if pourcentage_r > 0:
            risque_p = {
                'Nom': personne['Nom'],
                'Prenom': personne['Prenom'],
                'Pourcentage_risque': pourcentage_r,
            }
            risques.append(risque_p)
    if len(risques) > 0:
        print("Liste des personnes à risque :")
        for risque_p in risques:
            print(f"{risque_p['Nom']} {risque_p['Prenom']} : {risque_p['Pourcentage_risque']}% de risque")
    else:
        print("Il n'y a aucune personne à risque.")

# TEST
for i in range (2):
    print(f"info de personne {i+1}")
    personne = ajout_personne()  
    personnes.append(personne)
    print(f"maladie {i+1}")
    m=ajout_maladie()
    Maladies.append(m)
risque()
#p_quarantaine()


