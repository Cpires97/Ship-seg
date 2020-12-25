# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 18:38:18 2020

@author: Carlos Pires
"""

import cv2
import os

image_folder = 'clip_results'
video_name = 'detec_clip.avi'

images=os.listdir('./clip_results')

frame = cv2.imread(os.path.join(image_folder, 'test_2015-04-22-18-29-31_tase_frame0.jpg'))
height, width, layers = frame.shape

video = cv2.VideoWriter(video_name, 0, 30, (width,height))
i=0
for image in images:
    video.write(cv2.imread('./clip_results/test_2015-04-22-18-29-31_tase_frame'+str(i)+'.jpg'))
    i+=1

cv2.destroyAllWindows()
video.release()