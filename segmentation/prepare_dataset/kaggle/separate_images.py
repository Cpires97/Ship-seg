from PIL import Image 
import shutil


f_train = open("./airbus-ship-detection/input/detection/train2/train.txt", "r")

l_train=f_train.readlines()

for line in l_train:
    a,b,c,d,image = line.split('/')
    image, x=image.split('.')
    image=image+'.jpg'
    img = Image.open('./airbus-ship-detection/input/train_v2/'+image)  
    # make a copy the image so that the  
    # original image does not get affected 
    img2 = img.copy() 
    img2.save('./airbus-ship-detection/input/detection/train2/images/trainkaggle2/'+image)
    
    name, aux=image.split('.')
    shutil.copyfile('./airbus-ship-detection/input/detection/train2/labels_train/'+name+'.txt', './airbus-ship-detection/input/detection/train2/labels/trainkaggle2/'+name+'.txt')

f_test = open("./airbus-ship-detection/input/detection/train2/valid.txt", "r")

l_test=f_test.readlines()

for line in l_test:
    a,b,c,d,image = line.split('/')
    image, x=image.split('.')
    image=image+'.jpg'
    img = Image.open('./airbus-ship-detection/input/train_v2/'+image) 
    # make a copy the image so that the  
    # original image does not get affected 
    img2 = img.copy() 
    img2.save('./airbus-ship-detection/input/detection/train2/images/testkaggle2/'+image)
    
    name, aux=image.split('.')
    shutil.copyfile('./airbus-ship-detection/input/detection/train2/labels_train/'+name+'.txt', './airbus-ship-detection/input/detection/train2/labels/testkaggle2/'+name+'.txt')