# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 11:43:54 2020

@author: Carlos Pires
"""

import json
import cv2

with open('./test_videos/videos/resultclip_th=0.0001.txt') as json_file:
    data = json.load(json_file)
 

for obj in data:
    filename=obj['filename']
    aux,aux1,aux2, image=filename.split("/")
    img =cv2.imread('./test_videos/videos/clip/'+image)
    height,width,channels = img.shape
    bbs=obj['objects']
    for bb in bbs:
        if bb['name']=="boat":
            coordinates=bb['relative_coordinates']
            x_center=coordinates['center_x']*width
            y_center=coordinates['center_y']*height
            w_boat=coordinates['width']*width
            h_boat=coordinates['height']*height
            cv2.rectangle(img,(int(x_center-w_boat/2),int(y_center-h_boat/2)),(int(x_center+w_boat/2),int(y_center+h_boat/2)),(255,255,0), 2)
    cv2.imwrite('./test_videos/videos/clip_results/test_'+image, img)
        