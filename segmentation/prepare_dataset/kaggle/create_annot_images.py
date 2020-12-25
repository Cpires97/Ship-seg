# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 14:12:07 2020

@author: Carlos Pires
"""


import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
from skimage.morphology import label


import os
import cv2
import json
import random
from PIL import Image 

INPUT_DIR = './airbus-ship-detection/input/'
TRAIN_DATA_PATH = os.path.join(INPUT_DIR, 'train_v2')
TRAIN_SHIP_SEGMENTATIONS_PATH = os.path.join(INPUT_DIR, 'train_ship_segmentations_v2.csv')

IMAGE_WIDTH = 768
IMAGE_HEIGHT = 768
SHAPE = (IMAGE_WIDTH, IMAGE_HEIGHT)

masks = pd.read_csv(TRAIN_SHIP_SEGMENTATIONS_PATH)
masks.head()


def rle_decode(mask_rle, shape=SHAPE):

    s = mask_rle.split()
    starts, lengths = [np.asarray(x, dtype=int) for x in (s[0::2], s[1::2])]
    starts -= 1
    ends = starts + lengths
    img = np.zeros(shape[0]*shape[1], dtype=np.uint8)
    for lo, hi in zip(starts, ends):
        img[lo:hi] = 1
    return img.reshape(shape).T



def masks_as_image(in_mask_list, shape=SHAPE):
    all_masks = np.zeros(shape, dtype = np.int16)
    for mask in in_mask_list:
        if isinstance(mask, str):
            all_masks += rle_decode(mask)
    print(all_masks.shape)
    return np.expand_dims(all_masks, -1), all_masks



images=os.listdir('./airbus-ship-detection/input/train_seg4/images/')
d=0
for image in images:    
#    fig, axarr = plt.subplots(1, 2, figsize = (10, 5))
#    img_0 = imread(os.path.join(TRAIN_DATA_PATH, '00021ddc3.jpg'))
#    axarr[0].imshow(img_0)
#    axarr[0].set_title('00021ddc3.jpg')
    name_img,ext=image.split('.')
    rle_1 = masks.query('ImageId=="{}"'.format(image))['EncodedPixels']
    #print(rle_1)
    img_1, all_masks = masks_as_image(rle_1)  
    
#    axarr[1].imshow(img_1[:, :, 0])
#    axarr[1].set_title('Ship Mask')
    
#    plt.show()
#    plt.figure()
#    plt.imshow(all_masks)
    all_masks = np.array(all_masks)
#    all_masks[all_masks == 0] = 2
#    all_masks[all_masks == 1] = 0
#    all_masks[all_masks == 2] = 1 
    
    im = Image.fromarray(all_masks)     
    im.save('./airbus-ship-detection/input/train_seg4/labels/'+name_img+'.png')
#    d+=1
#    if d>5:
#        break