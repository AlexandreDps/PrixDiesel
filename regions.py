#install le module folium bg
pip install folium

#puis tu l'importes
import folium

#la j'affecte à la variable m une carte centrée sur la france
m = folium.Map(location=[46.232192999999995, 2.209666999999996], zoom_start=5)

#liste des identifiants OSM de chaque région
l = [8637, 3792883, 8654, 3792877, 3792878, 3792876, 4217435, 3793170]

for identifiant in l:
    region = f"https://polygons.openstreetmap.fr/get_geojson.py?id={identifiant}&params=0"
    folium.GeoJson(region, name="geojson").add_to(m)

'''
exemple changement couleur : utile pour après

là c'est l'occitanie avec comme couleur le veeeeeeeeeerttttttttt
color pour bordure et fillColor pour interieeeuurrr

style = {'fillColor': '#228B22', 'color': '#228B22'}
herault = f"https://polygons.openstreetmap.fr/get_geojson.py?id=3792883&params=0"
folium.GeoJson(herault, name="geojson", style_function=lambda x:style).add_to(m)
'''
