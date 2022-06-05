# Prix Diesel France

<p>Ce projet utilise Jupyter Notebook et permet de récupérer les données 'instantanés' (mises à jour toutes les 10 minutes) afin d'afficher sur une carte de la france, le prix moyen de l'essence par canton, régions et départements.</p>

<p> Les données sont récupérées sur le <a href = "https://www.prix-carburants.gouv.fr/rubrique/opendata/">site du gouvernement français</a></p>
<p> Après téléchargement et décompression des fichiers xlml qui nous intéressent, on trie les données à l'aide d'Element Tree</p>
<p> Pour des informations plus détaillées, veuillez consulter le document <code><a href = "https://github.com/Alemanu211/PrixDiesel/blob/main/Projet%20ISOC631.pdf"> Projet ISOC631.pdf</a></code> présent dans le répertoire</p>


# Installation et utilisation

Modules nécessaires pour l'obtention des différentes cartes:
 *  <code>folium</code>
 *  <code>geojson</code>
 *  <code>json</code>
 *  <code>wget</code>
 *  <code>etree</code>
 *  <code>os</code>
 *  <code>zipfile</code>
 *  <code>datetime</code>
 *  <code>centroid</code> from <code>geojson_utils</code>
 *  <code>urlopen</code> from <code>urllib.request</code>


Pour pouvoir utiliser notre projet, il vous suffit de télecharger tout le répertoire ou de cloner le répertoire avec la commande suivante:
 * <code>git clone https://github.com/Alemanu211/PrixDiesel.git</code>

Ensuite, vous devez exécuter l'un des fichiers _.ipynb_, ils offrent tous un résultat différent :
 * Le fichier _question1.ipynb_ donne une carte de la France contenant 2000 stations-service
 * Le fichier _question2.ipynb_ ajoute des flèches de variation sur l'affichage du fichier précédent
 * Les fichiers _question3_cantons.ipynb_, _question3_departements.ipynb_ et _question3_regions.ipynb_ donne respectivement une carte du prix moyen du diesel avec les variations pour chaque canton, puis pour chaque département et enfin pour chaque région


# Exemple de résultat

Voici une des cartes obtenues lors de notre projet (fichier <a href = "https://github.com/Alemanu211/PrixDiesel/blob/main/question3_regions.ipynb">_question3_regions.ipynb_</a>), elle représente le prix moyen du diesel par région avec des flèches de variation :

![q3_reg_bis](https://user-images.githubusercontent.com/93133836/172074128-e99654d4-2b06-466d-8e37-cafbb2a3e184.PNG)


# Ressources utilisées

Récupérations des contours:
 * https://github.com/gregoiredavid/france-geojson

Aides pour l'affichage des cartes:
 * https://python-visualization.github.io/folium/quickstart.html
 * https://plotly.com/python/mapbox-county-choropleth/
 * https://towardsdatascience.com/folium-and-choropleth-map-from-zero-to-pro-6127f9e68564
 * centroid geojson : https://pypi.org/project/geojson_utils/
