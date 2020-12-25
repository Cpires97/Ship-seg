# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 20:23:02 2020

@author: Carlos Pires
"""

import json
import cv2
import matplotlib.pyplot as plt
with open('./cropped_img_kaggle_v2_6000_th=0.0001.txt') as json_file:
    data = json.load(json_file)
 

for obj in data:
    filename=obj['filename']
    if filename=="00a3ab3cc.jpg":
        image, aux=filename.split(".")
        img =cv2.imread('../test_v2/'+image+'.jpg')
        height=768
        width=768
        bbs=obj['objects']
        for bb in bbs:
#            if bb['name']=="boat":
#                coordinates=bb['relative_coordinates']
#                x_center=coordinates['center_x']*width
#                y_center=coordinates['center_y']*height
#                w_boat=coordinates['width']*width
#                h_boat=coordinates['height']*height
            cv2.rectangle(img,(int(bb['x1']+40),int(bb['y1'])+20),(int(bb['x2']-40),int(bb['y2'])-20),(255,0,0), 3)
        #cv2.imwrite('./aaa.jpg', img)
        plt.figure()
        plt.imshow(img) 
        plt.show()