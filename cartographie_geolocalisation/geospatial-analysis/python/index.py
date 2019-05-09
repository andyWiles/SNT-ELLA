import folium
import webbrowser

# Create a map centered at the given latitude and longitude
stations_map = folium.Map(location=[45,1], zoom_start=5)
# Add data from a geojson file
stations_map.add_child(folium.GeoJson('data/postesNivo.json'))
# Display the map

stations_map.save("map.html")
#webbrowser.get().open("file:///Users/scscjcnc/Desktop/PYTHON/geospatial-analysis-2/python/map.html")


import geopandas as gpd

# Read the geolocalised data
stations = gpd.read_file('data/postesNivo.json')
# Convert the IDs to int
stations.ID = stations.ID.astype(int)
print(stations.head())
stations.plot()