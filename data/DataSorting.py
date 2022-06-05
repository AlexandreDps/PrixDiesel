from lxml import etree


def ArbreGlobal(fichier):
   
    tree = etree.parse(fichier)
    
    r = tree.getroot()
    
    latitudes = []
    longitudes = []
    prixGazole = [] 
    departements = []
    cantons = []
    
    for i in range(len(r)):
        print("Progression : " + str(round(100/len(r)*i,3)) + " %" )
        if (r[i].attrib['latitude']) != '' :
            latitudes.append(float(r[i].attrib['latitude'])/100000)
        else : latitudes.append(None)
        if r[i].attrib['longitude'] != '' :
            longitudes.append(float(r[i].attrib['longitude'])/100000)
        else : longitudes.append(None)
        if 20000 <= int(r[i].attrib['cp']) < 20200:
            departements.append('2A')
        elif 20200 <= int(r[i].attrib['cp']) < 20300:
            departements.append('2B')
        else:
            departements.append(r[i].attrib['cp'][:2:])
        cantons.append(r[i][1].text)
        test = r[i] #Vérifie que r[i] peut être parcouru au rang 4
        if len(test) > 4:
            if 'nom' in r[i][4].attrib :
                if r[i][4].attrib['nom'] == 'Gazole' :
                    if 'valeur' in r[i][4].attrib:
                        if float(r[i][4].attrib['valeur']) < 5 :
                            prixGazole.append(float(r[i][4].attrib['valeur']))
                        else : prixGazole.append(None)
                    else: prixGazole.append(None)
                else : prixGazole.append(None)
            else : prixGazole.append(None)
        else : prixGazole.append(None)
        
    res = [latitudes,longitudes,prixGazole,departements,cantons]
    return res

############################### Moyenne par départements #####################

def DictDepartements(fichier):
    dictionnaire = {}
    data = ArbreGlobal(fichier)
    departements = data[3]
    prixGazole = data[2]
    for d in departements:
        sum = 0
        nb = 0
        for i in range (len(departements)):
            if d == departements[i]:
                if prixGazole[i] != None:
                    sum += prixGazole[i]
                    nb += 1
        if nb == 0 :
            dictionnaire[d] = None
        else : dictionnaire[d] = sum/nb
    dictionnaire = dict(sorted(dictionnaire.items(), key=lambda t: t[0]))
    return dictionnaire
            
    
############################### Moyenne par cantons #####################


def DictCantons(fichier):
    dictionnaire = {}
    data = ArbreGlobal(fichier)
    cantons = data[4]
    prixGazole = data[2]
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

############################### Moyenne par régions #####################

def DictRegions(fichier):
    d = {'Nouvelle-Aquitaine': ['16', '17', '19', '23', '24', '33', '40', '47', '64', '79', '86', '87'],
         'Occitanie': ['09', '11', '12', '30', '31', '32', '34', '46', '48', '65', '66', '81', '82'],
         'Pays de la Loire': ['44', '49', '53', '72', '85'],
         "Provence-Alpes-Côte d'Azur": ['04', '05', '06', '13', '83', '84'],
         'Auvergne-Rhône-Alpes': ['01', '03', '07', '15', '26', '38', '42', '43', '63', '69', '73', '74'],
         'Bourgogne-Franche-Comté': ['21', '25', '39', '58', '70', '71', '89', '90'],
         'Centre-Val de Loire': ['18', '28', '36', '37', '41', '45'],
         'Bretagne': ['22', '29', '35', '56'],
         'Grand Est': ['08', '10', '51', '52', '54', '55', '57', '67', '68', '88'],
         'Île-de-France': ['75', '77', '78', '91', '92', '93', '94', '95'],
         'Normandie': ['14', '27', '50', '61', '76'],
         'Hauts-de-France': ['02', '59', '60', '62', '80'],
         'Corse': ['2A', '2B']}
    dr = {}
    d2 = DictDepartements(fichier)
    for reg in d:
        nb = 0
        for cp in d2:
            if cp in d[reg]:
                nb += d2[cp]
        moy = nb/len(d[reg])
        dr[reg] = moy
    return dr
