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
import numpy as np
import descartes

world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))


# print(world.head)
print(world.columns)



data = pd.read_csv('C:/Users/CRI User/Desktop/UNdata_Export_20200421_160539513.csv').astype(str)
print(data.columns)

years = ['2015-2020', '2010-2015', '2005-2010', '2000-2005', '1995-2000', '1990-1995', '1985-1990', '1980-1985', '1975-1980', '1970-1975', '1965-1970', '1960-1965', '1955-1960', '1950-1955']

for elem in years:
    vmin = -10
    vmax = 8
    yearly = data['Year(s)'] == elem
    yearlydata = pd.DataFrame(data[yearly], columns =['Country or Area', 'Year(s)', 'Variant', 'Value'])

    for_plotting = world.merge(yearlydata, left_on = 'name', right_on = 'Country or Area')
# =============================================================================
#     ax = for_plotting.dropna().plot(column='Value', cmap = 'copper_r', alpha = 0.95, figsize=(15,9),   
#                                   scheme='quantiles', legend = True, k=10, norm=plt.Normalize(vmin=vmin, vmax=vmax))
#     ax.set_title('Le taux de fécondité 1950-2015')
#     ax.annotate(elem, xy=(0.65, .225), xycoords='figure fraction',
#             horizontalalignment='left', verticalalignment='top')
#     #ax.get_legend().remove()
# =============================================================================
    #ax.get_legend()
    # mylabels = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    # ax.legend(handles = mylabels, labels=mylabels)
#    ax.set_axis_off()

# =============================================================================
# 
#     # pd.set_option('display.max_rows', None)
#     for_plotting['Value'].fillna(value='nan', inplace=True)
#     
#     keys = list(for_plotting['Value'].unique())
#     color_range = list(np.linspace(0, 1, len(keys), endpoint=False))
#     colors = [cm.tab20b(x) for x in color_range]
#     color_dict = dict(zip(keys, colors))
#     color_dict['No data'] = 'lightgray'
# 
# 
# =============================================================================


    vmin, vmax = 120, 220
    # create figure and axes for Matplotlib
    fig, ax = plt.subplots(1, figsize=(10, 6))
#    The stage has been set. Map time.
    # create map
    
    merged = world.set_index('name').join(yearlydata.set_index('Country or Area'))
    
    merged['Value'].plot(cmap='copper', linewidth=0.8, ax=ax)
        

print(marged['Value'])
# print(worldgood)
# print(worldgood.info)
    #plt.savefig('C:/Users/CRI User/Desktop/maps_gif/' + elem + '.png', dpi=300)

    
early = data['Year(s)'] == '1960-1965'
earlydata = pd.DataFrame(data[early], columns =['Country or Area', 'Year(s)', 'Variant', 'Value'])


late = data['Year(s)'] == '2010-2015'
latedata = pd.DataFrame(data[late], columns =['Country or Area', 'Year(s)', 'Variant', 'Value'])

# better = world['name'].rename({"Côte d'Ivoire": "Cote d'Ivoire"}, inplace = True)

# worldgood = pd.DataFrame(better, columns = ['pop_est', 'continent', 'name', 'iso_a3', 'gdp_md_est', 'geometry']) 

# =============================================================================
# vmin = 0.5
# vmax = 7
# for_plotting = world.merge(earlydata, left_on = 'name', right_on = 'Country or Area')
# #print(for_plotting)

#%%

# ax = for_plotting.dropna().plot(column='Value', cmap =    
#                                 'Greys', figsize=(15,9),   
#                                   scheme='quantiles', k=10, legend =  
#                                   True)
# #ax.get_legend().remove()
# ax.set_axis_off()


# pd.set_option('display.max_rows', None)

# print(worldgood)
# print(worldgood.info)
#plt.savefig('map_continent_early-leg.png', dpi=300)

print(world.columns)
#print(world['name'])
# =============================================================================
#print(world['name'])