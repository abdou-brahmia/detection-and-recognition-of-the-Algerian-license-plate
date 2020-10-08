import csv
import cv2
import numpy as np

import threading
from skimage.measure import compare_ssim
import time
from os import walk
import modules.recon_number.BDDcsv.coder_decoder as coder_csv

global kk
kk=["0","0","0","0","0","0","0","0","0","0"]
def is_number(number_image,bdd):

    val=[0,0,0,0,0,0,0,0,0,0]
    temp_element_from_bdd=bdd[0]
    dim_h=temp_element_from_bdd[1].shape[0]
    dim_w=temp_element_from_bdd[1].shape[1]

    dim=(dim_w,dim_h)
    number_image1=cv2.resize(number_image,dim, interpolation = cv2.INTER_AREA)
    _,number_image1 = cv2.threshold(number_image1,170,255,cv2.THRESH_BINARY)

    for element in bdd :
        (score, diff) = compare_ssim(number_image1, element[1], full=True)

        if (val[int(element[0])]<score):
            val[int(element[0])]=score

    return val.index(max(val))


def simplest_cb(img, percent):
    out_channels = []
    channels = cv2.split(img)
    totalstop = channels[0].shape[0] * channels[0].shape[1] * percent / 200.0
    for channel in channels:
        bc = np.bincount(channel.ravel(), minlength=256)
        lv = np.searchsorted(np.cumsum(bc), totalstop)
        hv = 255-np.searchsorted(np.cumsum(bc[::-1]), totalstop)
        out_channels.append(cv2.LUT(channel, np.array(tuple(0 if i < lv else 255 if i > hv else round((i-lv)/(hv-lv)*255) for i in np.arange(0, 256)), dtype="uint8")))
    return cv2.merge(out_channels)

def recon_number_th(numbers,image,bdd):
    threads = []
    i=0
    local_mat=[10000,10000,0,0]
    s=""


    for nmbr in numbers:
        [intX, intY, intWidth, intHeight]=nmbr
        nmrImage=cv2.cvtColor(image[intY :intY+intHeight,intX:intX+intWidth ],cv2.COLOR_BGR2GRAY)
        nmrImage=simplest_cb(nmrImage,1)
        th = threading.Thread(target=is_number_th, args=(nmrImage,bdd.copy(),i))
        threads.append(th)
        th.start()
        i+=1
        
        if  intX < local_mat [0] :
            local_mat [0] =intX
        if intY < local_mat [1] :
            local_mat [1] =intY
        if  intX + intWidth > local_mat [2] :
            local_mat [2] =intX + intWidth
        if intY +intHeight > local_mat [3] :
            local_mat [3] =intY +intHeight
    iiii=0
    
    while iiii !=10:
        if not(threads [iiii].isAlive()):
            threads[iiii].join()
            iiii+=1
    
    return kk,local_mat


def is_number_th(number_image,bdd,i):
    
    val=[0,0,0,0,0,0,0,0,0,0]
    temp_element_from_bdd=bdd[0]
    dim_h=temp_element_from_bdd[1].shape[0]
    dim_w=temp_element_from_bdd[1].shape[1]
    
    dim=(dim_w,dim_h)
    number_image1=cv2.resize(number_image,dim, interpolation = cv2.INTER_AREA)
    _,number_image1 = cv2.threshold(number_image1,170,255,cv2.THRESH_BINARY)

    for element in bdd :
        (score, diff) = compare_ssim(number_image1, element[1], full=True)
        if (val[int(element[0])]<score):
            val[int(element[0])]=score
    
    kk[i]=str(val.index(max(val)))


def read_bdd(type_bdd):
    #1 my bdd images 
    #2 my bdd csv
    #3 bdd net images
    #4 bdd net csv

    bdd= []
    names=[]
    if type_bdd==1 or type_bdd==3:
        path=""
    
        if type_bdd==1:
            path="./modules/recon_number/BDDimages/BDD1/"
        if type_bdd==3:
            path="./modules/recon_number/BDDimages/BDD2/"

        i=0
        val=0
        while (i<10):
            f = []
            for (dirpath, dirnames, filenames) in walk(path+str(i)+"/"):
                f.extend(filenames)
                break
            for a in f:
                names.append([i,a])

            i+=1

        for name in names:
            img = cv2.imread(path+str(name[0])+"/"+name[1])
            img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            bdd.append([name[0],img])
            
        
    elif type_bdd==2 or type_bdd==4 :
        bdd= coder_csv.read_bdd(type_bdd)
    
    return bdd


