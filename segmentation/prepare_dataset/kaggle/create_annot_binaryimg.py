# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 19:53:56 2020

@author: Carlos Pires
"""

import os
import json
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

from PIL import Image 



#test_img=cv2.imread('../segmentation/u_net_example/data/CamVid/trainannot/0001TP_006690.png')
#test_img_2=Image.open('../segmentation/u_net_example/data/CamVid/trainannot/0001TP_006690.png')
#test2=cv2.imread('./trainannot/2015-04-22-16-28-36_jai_eo_frame0.png')
#test3 = Image.open('./trainannot/2015-04-22-18-29-31_tase_frame0.png')  
#arr = np.array(test3)



d=0

images=os.listdir("./cut_annot/")  
for image in images: 
    #img_name=image.split('.') 
#    if os.path.isfile('./data_annotated/'+img_name[0] +'.json')==True:
#        with open('./data_annotated/'+img_name[0] +'.json') as json_file:
#            img_json = json.load(json_file)
##        img =cv2.imread('./images/'+image)
##        ann_img = np.zeros(img.shape).astype('uint8')
##        ann_img[ann_img == 0] = 1
#        ann_img=np.zeros((img_json['imageHeight'],img_json['imageWidth'])).astype('uint8')  
#        shapes=img_json['shapes']
#        for i in shapes:
#            points=i['points']
#            for point in points:
#                ann_img[int(point[1])][int(point[0])]=1
    
    img=Image.open('./cut_annot/'+image)
#    img = img.convert("L") 
    arr_img = np.array(img)
    arr_img[arr_img == 0] = 2
    arr_img[arr_img == 1] = 0
    arr_img[arr_img == 2] = 1   
    im = Image.fromarray(arr_img)
    im.save('./cut_annot/'+image)

#images=os.listdir("./validannot/")  
#for image in images: 
#    #img_name=image.split('.') 
##    if os.path.isfile('./data_annotated/'+img_name[0] +'.json')==True:
##        with open('./data_annotated/'+img_name[0] +'.json') as json_file:
##            img_json = json.load(json_file)
###        img =cv2.imread('./images/'+image)
###        ann_img = np.zeros(img.shape).astype('uint8')
###        ann_img[ann_img == 0] = 1
##        ann_img=np.zeros((img_json['imageHeight'],img_json['imageWidth'])).astype('uint8')  
##        shapes=img_json['shapes']
##        for i in shapes:
##            points=i['points']
##            for point in points:
##                ann_img[int(point[1])][int(point[0])]=1
#    
#    img=Image.open('./validannot/'+image)
#    img = img.convert("L") 
#    arr_img = np.array(img)
#    arr_img[arr_img == 0] = 2
#    arr_img[arr_img == 1] = 0
#    arr_img[arr_img == 2] = 1   
#    im = Image.fromarray(arr_img)
#    im.save('./validannot/'+image)