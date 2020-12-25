# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 15:37:46 2020

@author: Carlos Pires
"""

import os
import json
import cv2
import numpy as np

import os
#run the command inside the folder that we want to save the annotated images!!!!!

images=os.listdir("../images2/")
print(len(images))

d=0
for image in images:  
    img_name=image.split('.') 
    if os.path.isfile('../data_annotated2/'+img_name[0] +'.json')==True:
        cmd='labelme_json_to_dataset'+' ../data_annotated2/'+img_name[0] +'.json' +' -o '+ img_name[0]  
        os.system(cmd)
    else:
        img =cv2.imread('../images2/'+image)
        
        ann_img = np.zeros((img.shape[0],img.shape[1])).astype('uint8')
        #ann_img[ann_img == 0] = 1
        os.system('mkdir '+img_name[0])
        cv2.imwrite( './'+ img_name[0]+'/label.png' ,ann_img )
    