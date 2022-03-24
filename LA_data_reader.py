"""
initial data analysis of the uofu datathon4justice data
"""
import numpy as np
import pandas as pd
import geopandas as gpd

from tqdm import tqdm

import matplotlib.pyplot as plt

#read all the data
path_to_LA = "./LA_Census_Tracts_2020/Census_Tracts_2020.shp"
LA_tracts = gpd.read_file(path_to_LA)
LA_tracts = LA_tracts.rename(index = LA_tracts.CT20)

#read the streetlight data
path_to_LA_lights = "./LA_Street_lights/LA_Street_lights.shp"
LA_lights = gpd.read_file(path_to_LA_lights)


#read in census data, add it to the tracts
read_path =  "./census_data_2020_LA.csv"
df = pd.read_csv(read_path).drop(columns = "Unnamed: 0")
df = df.astype({"county":"str","state":"str","tract":"str"})
df = df.rename(index = df.tract)
df = df.drop(columns = ["county","state","tract"])
df[df<0] = np.nan

LA_tracts = pd.concat([LA_tracts,df],axis=1)

#plot things to make sure all is well
fig,ax = plt.subplots()

LA_tracts.plot(ax=ax,column = "DP03_0063E",edgecolor = "black")
LA_lights.plot(ax=ax,color = "red", marker = ".",markersize = 2,alpha = 0.2)
plt.show()

#try aggregating light data
num_lights = []
avg_wattage = []

#note: this computation took my 2020 macbook pro ~10 minutes
for idx, row in tqdm(LA_tracts.iterrows()):
  #print(f"row idx is {idx}")
  light_idx = LA_lights.CT20 == idx

  #get the number of lights
  temp_num = sum(light_idx)
  num_lights.append(temp_num)

  #get the average value for these lights
  temp_avg = LA_lights[light_idx & (LA_lights.LAMPA_watt > 0)].LAMPA_watt.mean()
  avg_wattage.append(temp_avg)

print("number of lights: ")
print(num_lights)
#don't forget to add this array to the dataframe
LA_tracts["num_lights"] = num_lights

print("average wattage: ")
print(avg_wattage)
#don't forget to add this array to the dataframe
LA_tracts["avg_wattage"] = avg_wattage

#now let's plot each, the counts and then the wattage 
fig, ax = plt.subplots(ncols = 2)

LA_tracts.plot(ax=ax[0],column = "avg_wattage",edgecolor="black",
                legend = True,legend_kwds={'label': "Avg. Wattage",'orientation': "horizontal"})
LA_tracts.plot(ax=ax[1],column = "num_lights",edgecolor="black",
                legend = True,legend_kwds={'label': "Num. lights",'orientation': "horizontal"})

plt.show()
