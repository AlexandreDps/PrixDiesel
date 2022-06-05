# Prix Diesel France

<h4> Modules nécessaires : <code>folium</code>, <code>geojson</code>, <code>json</code>, <code>wget</code>, <code>etree</code>, <code>os</code>, <code>zipfile</code>, <code>datetime</code>, <code>centroid</code> from <code>geojson_utils</code>, <code>urlopen</code> from <code>urllib.request</code></h4>
<p>Projet jupyter notebook de qui permet de récupérer les données 'instantannées' (mises à jour toutes les 10 minutes) afin d'afficher sur une carte de la france, le prix moyen de l'essence par canton, régions et départements.</p>

<p> Les données sont récupérées sur le <a href = "https://www.prix-carburants.gouv.fr/rubrique/opendata/">site du gouvernement français</a></p>
<p> Après téléchargement et décompression des fichiers xlml qui nous intéressent, on trie les données à l'aide d'Element Tree</p>
<p> Pour des informations plus détaillées, veuillez consulter le document <code>Projet ISOC631.pdf</code> présent dans le répertoire</p>


# Exemple de résultat

Voici une des cartes obtenues lors de notre projet (<a href = "https://github.com/Alemanu211/PrixDiesel/blob/main/question3_regions.ipynb">fichier _question3_regions.ipynb_</a>), elle représente le prix moyen du diesel par région avec des flèches de variation :

![q3_reg_bis](https://user-images.githubusercontent.com/93133836/172074128-e99654d4-2b06-466d-8e37-cafbb2a3e184.PNG)


# Ressources utilisées

Récupérations des contours:
 * https://github.com/gregoiredavid/france-geojson

Aides pour l'affichage des cartes:
 * https://python-visualization.github.io/folium/quickstart.html
 * https://plotly.com/python/mapbox-county-choropleth/
 * https://towardsdatascience.com/folium-and-choropleth-map-from-zero-to-pro-6127f9e68564
 * centroid geojson : https://pypi.org/project/geojson_utils/
