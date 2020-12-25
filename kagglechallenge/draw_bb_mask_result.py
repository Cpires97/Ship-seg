# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 20:54:44 2020

@author: Carlos Pires
"""

import json
import cv2
import os
from PIL import Image 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 


results=os.listdir('./results_train_seg4_focal_weighteddl__batch8_1_densenet121_50epochs/')

filename='00a3ab3cc.jpg'
matches = [x for x in results if x.split('_')[0] == filename.split('.')[0]]

for obj in matches:
    with open('./results_train_seg4_focal_weighteddl__batch8_1_densenet121_50epochs/'+obj) as json_file:
        bb_file = json.load(json_file)
        
    bb_pr_mask=np.asarray(bb_file['pr_mask'],dtype=np.uint8)
    im = Image.fromarray(bb_pr_mask.squeeze())
    plt.figure()
    plt.imshow(im) 
    plt.show()