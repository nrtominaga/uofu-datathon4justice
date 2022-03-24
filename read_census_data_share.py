"""
json reader
"""

import numpy as np
import pandas as pd
import os
import geopandas

from tqdm import tqdm

import matplotlib.pyplot as p

import time

#your API key would go here
#for information on using the census API and getting a key, see the guide here:
#https://www.census.gov/data/developers/guidance/api-user-guide.Example_API_Queries.html
API_key = ""

#API_name = "https://api.census.gov/data/2020/acs/acs5/profile"

#starting the data processing
time1 = time.time()

#DP02 from 0001 to 0152
#DP03 from 0001 to 0137
#DP04 from 0001 to 0141
#DP05 from 0001 to 0081
variables = []
variable_sizes = [154,138,144,90]

for ii in range(2,6):
  for kk in range(1,variable_sizes[ii-2]):
    write_str_list = [0,0,0,0]
    write_str = ""
    for jj in range(len(str(kk))):
      write_str_list[-jj - 1] = int(str(kk)[-jj-1])
    for jj in write_str_list:
      write_str = write_str + str(jj)

    variables.append("DP0" + str(ii) + "_" + write_str + "E")

# Salt lake county, UT -> 49, 035
# LA county, CA -> 06, 037
API_name = "https://api.census.gov/data/2020/acs/acs5/profile?get=" + variables[0] + "&for=tract:*&in=county:037&in=state:06" + "&key=" + API_key
df = pd.read_json(path_or_buf = API_name)
df = df.rename(columns = df.iloc[0])
df = df.drop(index=0)


for v_name in tqdm(variables[1:]):
  API_name = "https://api.census.gov/data/2020/acs/acs5/profile?get=" + v_name + "&for=tract:*&in=county:037&in=state:06" + "&key=" + API_key

  new_df = pd.read_json(path_or_buf = API_name)
  new_df = new_df.drop(columns=[1,2])
  new_df = new_df.rename(columns = new_df.iloc[0])
  new_df = new_df.drop(index=0)


  df = pd.merge(df,new_df,on="tract")

#done with the processing
time2 = time.time()

print("time to compute was:" + f"{time2-time1:.2f}")

#read in each individual variable?
save_fp = "./census_data_2020_LA.csv"
df.to_csv(path_or_buf = save_fp)
