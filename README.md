


# Prix Diesel France

<h4> Modules necessaires : <code>wget</code>, <code>etree</code>, <code>os</code>, <code>zipfile</code>, <code>datetime</code> </h4>
<p>Projet jupyter notebook de qui permet de récupérer les données 'instantannées' (mises à jour toutes les 10 minutes) afin d'afficher sur une carte de la france, le prix moyen de l'essence par canton, régions et départements.</p>

<p> Les données sont récupérées sur le <a href = "https://www.prix-carburants.gouv.fr/rubrique/opendata/">site du gouvernement français</a></p>
<p> Après téléchargement et décompression des fichiers xlml qui nous intéressent, on trie les données à l'aide d'Element Tree</p>
<p> Pour des informations plus détaillées, veuillez consulter le document <code>Projet ISOC631.pdf</code> présent dans le répertoire</p>


# Ressources importantes (Carte folium)
Récupération des ID:
  * https://www.openstreetmap.org/#map=8/44.064/2.543

Récupérations des polygones :
  * https://polygons.openstreetmap.fr/

Contours:
 * https://github.com/gregoiredavid/france-geojson

Help dessin carte moyenne/variation:
 * https://python-visualization.github.io/folium/quickstart.html
 * https://www.python-graph-gallery.com/map-read-geojson-with-python-geopandas
 * https://www.python-graph-gallery.com/choropleth-map-geopandas-python
 * https://plotly.com/python/mapbox-county-choropleth/
 * https://towardsdatascience.com/folium-and-choropleth-map-from-zero-to-pro-6127f9e68564
