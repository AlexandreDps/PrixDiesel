# -*- coding: utf-8 -*-
"""
Created on Tue May  3 15:29:49 2022

@author: descompa
"""

from zipfile import ZipFile 
import wget
import os


#On supprime les vieux fichiers
if os.path.isfile('PrixCarburants_instantane.zip') == True :
    os.remove("PrixCarburants_instantane.zip")
if os.path.isfile("PrixCarburants_instantane.xml") == True :
    os.remove("PrixCarburants_instantane.xml")
if os.path.isfile("PrixCarburants_annuel_2022.zip") == True :
    os.remove("PrixCarburants_annuel_2022.zip")
if os.path.isfile("PrixCarburants_annuel_2022.xml") == True :
    os.remove("PrixCarburants_annuel_2022.xml")

#Téléchargement des fichiers zip
url='https://donnees.roulez-eco.fr/opendata/instantane'
wget.download(url)
url='https://donnees.roulez-eco.fr/opendata/annee'
wget.download(url)


# Décompression des fichiers zip
file = "PrixCarburants_instantane.zip"

# ouvrir le fichier zip en mode lecture
with ZipFile(file, 'r') as zip: 
    # afficher tout le contenu du fichier zip
    #print("Contenu du dossier zip : ")
    #zip.printdir() 
  
    # extraire tous les fichiers
    print('Extraction du fichier 1/2 ...') 
    zip.extractall() 
    print('Fichier 1 dézippé') 

# Décompression du fichier zip
file = "PrixCarburants_annuel_2022.zip"

# ouvrir le fichier zip en mode lecture
with ZipFile(file, 'r') as zip: 
    # afficher tout le contenu du fichier zip
    #print("Contenu du dossier zip : ")
    #zip.printdir() 
  
    # extraire tous les fichiers
    print('Extraction du fichier 2/2 ...') 
    zip.extractall() 
    print('Terminé!') 

############################### Récupération des données ###############################



from lxml import etree

tree = etree.parse("PrixCarburants_instantane.xml")

r = tree.getroot()

latitudes = []
longitudes = []
prixGazole = [] 
departements = []
cantons = []

for i in range(len(r)):
    
    latitudes.append(float(r[i].attrib['latitude'])/100000)
    longitudes.append(float(r[i].attrib['longitude'])/100000)
    departements.append(int(r[i].attrib['cp'][:2:]))
    cantons.append(r[i][1].text)
    test = r[i] #Vérifie que r[i] peut être parcouru au rang 4
    if len(test) > 4:
        if r[i][4].attrib['nom'] == 'Gazole':
            prixGazole.append(float(r[i][4].attrib['valeur']))
        else : prixGazole.append(None)
    else : prixGazole.append(None)
 
John = [] #John est la liste de coordonnées   
for i in range(len(r)):
    John.append([latitudes[i], longitudes[i], prixGazole[i]])


############################### Moyenne par départements #####################

PrixParDepartements = {}
for d in range(1,96): #Car 96 départements renseignés
    sum = 0
    nb = 0
    for i in range (len(departements)):
        if d == departements[i]:
            if prixGazole[i] != None:
                sum += prixGazole[i]
                nb += 1
    PrixParDepartements[d] = sum/nb
            
    
############################### Moyenne par cantons #####################

PrixParCantons = {}

for d in set(cantons):
    sum = 0
    nb = 0
    for i in range (len(cantons)):
        if d == cantons[i]:
            if prixGazole[i] != None:
                sum += prixGazole[i]
                nb += 1
    if nb>0 : PrixParCantons[d] = sum/nb



#folium.Marker(location=[46.227638, 2.213749],popup='Marker 1',icon=folium.features.CustomIcon('https://cdn.icon-icons.com/icons2/510/PNG/512/arrow-up-c_icon-icons.com_50458.png', icon_size=(14, 14))).add_to(m)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

