# -*- coding: utf-8 -*-
"""
Created on Thu May  5 17:25:14 2022

@author: descompa
"""

from zipfile import ZipFile 
import wget
import os





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


    

def get_annualData():
    
    if os.path.isfile("PrixCarburants_annuel_2022.zip") == True :
        os.remove("PrixCarburants_annuel_2022.zip")
    if os.path.isfile("PrixCarburants_annuel_2022.xml") == True :
        os.remove("PrixCarburants_annuel_2022.xml")
        
    url='https://donnees.roulez-eco.fr/opendata/annee'
    wget.download(url)
    
    # Décompression du fichier zip
    file = "PrixCarburants_annuel_2022.zip"
    with ZipFile(file, 'r') as zip: 
        print('Extraction du fichier PrixCarburants_annuel_2022 ...') 
        zip.extractall() 
        print('Terminé !') 