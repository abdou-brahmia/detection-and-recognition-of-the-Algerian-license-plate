
import cv2
import numpy as np


#################################################
# LES CORDONNÉE DE SONE DINTERRET DE LIMAGE 
# LA ZONE LI KI TKOUN THARKT HAJA N3TABROUHA TOMOBILE 
XMIN=90
XMAX=510
YMIN=100
YMAX=360
#################################################
SEILLE_PIXEL=20
SEILLE_IMAGE=20


def moyenne_images(images):
    tab_image=np.array(images)
    image_moyenne=np.mean(tab_image, axis=0)
    ## np.mean Renvoie la moyenne des éléments du tableau
    ## les valeurs  de retour sont de type float64 
    ## Nous devons le convertir en type par default qui est uint8
    return image_moyenne.astype(np.uint8) 

def take_back_ground_debut(cap):
    # nombre des image pour calculler le background
    nbr_images=10
    i=0
    tab_image=[]
    while i<nbr_images:
        ret, frame=cap.read()
        tab_image.append(frame[YMIN:YMAX,XMIN:XMAX])
        i+=1

    image_back=moyenne_images(tab_image)
    image_back=image_back
    return image_back

def sub_image(image1,image2):
    a=0

    return False

def maj_back(image_back,frame):
    tab=[]
    tab.append(image_back)
    tab.append(frame)
    

"""

def calcul_mask(image, fond, seuil):
    image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    height, width=image.shape
    mask=np.zeros([height, width], np.uint8)
    for y in range(height):
        for x in range(width):
            if abs(int(fond[y][x])-int(image[y][x]))>seuil:
                mask[y][x]=255
    kernel=np.ones((3, 3), np.uint8)
    mask=cv2.erode(mask, kernel, iterations=1)
    mask=cv2.dilate(mask, kernel, iterations=3)
    return mask


def test_moyenne():
    ##### test moyene des images
    i=0
    tab_image=[]
    video='voiture.mp4'
    cap=cv2.VideoCapture(video)
    while i<10:
        ret, frame=cap.read()
        tab_image.append(frame)
        i+=1
    image_moyenne=moyenne_images(tab_image)
    cv2.imshow('fond', image_moyenne)
    cv2.waitKey()


def test_mask():
    ##### test moyene des images
    i=0
    tab_image=[]
    video='voiture.mp4'
    cap=cv2.VideoCapture(video)
    while i<10:
        ret, frame=cap.read()
        tab_image.append(frame)
        i+=1
    image_moyenne=moyenne_images(tab_image)
    ret, frame=cap.read()
    image_moyenne_gray=cv2.cvtColor(image_moyenne, cv2.COLOR_BGR2GRAY)
    mask=calcul_mask(frame,image_moyenne_gray,50)
    cv2.imshow('fond', image_moyenne)
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.waitKey()


## test_moyenne()
## test_mask()

def a(val):
    val[0]= not val[0]

b=[True]
a(b)
print(b[0])
"""
