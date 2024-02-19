# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 15:43:46 2024

@author: halde
"""

import geopandas as gpd

# Path to your GeoJSON file
geojson_file = 'C:\Suvankar\Delhi_BFP_GEE\Google_BFP_GJSON.geojson'

# Read GeoJSON file
gdf = gpd.read_file(geojson_file)

# Path for the output Shapefile
shapefile_output = 'C:\Suvankar\Delhi_BFP_GEE\Delhi_BPF_GEE.shp'

# Save GeoDataFrame to Shapefile
gdf.to_file(shapefile_output, driver='ESRI Shapefile')
