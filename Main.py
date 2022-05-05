# -*- coding: utf-8 -*-
"""
Created on Tue May  3 15:29:49 2022

@author: descompa
"""

import DownloadData as DD

DD.get_ten_Mins_Data()
DD.get_annualData()

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
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

