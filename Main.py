import downald as DD
import moyenne as DS


#Mise à jour de la data
DD.get_ten_Mins_Data()
DD.get_dailyData()


d = {'Nouvelle-Aquitaine': [16, 17, 19, 23, 24, 33, 40, 47, 64, 79, 86, 87], 'Occitanie_(région_administrative)': [9, 11, 12, 30, 31, 32, 34, 46, 48, 65, 66, 81, 82], 'Pays_de_la_Loire': [44, 49, 53, 72, 85], "Provence-Alpes-Côte_d'Azur": [4, 5, 6, 13, 83, 84], 'Auvergne-Rhône-Alpes': [1, 3, 7, 15, 26, 38, 42, 43, 63, 69, 73, 74], 'Bourgogne-Franche-Comté': [21, 25, 39, 58, 70, 71, 89, 90], 'Centre-Val_de_Loire': [18, 28, 36, 37, 41, 45], 'Bretagne_(région_administrative)': [22, 29, 35, 56], 'Grand_Est': [8, 10, 51, 52, 54, 55, 57, 67, 68, 88], 'Île-de-France': [75, 77, 78, 91, 92, 93, 94, 95], 'Normandie_(région_administrative)': [14, 27, 50, 61, 76], 'Hauts-de-France': [2, 59, 60, 62, 80], 'Corse': [20]}
prixRegions = DS.DictRegions("PrixCarburants_instantane.xml", d)
print(prixRegions)
