# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 19:00:44 2020

@author: Carlos Pires
"""

import json
from PIL import Image
with open('./results_seagull6000/cropped_img_seagull6000_th=0.00001.txt') as json_file:
    data = json.load(json_file)
p_area=0    
for obj in data:
    image=obj['filename']
    img=Image.open('./images/'+image)
    width, height = img.size
    area=width*height
    area_bb=0
    for bb in obj['objects']:
        area_bb=area_bb+(bb['x2']-bb['x1'])*(bb['y2']-bb['y1'])
    
    p_area=p_area+area_bb/area
    
p_area_final=p_area/len(data)*100
print(p_area_final)