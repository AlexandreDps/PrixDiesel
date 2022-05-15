import requests
from bs4 import BeautifulSoup
from lxml import etree

def Xpath(soup,path):
    documentObjectModel = etree.HTML(str(soup)) 
    return (documentObjectModel.xpath(path)[0])

def nbCodeTR6(soup):
    s = soup.find('table', class_='infobox infobox_v2')
    s2 = s.find_all('tr')
    s3 = s2[5]
    s4 = s3.find('td')
    s5 = s4.find_all('a')
    return len(s5)

def nbCodeTR7(soup):
    s = soup.find('table', class_='infobox infobox_v2')
    s2 = s.find_all('tr')
    s3 = s2[6]
    s4 = s3.find('td')
    s5 = s4.find_all('a')
    return len(s5)

def nbCodeTR8(soup):
    s = soup.find('table', class_='infobox infobox_v2')
    s2 = s.find_all('tr')
    s3 = s2[7]
    s4 = s3.find('td')
    s5 = s4.find_all('a')
    return len(s5)

def listeCP(l, path):
    if path == '':
        path = None
    else:
        if int(path) not in l:
            l.append(int(path))
    return l

def listeCPGE(l, soup):
    for i in range(1, nbCodeTR6(soup)+2):
        if i == 9 or i == 10:
            path = Xpath(soup,f'//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[6]/td/a[{i}]').text
            l.append(int(path))
        else:
            path = Xpath(soup,f'//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[6]/td/text()[{i}]')[2:4]
            if path == '':
                path = None
            else:
                if int(path) not in l:
                    l.append(int(path))
    return l


def cpRegion(l):
    d = {}
    for reg in l:
        url = f'https://fr.wikipedia.org/wiki/{reg}'
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        l  = []
        if reg == 'Occitanie_(région_administrative)' or reg == 'Bourgogne-Franche-Comté' or reg =='Normandie_(région_administrative)':
            for i in range(1, nbCodeTR8(soup)+1):
                path = Xpath(soup,f'//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[8]/td/text()[{i}]')[2:4]
                listeCP(l, path)
            d[reg] = l
        elif reg == 'Centre-Val_de_Loire':
            for i in range(1, nbCodeTR6(soup)+1):
                path = Xpath(soup,f'//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[6]/td/text()[{i}]')[2:4]
                listeCP(l, path)
            d[reg] = l
        elif reg == 'Hauts-de-France':
            for i in range(1, nbCodeTR6(soup)+2):
                path = Xpath(soup,f'//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[6]/td/text()[{i}]')[2:4]
                listeCP(l, path)
            d[reg] = l
        elif reg == 'Grand_Est':
            listeCPGE(l, soup)
            d[reg] = l
        elif reg == 'Auvergne-Rhône-Alpes':
            for i in range(1, nbCodeTR7(soup)+2):
                path = Xpath(soup,f'//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[7]/td/text()[{i}]')[2:4]
                listeCP(l, path)
            d[reg] = l
        else:
            for i in range(1, nbCodeTR7(soup)+1):
                path = Xpath(soup,f'//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[7]/td/text()[{i}]')[2:4]
                listeCP(l, path)
            d[reg] = l
    return d


l = ['Nouvelle-Aquitaine', 'Occitanie_(région_administrative)', 'Pays_de_la_Loire', 'Provence-Alpes-Côte_d\'Azur', 'Auvergne-Rhône-Alpes', 'Bourgogne-Franche-Comté', 'Centre-Val_de_Loire', 'Bretagne_(région_administrative)', 'Grand_Est', 'Île-de-France', 'Normandie_(région_administrative)', 'Hauts-de-France']
print(cpRegion(l))

'''
Résultat obtenu :
    {
    'Nouvelle-Aquitaine': [16, 17, 19, 23, 24, 33, 40, 47, 64, 79, 86, 87],
    'Occitanie_(région_administrative)': [9, 11, 12, 30, 31, 32, 34, 46, 48, 65, 66, 81, 82],
    'Pays_de_la_Loire': [44, 49, 53, 72, 85],
    "Provence-Alpes-Côte_d'Azur": [4, 5, 6, 13, 83, 84],
    'Auvergne-Rhône-Alpes': [1, 3, 7, 15, 26, 38, 42, 43, 63, 69, 73, 74],
    'Bourgogne-Franche-Comté': [21, 25, 39, 58, 70, 71, 89, 90],
    'Centre-Val_de_Loire': [18, 28, 36, 37, 41, 45],
    'Bretagne_(région_administrative)': [22, 29, 35, 56],
    'Grand_Est': [8, 10, 51, 52, 54, 55, 57, 67, 68, 88],
    'Île-de-France': [75, 77, 78, 91, 92, 93, 94, 95],
    'Normandie_(région_administrative)': [14, 27, 50, 61, 76],
    'Hauts-de-France': [2, 59, 60, 62, 80]
    }
    
'''
