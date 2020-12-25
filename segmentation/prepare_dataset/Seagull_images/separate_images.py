from PIL import Image 
import shutil
import numpy as np



f_train = open("./train.txt", "r")
l_train=f_train.readlines()

for line in l_train:
    img_name, ext = line.split('.')
    img = Image.open('./cut_images/'+img_name+'.jpg')  
    # make a copy the image so that the  
    # original image does not get affected 
    img2 = img.copy() 
    img2.save('./train/'+img_name+'.png')
    
    img3 = Image.open('./cut_annot/'+img_name+'.png')
    
    img4=img3.copy()
    
    img4.save('./trainannot/'+img_name+'.png')    
    #shutil.copyfile('./labels/'+name+'.txt', './labels_train/'+name+'.txt')
    
    

f_test = open("./valid.txt", "r")
l_test=f_test.readlines()

for line in l_test:
    img_name, ext = line.split('.')    

    img = Image.open('./cut_images/'+img_name+'.jpg')  
    # make a copy the image so that the  
    # original image does not get affected 

    

    img2 = img.copy() 
    img2.save('./valid/'+img_name+'.png')
    img3 = Image.open('./cut_annot/'+img_name+'.png')  
    img4=img3.copy()
    img4.save('./validannot/'+img_name+'.png')