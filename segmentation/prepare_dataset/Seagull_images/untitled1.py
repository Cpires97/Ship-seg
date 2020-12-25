# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 12:27:33 2020

@author: Carlos Pires
"""


import json
import cv2

from PIL import Image 

def get_iou(bb1, bb2):
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

def agregate_bb(bb1, bb2):
    x_left = min(bb1['x1'], bb2['x1'])
    y_top = min(bb1['y1'], bb2['y1'])
    x_right = max(bb1['x2'], bb2['x2'])
    y_bottom = max(bb1['y2'], bb2['y2'])
    
    return {"x1": x_left,"x2":x_right, "y1":y_top, "y2":y_bottom}

def get_rects_list(bb_list,width, height):
    rects_list=[]
    for bb in bb_list:        
        if bb['name']=="boat":
            x_center1=bb['relative_coordinates']['center_x']*width
            y_center1=bb['relative_coordinates']['center_y']*height
            w_boat1=bb['relative_coordinates']['width']*width
            h_boat1=bb['relative_coordinates']['height']*height
            rects_list.append({"x1":int(x_center1-w_boat1/2),"x2": int(x_center1+w_boat1/2), "y1": int(y_center1-h_boat1/2), "y2": int(y_center1+h_boat1/2)})
    return rects_list

def get_bb_uniou(bbs):
    bbs_aux=bbs     
    for i, bb in enumerate(bbs):                        
        for j, bbaux in enumerate(bbs_aux):      
            iou=get_iou(bb, bbaux)
            if iou>0:
                print(iou)
                agregated_bb=agregate_bb(bb, bbaux)
                bbs[i]=agregated_bb
                bbs[j]=agregated_bb
    return bbs

def delete_reps(bbs):
    final=[]
    for bb in bbs:
        if bb in final:
            continue
        else:
            final.append(bb) 
    return final                
                

def duplicate_bbs(bbs, width, height, img, annot_img):
    i=1
    cropped_bb=[]
    for final_bb in bbs:
        bb_width=final_bb["x2"]-final_bb["x1"]
        bb_height=final_bb["y2"]-final_bb["y1"]
        if final_bb["x1"] < bb_width/2:
            left=0
        else:
            left=final_bb["x1"] - bb_width/2
        if final_bb["y1"] < bb_height/2:
            top=0
        else:
            top=final_bb["y1"] - bb_height/2
        if final_bb["x2"]+bb_width/2 > width:
            right=width
        else:
            right=final_bb["x2"]+bb_width/2
        if final_bb["y2"]+bb_height/2 > height:
            bottom=width
        else:
            bottom=final_bb["y2"]+bb_height/2 
        
        cropped_img = img.crop((left, top, right, bottom)) 
        #cropped_img = cropped_img.resize((480,360)) 
        
         ##para os cortes apenas
        res=0
        
        res=int((right-left)%32)
        
        if res==0:
            new_width=int(right-left)
        else:
            new_width=int(right-left)-res+32
        
        res=int((bottom-top)%32)
        if res==0:
            new_height=int(bottom-top)
        else:
            new_height=int(bottom-top)-res+32
        
        cropped_img = cropped_img.resize((new_width,new_height))
        
        
        #cropped_img.save('./cut_images2/'+name_image+"_"+str(i)+".png")
        
        cropped_annot = annot_img.crop((left, top, right, bottom))  
        
        cropped_annot = cropped_annot.resize((new_width,new_height)) 
        
        #cropped_annot.save('./cut_annot2/'+name_image+"_"+str(i)+".png")
        
        cropped_bb.append({"id": i,"x1":left,"x2":right,"y1":top,"y2":bottom})
        i=i+1     
    return cropped_bb



with open('./results_seagull6000/resultseagull6000_th=0.00001.txt') as json_file:
    data = json.load(json_file)
 

    
d=0
list_croppedimg=[]
for obj in data:     
#    init=1
#    result_bbs=[]
    filename=obj['filename']
    aux,aux1,aux2, image=filename.split("/")   
    img=Image.open('./images/'+image)    
    width, height = img.size    
    name_image, ext=image.split(".")
    annot_img=Image.open('./annot_images/'+name_image+"/label.png")
    
    rects_list=get_rects_list(obj['objects'], width, height)
    bbs=get_bb_uniou(rects_list)
    
    final=delete_reps(bbs)
    
    cropped=duplicate_bbs(final, width, height, img, annot_img)
    
    list_croppedimg.append({"filename": image, "objects": cropped})
#    d+=1
#    if d>4:
#        break
    
with open('./results_seagull6000/cropped_img_seagull6000_th=0.00001.txt', 'w') as outfile:
    json.dump(list_croppedimg, outfile)    