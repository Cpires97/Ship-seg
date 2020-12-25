# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 14:12:41 2020

@author: Carlos Pires
"""

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
from skimage.morphology import label
from skimage.data import imread

import os

import json


from PIL import Image 

def get_points(annot):
    points=[]
    shapes=annot['shapes']
    for obj in shapes:
        points.append(np.asarray(obj['points']))
    return points

def get_boat_bb(bb):
    list_min_max=[]
    for obj in bb:
        #print(min(obj[:,1]))
        list_min_max.append({"x1":int(min(obj[:,0])), "x2":int(max(obj[:,0])), "y1":int(min(obj[:,1])), "y2":int(max(obj[:,1]))})
    
    return list_min_max

images=os.listdir('./annot_images2/')
labels=os.listdir('./data_annotated2/')
list_bb=[]
points=[]
d=0

list_bb=[]
for image in images:
    if os.path.exists('./data_annotated2/'+image+'.json'):        
        with open('./data_annotated2/'+image+'.json') as json_file:
            annot = json.load(json_file)
        list_points=get_points(annot)
        list_min_max=get_boat_bb(list_points)
        list_bb.append({"filename": image+'.jpg', "objects": list_min_max})
    else:
        list_bb.append({"filename": image, "objects": []})

with open('./groundtruth_bb2.txt', 'w') as outfile:
    json.dump(list_bb, outfile)    
    
    
    
    
    
