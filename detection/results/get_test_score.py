# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 17:12:38 2020

@author: Carlos Pires
"""

import json
from PIL import Image 

def get_iou(bb1, bb2):
    
    if bb1['x1']< bb2['x1'] and bb1['x2']>bb2['x2'] and bb1['y1']<bb2['y1'] and bb1['y2'] >bb2['y2']:
        return 1.0
    x_left = max(bb1['x1'], bb2['x1'])
    y_top = max(bb1['y1'], bb2['y1'])
    x_right = min(bb1['x2'], bb2['x2'])
    y_bottom = min(bb1['y2'], bb2['y2'])

    if x_right < x_left or y_bottom < y_top:
        return 0.0

    intersection_area = (x_right - x_left) * (y_bottom - y_top)

    bb1_area = (bb1['x2'] - bb1['x1']) * (bb1['y2'] - bb1['y1'])
    bb2_area = (bb2['x2'] - bb2['x1']) * (bb2['y2'] - bb2['y1'])

    iou = intersection_area / float(bb1_area + bb2_area - intersection_area)

    return iou



with open('./results_seagull6000/cropped_img_seagull6000_th=0.001.txt') as json_file:
    results = json.load(json_file)
    
with open('./groundtruth_bb.txt') as json_file:
    g_truth = json.load(json_file)

tp=0
fp=0
total_boats=0
inspected_list=[]
for i in g_truth:
    total_boats=len(i['objects'])+ total_boats
    inspected_list.append({"filename": i['filename'], "checked": [0]*len(i['objects'])})

for obj in results:
    image=obj['filename']
    for n, i in enumerate(g_truth):
        if i['filename']==obj['filename']:
            for bb in obj['objects']:
                flag_tp=0
                for x, bb_truth in enumerate(i['objects']):
                    iou=get_iou(bb,bb_truth)
                    print(iou)
                    if iou>0.5:
                        inspected_list[n]['checked'][x]=1
                        tp=tp+1
                        flag_tp=1
                if flag_tp==0:
                    fp=fp+1
tp=0
for j,aux in enumerate(inspected_list):
    for x,check in enumerate(aux['checked']):
        if check==1:
            tp+=1
        elif check==0:
            print("aa")
#            boxes=g_truth[j]['objects']
#            box=boxes[x]
#            img=Image.open('./images/'+g_truth[j]['filename'])
#            width, height = img.size 
#            
#            bb_width=box["x2"]-box["x1"]
#            bb_height=box["y2"]-box["y1"]
#            if box["x1"] < bb_width/2:
#                left=0
#            else:
#                left=box["x1"] - bb_width/2
#            if box["y1"] < bb_height/2:
#                top=0
#            else:
#                top=box["y1"] - bb_height/2
#            if box["x2"]+bb_width/2 > width:
#                right=width
#            else:
#                right=box["x2"]+bb_width/2
#            if box["y2"]+bb_height/2 > height:
#                bottom=width
#            else:
#                bottom=box["y2"]+bb_height/2 
#                
#            annot_img=Image.open('./annot_images2/'+g_truth[j]['filename'].split('.')[0]+"/label.png")
#            cropped_img = img.crop((left, top, right, bottom)) 
#            cropped_img = cropped_img.resize((480,360)) 
#            cropped_img.save('./md_images2/'+g_truth[j]['filename'].split('.')[0]+"_"+str(x)+".png")
#            
#            cropped_annot = annot_img.crop((left, top, right, bottom))
#            cropped_annot = cropped_annot.resize((480,360)) 
#            cropped_annot.save('./md_annot2/'+g_truth[j]['filename'].split('.')[0]+"_"+str(x)+".png")
            
print("total boats: "+ str(total_boats)) 
print("true positives: "+str(tp))
print("false positives: "+ str(fp))
print("false negatives: "+str(total_boats-tp))