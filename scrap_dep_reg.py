import requests
from bs4 import BeautifulSoup
from lxml import etree

def Xpath(soup,path):
    documentObjectModel = etree.HTML(str(soup)) 
    return (documentObjectModel.xpath(path)[0])


def nbCode(soup):
    s = soup.find('table', class_='infobox infobox_v2')
    s2 = s.find_all('tr')
    s3 = s2[6]
    s4 = s3.find('td')
    s5 = s4.find_all('a')
    return len(s5)

def nbCodeOCC(soup):
    s = soup.find('table', class_='infobox infobox_v2')
    s2 = s.find_all('tr')
    s3 = s2[7]
    s4 = s3.find('td')
    s5 = s4.find_all('a')
    return len(s5)


def cpRegion(l):
    d = {}
    for reg in l:
        url = f'https://fr.wikipedia.org/wiki/{reg}'
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        l  = []
        if reg == 'Occitanie_(région_administrative)':
            for i in range(1, nbCodeOCC(soup)+1):
                l.append(Xpath(soup,f'//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[8]/td/text()[{i}]'))
            d[reg] = l
        else:
            for i in range(1, nbCode(soup)+1):
                l.append(Xpath(soup,f'//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[7]/td/text()[{i}]'))
            d[reg] = l
    return d

l = ['Nouvelle-Aquitaine', 'Occitanie_(région_administrative)', 'Pays_de_la_Loire']
print(cpRegion(l))