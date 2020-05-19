# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 13:15:47 2020

@author: Sarah Haggenmüller
"""

import pandas as pd #used to read in the revenue file 
import matplotlib.pyplot as plt #for plotting
#to read in shape file and provides high #level interface with #matplotlib library for making maps
import geopandas as gpd
import mapclassify
import descartes

world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

data = pd.read_csv('C:/Users/CRI User/Downloads/DP_LIVE_21042020123922326.csv').astype(str)

#indexNames = data[(data['TIME'] == '1960')].index


worldshort = world['continent'] == 'Africa'
worldplot = pd.DataFrame(world[worldshort], columns = ['pop_est', 'continent', 'name', 'iso_a3', 'gdp_md_est', 'geometry'] )
 
early = data['TIME'] == '1960'
worldearly = pd.DataFrame(data[early], columns = ['LOCATION', 'INDICATOR', 'SUBJECT', 'MEASURE', 'FREQUENCY', 'TIME',
       'Value', 'Flag Codes'])


late = data['TIME'] == '2010'
worldlate = pd.DataFrame(data[late], columns = ['LOCATION', 'INDICATOR', 'SUBJECT', 'MEASURE', 'FREQUENCY', 'TIME',
       'Value', 'Flag Codes'])
#print(data[early])
#dfObj.drop(indexNames , inplace=True)


for_plotting = world.merge(worldlate, left_on = 'iso_a3', right_on = 'LOCATION')

#print(worldearly)


ax = for_plotting.dropna().plot(column='Value', cmap =    
                                'Greys', figsize=(15,9),   
                                 scheme='quantiles', k=100, legend =  
                                  True)
ax.get_legend().remove()
ax.set_axis_off()

#print(world.info)
#print(data.info)

#pd.set_option('display.max_rows', None)

# print(worldgood)
# print(worldgood.info)
plt.savefig('map_3.png', dpi=300)


print(world.columns)
print(data.columns)

print(worldearly.shape)
print(worldlate.shape)
print(data.shape)

print(world['continent'])

print(data.info)
print(world.info)