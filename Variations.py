# -*- coding: utf-8 -*-
"""
Created on Mon May  9 18:20:24 2022

@author: descompa
"""

import DownloadData as DD
import DataSorting as DS


#Mise à jour de la data
DD.get_ten_Mins_Data()
DD.get_dailyData()


#Dictionnaires prix (Instantané)
prixParDepartements = DS.DictDepartements("PrixCarburants_instantane.xml")
prixParCantons = DS.DictCantons("PrixCarburants_instantane.xml")



chaine = DD.get_chaine()
#Dictionnaires prix (Instantané)
prixParDepartementsB = DS.DictDepartements("PrixCarburants_quotidien_" + chaine + ".xml")
prixParCantonsB = DS.DictCantons("PrixCarburants_quotidien_" + chaine + ".xml")


diffDepartements = {key: prixParDepartements[key] - prixParDepartementsB.get(key, 0) for key in prixParDepartements.keys()}
diffCantons = {key: prixParCantons[key] - prixParCantonsB.get(key, 0) for key in prixParCantons.keys()}