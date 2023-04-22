personnes=[]
def ajout_personne():
    personne = {
        'CIN': input("Numéro de CIN : ") ,
        'Nom': input("Nom : "),
        'Prenom': input("Prénom : "),
        'Age': int(input("Âge : ")),
        'Adresse': input("Adresse : "),
        'Nationalite': input("Nationalité : "),
        'Telephone': input("Téléphone : "),
        'Date_infection': input("Date d'infection (jj/mm/aaaa) : "),
        'Decede': int(input("donner 0 si personne decede,1sinon  :   ")),
        'maladie':[],
    }
    return personne
#____________________________________________________________
def aff_personne(personne):
    print("Données de la personne :")
    print("- CIN :", personne['CIN'])
    print("  Nom :", personne['Nom'])
    print("  Prénom :", personne['Prenom'])
    print("  Age :", personne['Age'])
    print("  Adresse :", personne['Adresse'])
    print("  Nationalité :", personne['Nationalite'])
    print("  Téléphone :", personne['Telephone'])
    print("  Date d'infection :", personne['Date_infection'])
    print("  Décédé :", personne['Decede'])
def affiche (personne):
    print(personne['CIN'],"  ",personne['Nom'],"  ",personne['Prenom'],"    \t",personne['Age'],"\t",personne['Nationalite'],"\t",personne['Telephone'],"  \t",personne['Date_infection'],"     ",personne['Decede'])
#___________________________________________
def supp_pers_donne(nom, prenom):
    for personne in personnes:
        if personne['Nom'] == nom and personne['Prenom'] == prenom:
            personnes.remove(personne)
            print(f"La personne {nom} {prenom} a été supprimée avec succès !")
        print(f"La personne {nom} {prenom} n'a pas été trouvée.")
#________________________________________________
def supp_nation(nationalite):
    global personnes 
    i = 0
    while i < len(personnes):
        if personnes[i]['Nationalite'] == nationalite:
            personnes.pop(i)
        else:
            i += 1
    print(f"Les personnes de nationalité '{nationalite}' ont été supprimées!")
#____________________________________________________
def supp_pers_indi(indicatif):
    global personnes
    i = 0
    while i < len(personnes):
        if personnes[i]['Telephone'].find(indicatif) == 0 :
            personnes.pop(i)
        else:
            i += 1
    print(f"Les personnes avec l'indicatif '{indicatif}' ont été supprimées")
#_____________________________________________
def modif_tel(nom, prenom, nouveau_tel):
    global personnes 
    for personne in personnes:
        if personne['Nom'] == nom and personne['Prenom'] == prenom:
            personne['Telephone'] = nouveau_tel
#_________________________________________________
def modif_adresse(nom, prenom, nouvelle_adresse):
    global personnes  
    for personne in personnes:
        if personne['Nom'] == nom and personne['Prenom'] == prenom:
            personne['Adresse'] = nouvelle_adresse
#__________________________________________________
def dict_pers():
    global personnes 
    print("CIN\t  Nom \t   Prenom\tAge\t   Nationalité\t   Tél\t      D_infection\t    \t  Décés",)
    for personne in personnes:
        affiche(personne)
#_________________________________________________
def rech_tel(num_tel):
    global personnes  
    personne_trouvee = False

    for personne in personnes:
        if personne['Telephone'] == num_tel:
            print("Informations de la personne trouvée :")
            aff_personne(personne) 
            print("--------------------")
            personne_trouvee = True
    if not personne_trouvee:
        print(f"Aucune personne trouvée avec le numéro de téléphone '{num_tel}'.")
#_______________________________________________
def rech_nation(nation):
    global personnes  
    personne_trouvee = False

    for personne in personnes:
        if personne['Nationalite'] == nation:
            print("Informations de la personne trouvée :")
            aff_personne(personne) 
            print("--------------------")
            personne_trouvee = True
    if not personne_trouvee:
        print(f"Aucune personne trouvée avec la nationalite'{nation}'.")
#____________________________________________
def rech_ind(indicatif):
    global personnes 
    personne_trouvee = False

    for personne in personnes:
        if personne['Telephone'].find(indicatif) == 0:
            print("Informations de la personne trouvée :")
            aff_personne(personne)  
            print("--------------------")
            personne_trouvee = True
    if not personne_trouvee:
        print(f"Aucune personne trouvée avec l'indicatif '{indicatif}'.")       
#______________________________________________________
def rech_dec():
    global personnes 
    personne_trouvee = False

    for personne in personnes:
        if personne['Decede']:
            print("Informations de la personne décédée :")
            aff_personne(personne)  
            print("--------------------")
            personne_decedee_trouvee = True

    if not personne_decedee_trouvee:
        print("Aucune personne décédée trouvée.")
#_____________________________________
def rech_ndec():
    global personnes 
    personne_trouvee = False

    for personne in personnes:
        if personne['Decede']==0:
            print("Informations de la personne non décédée :")
            aff_personne(personne)  
            print("--------------------")
            personne_trouvee = True

    if not personne_trouvee:
        print("Aucune personne non décédée trouvée.")
#______________________________________
#  TEST
"""for i in range(1):
    print(f"Saisie des informations de la personne {i + 1}:")
    personne = ajout_personne()  
    personnes.append(personne)
dict_pers()"""
