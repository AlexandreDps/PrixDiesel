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
style = {'fillColor': '#228B22', 'color': '#228B22'}
herault = f"https://polygons.openstreetmap.fr/get_geojson.py?id=3792883&params=0"
folium.GeoJson(herault, name="geojson", style_function=lambda x:style).add_to(m)
