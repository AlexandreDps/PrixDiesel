#install le module folium bg
pip install folium

#puis tu l'importes
import folium

#la j'affecte à la variable m une carte centrée sur la france
m = folium.Map(location=[46.232192999999995, 2.209666999999996], zoom_start=5)

#là je trace le contour de la région aquitaine
aquitaine = f"https://polygons.openstreetmap.fr/get_geojson.py?id=8637&params=0"
folium.GeoJson(aquitaine, name="geojson").add_to(m)

#là c'est l'occitanie avec comme couleur le veeeeeeeeeerttttttttt
# color pour bordure et fillColor pour interieeeuurrr
style = {'fillColor': '#228B22', 'color': '#228B22'}
herault = f"https://polygons.openstreetmap.fr/get_geojson.py?id=3792883&params=0"
folium.GeoJson(herault, name="geojson", style_function=lambda x:style).add_to(m)

paca = f"https://polygons.openstreetmap.fr/get_geojson.py?id=8654&params=0"
folium.GeoJson(paca, name="geojson").add_to(m)

ara = f"https://polygons.openstreetmap.fr/get_geojson.py?id=3792877&params=0"
folium.GeoJson(ara, name="geojson").add_to(m)

bfc = f"https://polygons.openstreetmap.fr/get_geojson.py?id=3792878&params=0"
folium.GeoJson(bfc, name="geojson").add_to(m)

ge = f"https://polygons.openstreetmap.fr/get_geojson.py?id=3792876&params=0"
folium.GeoJson(ge, name="geojson").add_to(m)

hdf = f"https://polygons.openstreetmap.fr/get_geojson.py?id=4217435&params=0"
folium.GeoJson(hdf, name="geojson").add_to(m)

norm = f"https://polygons.openstreetmap.fr/get_geojson.py?id=3793170&params=0"
folium.GeoJson(norm, name="geojson").add_to(m)
