from lxml import etree


#"PrixCarburants_instantane.xml"



def ArbreGlobal(fichier):
   
    tree = etree.parse(fichier)
    
    r = tree.getroot()
    
    latitudes = []
    longitudes = []
    prixGazole = [] 
    departements = []
    cantons = []
    
    for i in range(len(r)):
        print("Progression : " + str(((100/len(r))*i)) + "%" )
        if (r[i].attrib['latitude']) != '' :
            latitudes.append(float(r[i].attrib['latitude'])/100000)
        else : latitudes.append(None)
        if r[i].attrib['longitude'] != '' :
            longitudes.append(float(r[i].attrib['longitude'])/100000)
        else : longitudes.append(None)
        departements.append(int(r[i].attrib['cp'][:2:]))
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
#ArbreGlobal("PrixCarburants_quotidien_20220506.xml")


def DictDepartements(fichier):
    dictionnaire = {}
    data = ArbreGlobal(fichier)
    departements = data[3]
    prixGazole = data[2]
    for d in range(1,96): #Car 96 départements renseignés
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

def DictRegions(fichier, d):
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
                