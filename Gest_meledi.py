Maladies=[]
code=1
from Gest_pes import *
def ajout_maladie():
    global code
    maladie = {
        'Code': code,
        'CIN': input("Numéro de CIN : "),
        'nom_maladie': input("Nom de maladie: "),
        'num_annees': int(input("donner les annes de maladie: ")), 
    }
    for personne in personnes:
        if maladie['CIN']==personne['CIN']:
            personne['maladie'].append(maladie)
    return maladie
#________________
def aff_maladie (maladie):
    print (maladie['Code'],"\t",maladie['CIN'],"\t",maladie['nom_maladie'],"\t\t",maladie['num_annees'])

def supp_maladie(nom):
    for maladie in Maladies:
        if maladie['nom_maladie'] == nom:
            Maladies.remove(maladie)
            print("Maladie supprimé avec succès.")
    print("Aucun malade trouvé avec ce nom.")
#_______________________
def modif_nbr_annee(cin, nom, new_nbr):
    t=False
    for maladie in Maladies:
        if maladie['CIN'] == cin and maladie['nom_maladie'] == nom:
            maladie['num_annees'] = new_nbr
            t=True
            print("Nombre d'années de la maladie modifié avec succès.")
    if not t:
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
def dict_malad ():
    global Maladies
    print ("code\t CIN\t Nom maladie\t Num annees ")
    for maladie in Maladies:
        aff_maladie(maladie)
        maladie['Code']=maladie['Code']+1
#________________________
def rech_malad(nom):
    global Maladies
    t=False
    for maladie in Maladies:
        if maladie['nom_maladie']==nom:
            print("Maladie Trouvee:\n")
            aff_maladie(maladie)
            t=True
    if t==False:
        print(f"Aucune personne trouvée avec le maladie '{nom}'.")
#___________________________________
def rech_m():
    nom= input("Donner le nom de la maladie : ")
    t=False
    for personne in personnes:
        for maladie in personne['maladie']:
            if maladie['nom_maladie'] == nom:
                t=True
                print(f"Les personnes avec la maladie {nom} sont :")
                aff_personne(personne)
    if not t:
        print(f"Aucune personne avec la maladie {nom} n'a été trouvée.")
#_____________________________________
def rech_m_p():
    cin = input("Entrez le numéro de CIN de la personne : ")
    maladies_trouvees = []
    for maladie in Maladies:
        if maladie['CIN'] == cin:
            maladies_trouvees.append(maladie)
    if len(maladies_trouvees) > 0:
        print(f"Les maladies de la personne de CIN {cin} sont :")
        for maladie in maladies_trouvees:
            print(f"- {maladie['nom_maladie']}")
    else:
        print(f"Aucune maladie trouvée pour la personne de CIN {cin}.")
#_____________________________________
def rech_pourcent():
    maladie_count = {}
    total = len(Maladies)
    for maladie in Maladies:
        if maladie['nom_maladie'] not in maladie_count:
            maladie_count[maladie['nom_maladie']] = 1
        else:
            maladie_count[maladie['nom_maladie']] += 1
    for nom_maladie, count in maladie_count.items():
        pourcent = (count / total) * 100
        print(f"{nom_maladie} : {pourcent:.2f}%")
#_____________________________________
def rech_m_chaque_p():
    global personnes
    for personne in personnes:
        print("Informations sur la personne :")
        aff_personne(personne)
        maladies = []
        for maladie in personne['maladie']:
            maladies.append(maladie['nom_maladie'])
        print("Liste des maladies : ", maladies)
        print("\n")
#________________________________
#   TEST
"""personne = ajout_personne()  
personnes.append(personne)"""
print("Saisie des informations de la maladie :")
malad=ajout_maladie()
Maladies.append(malad)
code+=1
modif_nbr_annee("0123456","nom",45)

#dict_malad()