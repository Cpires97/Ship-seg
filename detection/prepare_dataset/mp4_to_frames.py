# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 11:54:26 2020

@author: Carlos Pires
"""

# Importing all necessary libraries 
import cv2 
import os 
  
# Read the video from specified path 
video=input("name video:")
cam = cv2.VideoCapture("./test_videos/videos/"+video) 
  
#try: 
#      
#    # creating a folder named data 
#    if not os.path.exists('data'): 
#        os.makedirs('data') 
#  
## if not created then raise error 
#except OSError: 
#    print ('Error: Creating directory of data') 
  
# frame 
currentframe = 0
img, aux=video.split('.')

while(True): 
      
    # reading from frame 
    ret,frame = cam.read() 
  
    if ret: 
        # if video is still left continue creating images 
        if currentframe <300:
            name = './test_videos/videos/clip/' + img+'_frame'+str(currentframe) + '.jpg'
            print ('Creating...' + name) 
      
            # writing the extracted images 
            cv2.imwrite(name, frame) 
      
            # increasing counter so that it will 
            # show how many frames are created 
        currentframe += 1
    else: 
        break
  
# Release all space and windows once done 
cam.release() 
#cv2.destroyAllWindows() 

