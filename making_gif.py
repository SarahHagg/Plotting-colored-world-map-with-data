# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 17:17:21 2020

@author: CRI User
"""
# =============================================================================
# 
# import os,sys
# import datetime
# import imageio
# from pprint import pprint
# import time
# import datetime
# e=sys.exit
#  
# years = ['2015-2020', '2010-2015', '2005-2010', '2000-2005', '1995-2000', '1990-1995', '1985-1990', '1980-1985', '1975-1980', '1970-1975', '1965-1970', '1960-1965', '1955-1960', '1950-1955']
# filenames_print = []
# for elem in years:
#     file = 'C:/Users/CRI User/Desktop/maps_gif/' + elem + '.png'
#     filenames_print.append(file)
# #C:/Users/CRI User/Desktop/maps_gif/1950-1955.png
# def create_gif(filenames, duration):
# 	images = []
# 	for filename in filenames:
# 		images.append(imageio.imread(filename))
# 	output_file = 'Gif-%s.gif' % datetime.datetime.now().strftime('%Y-%M-%d-%H-%M-%S')
# 	imageio.mimsave(output_file, images, duration=duration)
#  
#  
# # =============================================================================
# # if __name__ == "__main__":
# # 	script = sys.argv.pop(0)
# # 	duration = 0.2 
# # 	filenames = sorted(filter(os.path.isfile, [x for x in os.listdir() if x.endswith(".jpg")]), key=lambda p: os.path.exists(p) and os.stat(p).st_mtime or time.mktime(datetime.now().timetuple()))
# #  
# # =============================================================================
# create_gif(filenames_print, 1)
# =============================================================================


from PIL import Image, ImageDraw
import glob

frames = []
imgs = glob.glob("*.png")
for i in imgs:
    new_frame = Image.open(i)
    frames.append(new_frame)

frames[0]