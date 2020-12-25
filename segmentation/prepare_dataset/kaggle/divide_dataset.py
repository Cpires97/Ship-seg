import glob
import os
current_dir = './airbus-ship-detection/input/detection/train2/labels_train'
# Percentage of images to be used for the valid set
percentage_test = 20
# Create train.txt and valid.txt
file_train = open('./airbus-ship-detection/input/detection/train2/train.txt', 'w')  
file_test = open('./airbus-ship-detection/input/detection/train2/valid.txt', 'w')
# Populate train.txt and valid.txt
counter = 1  
index_test = round(100 / percentage_test)  
for file in glob.iglob(os.path.join(current_dir, '*.txt')):  
    title, ext = os.path.splitext(os.path.basename(file))
    if counter == index_test:
        counter = 1
        file_test.write( "../train2/images/testkaggle2"+ "/" + title + '.jpg' + "\n")
    else:
        file_train.write("../train2/images/trainkaggle2" + "/" + title + '.jpg' + "\n")
        counter = counter + 1