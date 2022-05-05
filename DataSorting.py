# -*- coding: utf-8 -*-
"""
Created on Thu May  5 17:43:31 2022

@author: descompa
"""

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


def DictDepartements(dictionnaire = {}):
    for d in range(1,96): #Car 96 départements renseignés
        sum = 0
        nb = 0
        for i in range (len(departements)):
            if d == departements[i]:
                if prixGazole[i] != None:
                    sum += prixGazole[i]
                    nb += 1
        dictionnaire[d] = sum/nb
    return dictionnaire
            
    
############################### Moyenne par cantons #####################


def DictCantons(dictionnaire={}):
    
    for d in set(cantons):
        sum = 0
        nb = 0
        for i in range (len(cantons)):
            if d == cantons[i]:
                if prixGazole[i] != None:
                    sum += prixGazole[i]
                    nb += 1
        if nb>0 : dictionnaire[d] = sum/nb
    return dictionnaire