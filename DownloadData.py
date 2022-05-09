# -*- coding: utf-8 -*-
"""
Created on Thu May  5 17:25:14 2022

@author: descompa
"""

from zipfile import ZipFile 
import wget
import os
import datetime





def get_ten_Mins_Data() :
    
    #On supprime les vieux fichiers
    if os.path.isfile('PrixCarburants_instantane.zip') == True :
        os.remove("PrixCarburants_instantane.zip")
    if os.path.isfile("PrixCarburants_instantane.xml") == True :
        os.remove("PrixCarburants_instantane.xml")
    
    
    #Téléchargement du fichier zip
    url='https://donnees.roulez-eco.fr/opendata/instantane'
    wget.download(url)



    # Décompression des fichiers zip
    file = "PrixCarburants_instantane.zip"
    
    # ouvrir le fichier zip en mode lecture
    with ZipFile(file, 'r') as zip: 
      
        # extraire tous les fichiers
        print('Extraction du fichier PrixCarburants_instantane ...') 
        zip.extractall() 
        print('Terminé !') 


    

def get_dailyData():
    
    annee = datetime.datetime.today().strftime('%Y')
    mois = datetime.datetime.today().strftime('%m')
    jour =  '0' + str(int(datetime.datetime.today().strftime('%d')) - 1) #Veille
    chaine = annee + mois + jour
    
    
    if os.path.isfile("PrixCarburants_quotidien_" + chaine + ".zip") == True :
        os.remove("PrixCarburants_quotidien_" + chaine + ".zip")
    if os.path.isfile("PrixCarburants_quotidien_" + chaine + ".xml") == True :
        os.remove("PrixCarburants_quotidien_" + chaine + ".xml")
        
    url='https://donnees.roulez-eco.fr/opendata/jour/' + chaine
    wget.download(url)
    
    # Décompression du fichier zip
    file = "PrixCarburants_quotidien_" + chaine + ".zip"
    with ZipFile(file, 'r') as zip: 
        print('Extraction du fichier PrixCarburants_quotidien ...') 
        zip.extractall() 
        print('Terminé !') 
