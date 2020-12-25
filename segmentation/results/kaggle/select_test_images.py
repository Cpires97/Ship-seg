# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 11:04:25 2020

@author: Carlos Pires
"""
import os
import cv2

images=os.listdir('./airbus-ship-detection/input/train_v2/')

train_images=os.listdir('./airbus-ship-detection/input/detection/train1/labels_train/')
train_images2=os.listdir('./airbus-ship-detection/input/detection/train2/labels_train/')

images2=os.listdir('./airbus-ship-detection/input/test_results2/test_images/')

images3=os.listdir('./airbus-ship-detection/input/test_segmentation/images/')

train_seg2=os.listdir('./airbus-ship-detection/input/train_seg2/images/')

file_test = open('./airbus-ship-detection/input/train_seg4/trainsegkaggle4.txt', 'w')  
d=0
for image in images:
    name_img, ext=image.split('.')
    if name_img+".txt" in train_images or name_img+".txt" in train_images2 or image in images2 or image in images3 or image in train_seg2:
        continue
    else:
        file_test.write( "../train_seg4/" + image + "\n")
        img =cv2.imread('./airbus-ship-detection/input/train_v2/'+image)
        cv2.imwrite('./airbus-ship-detection/input/train_seg4/images/'+image, img)
        d=d+1
        if d==20000:
            break
    
file_test.close()