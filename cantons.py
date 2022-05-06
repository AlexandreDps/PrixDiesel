c = folium.Map(location=[46.232192999999995, 2.209666999999996], zoom_start=5)
can = "cantons.geojson"
folium.GeoJson(can, name="geojson").add_to(c)
