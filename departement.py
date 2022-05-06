d = folium.Map(location=[46.232192999999995, 2.209666999999996], zoom_start=5)
dep = "departement.geojson"
folium.GeoJson(dep, name="geojson").add_to(d)
