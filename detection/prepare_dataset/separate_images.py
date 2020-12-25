from PIL import Image 
import shutil


f_train = open("./train.txt", "r")

l_train=f_train.readlines()

for line in l_train:
    a,b,c,d,image = line.split('/')
    image, x=image.split('.')
    image=image+'.jpg'
    img = Image.open('./images/'+image)  
    # make a copy the image so that the  
    # original image does not get affected 
    img2 = img.copy() 
    img2.save('./trainS/'+image)
    
    name, aux=image.split('.')
    shutil.copyfile('./labels/'+name+'.txt', './labels_train/'+name+'.txt')

f_test = open("./valid.txt", "r")

l_test=f_test.readlines()

for line in l_test:
    a,b,c,d,image = line.split('/')
    image, x=image.split('.')
    image=image+'.jpg'
    img = Image.open('./images/'+image) 
    # make a copy the image so that the  
    # original image does not get affected 
    img2 = img.copy() 
    img2.save('./testS/'+image)
    
    name, aux=image.split('.')
    shutil.copyfile('./labels/'+name+'.txt', './labels_test/'+name+'.txt')