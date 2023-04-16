Maladies=[]
from Gest_pes import *
def ajout_maladie():
    maladie = {
        'Code': 1,
        'CIN': input("Numéro de CIN : "),
        'nom_maladie': input("Nom de maladie: "),
        'num_annees': int(input("donner les annes de maladie ")), 
    }
    return maladie
#________________
def supp_maladie(nom):
    for maladie in Maladies:
        if maladie['Nom_Maladie'] == nom:
            Maladies.remove(maladie)
            print("Maladie supprimé avec succès.")
    print("Aucun malade trouvé avec ce nom.")
#_______________________
def modif_nbr_annee(cin, nom, new_nbr):
    for maladie in Maladies:
        if maladie['CIN'] == cin and malade['nom_maladie'] == nom:
            maladie['num_annees'] = new_nbr
            print("Nombre d'années de la maladie modifié avec succès.")
    print(f"Aucun malade trouvé avec {cin} et de nom {nom}.")
#__________________________
def modif_deces(cin):
    for personne in personnes:
        if personne['CIN'] == cin:
            if personne['Decede'] == 0:
                personne['decede'] = 1
                print("L'état de décès de la personne a été modifié.")
            else:
                print("La personne est déjà marquée comme décédée.")
            return
    print("Aucune personne trouvée avec ce CIN.") 
#______________________________
