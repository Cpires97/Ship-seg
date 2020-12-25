from PIL import Image
import os
import random


txt=input('Nome do ficheiro:')
aux=txt + ".gt.txt"
print(aux)
f = open('./videos/'+aux, "r")


lines=f.readlines()

for line in lines:
    frame,x,y,w,h,iden,temp = line.split()
    frame=int(frame)
    xr=int(x)
    yr=int(y)
    wr=int(w)
    hr=int(h)
    if os.path.isfile('./images/'+txt +'_frame'+str(frame)+'.jpg')==True:
        
        f1= open('./labels/'+txt +'_frame'+str(frame)+'.txt',"a+")
        im = Image.open('./images/'+txt +'_frame'+str(frame)+'.jpg')
        width, height = im.size
        x_center=xr+wr/2
        x_center=x_center/width
        y_center=yr+hr/2
        y_center=y_center/height
        w_norm=wr/width
        h_norm=hr/height

        x_back=random.randrange(0, width-wr)
        
        y_back=random.randrange(0, height-hr)

        x_back_center=(x_back+wr/2)/width
        y_back_center=(y_back+hr/2)/height

        f1.write('0 '+str(x_center)+' '+str(y_center)+' '+ str(w_norm)+' '+str(h_norm)+'\n')
        f1.close()


