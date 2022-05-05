# -*- coding: utf-8 -*-
"""
Created on Tue May  3 15:29:49 2022

@author: descompa
"""

import DownloadData as DD
import DataSorting as DS


#Mise à jour de la data
DD.get_ten_Mins_Data()
DD.get_annualData()


#Dictionnaires prix
prixParDepartements = DS.DictDepartements()
prixParCantons = DS.DictCantons()

