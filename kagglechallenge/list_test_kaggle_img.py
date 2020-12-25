# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 19:31:02 2020

@author: Carlos Pires
"""

import os
import cv2

images=os.listdir('./segmentation/airbus-ship-detection/input/test_v2/')
file_test = open('./testkaggle_v2.txt', 'w')  

for image in images:
    file_test.write( "../test_v2/" + image + "\n")

file_test.close()