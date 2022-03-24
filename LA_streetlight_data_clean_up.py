"""
this script takes the publicly available LA streetlight data and "cleans" it up:
(1) Lamp info is split into wattage and type for ease of reference
(2) Lamp locations are matched to census tracts

census tract shapefiles were taken from here: https://geohub.lacity.org/datasets/lacounty::census-tracts-2020/about
street light data was taken from the publicly available data set here: https://geohub.lacity.org/datasets/5e7c617cd8c141308c79024baa2ffcae_0/about


"""
import numpy as np
import pandas as pd
import geopandas as gpd
import os

from tqdm import tqdm

from shapely.ops import cascaded_union

import matplotlib.pyplot as plt

#read in tract info
path_to_LA = "./LA_Census_Tracts_2020/Census_Tracts_2020.shp"
LA_tracts = gpd.read_file(path_to_LA)
LA_tracts = LA_tracts.rename(index = LA_tracts.CT20)

#read the streetlight data
path_to_LA_lights = "./LA_Street_Lights_init/Street_Lights.shp"
LA_lights = gpd.read_file(path_to_LA_lights)

#first, split up lamp info into wattage and type
lamp_names = ["LAMPA","LAMPB","LAMPC","LAMPD","LAMPE","LAMPF"]

#for each lamp variable
for l_name in lamp_names:

    temp_wattage = []
    temp_type = []

    #loop through all rows
    for iidx, rrow in tqdm(LA_lights.iterrows()):
        temp = LA_lights.loc[iidx]
        if temp[l_name] is not None:
            l_watt = float(temp[l_name].split()[0].split("W")[0])
            l_type = temp[l_name].split()[1]

            temp_wattage.append(l_watt)
            temp_type.append(l_type)
        else:
            temp_wattage.append(None)
            temp_type.append(None)

    #add data to the dataframe
    LA_lights[l_name+"_wattage"] = temp_wattage
    LA_lights[l_name+"_type"] = temp_type

# match streetlights to tracts
## warning, slow
l_tracts = []
for iidx, rrow in tqdm(LA_lights.iterrows()):
    temp_val = None
    for idx,row in LA_tracts.iterrows():
        if row.geometry.contains(rrow.geometry):
            temp_val = row.CT20
            break
    l_tracts.append(temp_val)

LA_lights["CT20"] = l_tracts

LA_lights.to_file("./LA_Street_lights/LA_Street_lights.shp")

#test that everything wrote correctly
new_LA_lights = gpd.read_file("./LA_Street_lights/LA_Street_lights.shp")
