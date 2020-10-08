import csv
import cv2
import numpy as np
from os import walk

def write_bdd():

    with open("./BDD1.txt", 'w', newline='') as file:
        writer = csv.writer(file)
        
        for index in range (10):
            f=[]
            for (dirpath, dirnames, filenames) in walk("../BDDimages/BDD1/"+str(index)+"/"):
                f.extend(filenames)
            for j in f:
                filrname="../BDDimages/BDD1/"+str(index)+"/"+j
                image=cv2.imread(filrname)
                writer.writerow(image_ligne(index,image.shape[0],image.shape[1],image))  
                


def image_ligne(index,ww,hh,image):
        image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        image = cv2.threshold(image, 125, 255, cv2.THRESH_BINARY)[1]
        tab=[]
        tab.append(index)
        tab.append(ww)
        tab.append(hh)
        for w in range(image.shape[0]):
            for h in range (image.shape[1]):
                tab.append(image[w,h])
        return tab

write_bdd()
