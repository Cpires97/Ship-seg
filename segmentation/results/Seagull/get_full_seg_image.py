# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 12:06:23 2020

@author: Carlos Pires
"""


import json
import cv2
import os
from PIL import Image 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
from skimage.morphology import binary_opening, disk, label

def get_bb_position(list_bb, bb_id):
    for a in list_bb:
        if a['id']==int(bb_id):
            return a
        
#def rle_encode(img):
#    '''
#    img: numpy array, 1 - mask, 0 - background
#    Returns run length as string formated
#    '''
#    pixels = img.flatten()
#    print(len(pixels))
#    pixels = np.concatenate([[0], pixels, [0]])
#    runs = np.where(pixels[1:] != pixels[:-1])[0] + 1
#    runs[1::2] -= runs[::2]
#    return ' '.join(str(x) for x in runs)
    

def multi_rle_encode(img, **kwargs):
    '''
    Encode connected regions as separated masks
    '''
    labels = label(img)
    if img.ndim > 2:
        return [rle_encode(np.sum(labels==k, axis=2), **kwargs) for k in np.unique(labels[labels>0])]
    else:
        return [rle_encode(labels==k, **kwargs) for k in np.unique(labels[labels>0])]

# ref: https://www.kaggle.com/paulorzp/run-length-encode-and-decode
def rle_encode(img, min_max_threshold=1e-3, max_mean_threshold=None):
    '''
    img: numpy array, 1 - mask, 0 - background
    Returns run length as string formated
    '''
    if np.max(img) < min_max_threshold:
        return '' ## no need to encode if it's all zeros
    if max_mean_threshold and np.mean(img) > max_mean_threshold:
        return '' ## ignore overfilled mask
    pixels = img.T.flatten()
    pixels = np.concatenate([[0], pixels, [0]])
    runs = np.where(pixels[1:] != pixels[:-1])[0] + 1
    runs[1::2] -= runs[::2]
    return ' '.join(str(x) for x in runs)

def pred_encode(img,mask, **kwargs):
    cur_rles = multi_rle_encode(mask, **kwargs)
    return [[img, rle] for rle in cur_rles ]



with open('./cropped_img_clip_v2_6000_th=0.0001.txt') as json_file:
    cropped_img = json.load(json_file)
    
results=os.listdir('./seg_results/')
d=0

output_pred=[]


for image in cropped_img:    
    img=Image.open('./clip_images/'+image['filename'])
    mask= np.zeros((img.size[1],img.size[0]),dtype=np.uint8)
    
    matches = [x for x in results if x.rsplit('_',1)[0] == image['filename'].split('.')[0]]
    
    for obj in matches:
        with open('./seg_results/'+obj) as json_file:
            bb_file = json.load(json_file)
            
        bb_pr_mask=np.asarray(bb_file['pr_mask'],dtype=np.uint8)
        
        bb_position=get_bb_position(image['objects'], obj.rsplit('_',1)[1].split('.')[0])
        
        width=bb_position['x2']- bb_position['x1']
        height=bb_position['y2']- bb_position['y1']
        
        im = Image.fromarray(bb_pr_mask.squeeze())
        im=im.resize((int(width),int(height))) 
        
        bb_pr_mask=np.asarray(im)
        
        for y in  range(0,int(height)-1):
            for x in range(0, int(width)-1):
                if int(bb_position['x1'])+x >= img.size[0]:
                    continue
                elif int(bb_position['y1'])+y >= img.size[1]:
                    continue
                else:
                    mask[int(bb_position['y1'])+y][int(bb_position['x1'])+x]=bb_pr_mask[y][x]*255
#    plt.figure()
#    plt.imshow(mask)
#    plt.figure()
#    plt.imshow(img)
                    
#    if np.sum(mask)==0:
#        output_pred.append([image['filename'], ''])
#    else:
#        output_pred += pred_encode(image['filename'], mask, min_max_threshold=1.0)
    #mask_rle=rle_encode(mask)
    #output_pred.append([image['filename'], mask_rle])
    
    cv2.imwrite('./full_image_seg/test_'+image['filename'], mask)
    
#    d+=1
#    if d>2:
#        break
    
    
#df = pd.DataFrame(output_pred) 
#df.columns = ['ImageId', 'EncodedPixels']
#
#print(df.head())
#
#df.to_csv('test1.csv',index=False)
