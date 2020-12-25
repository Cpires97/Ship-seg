# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 11:19:51 2020

@author: Carlos Pires
"""

import os
import json
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

from PIL import Image 

def save_images(arr_annot, annot):
    annot_im = Image.fromarray(arr_annot)
    annot_im.save('./airbus-ship-detection/input/train_seg4/cut_annot_balanced/'+annot)
    
    img=Image.open('./airbus-ship-detection/input/train_seg4/cut_images/'+annot)
    img2=img.copy()
    img2.save('./airbus-ship-detection/input/train_seg4/cut_images_balanced/'+annot)

annots=os.listdir('./airbus-ship-detection/input/train_seg4/cut_annot/')
d=0
num_boats=0
bb_queue=0
for annot in annots:
    annot_img=Image.open('./airbus-ship-detection/input/train_seg4/cut_annot/'+annot)
    arr_annot = np.array(annot_img)
    if np.sum(arr_annot)!=0:
        num_boats+=1
        save_images(arr_annot, annot)
        bb_queue+=1
    else:
        if bb_queue>0:
            bb_queue-=1
            save_images(arr_annot, annot)
        