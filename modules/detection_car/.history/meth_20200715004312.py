
import cv2
import numpy as np


#################################################
# LES CORDONNÉE DE SONE DINTERRET DE LIMAGE 
# LA ZONE LI KI TKOUN THARKT HAJA N3TABROUHA TOMOBILE 
XMIN=90
XMAX=510
YMIN=300
YMAX=360
#################################################
SEILLE_PIXEL=20
SEILLE_IMAGE=200


def moyenne_images(images):
    tab_image=np.array(images)
    image_moyenne=np.mean(tab_image, axis=0)
    ## np.mean Renvoie la moyenne des éléments du tableau
    ## les valeurs  de retour sont de type float64 
    ## Nous devons le convertir en type par default qui est uint8
    return image_moyenne.astype(np.uint8) 

def take_back_ground_debut(cap):
    # nombre des image pour calculler le background
    nbr_images=2
    i=0
    tab_image=[]
    while i<nbr_images:
        ret, frame=cap.read()
        new_frame=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY )
        tab_image.append(new_frame[YMIN:YMAX,XMIN:XMAX])
        i+=1

    image_back=moyenne_images(tab_image)
    image_back=image_back
    return image_back

def sub_image(image_back,frame):
    frame_temp=frame.copy()[YMIN:YMAX,XMIN:XMAX]
    image_back_temp=image_back.copy()
    new_image_temp=image_back_temp.copy()
    somme=0

    for i in range(image_back_temp.shape[0]):
        for j in range(image_back_temp.shape[1]):
            new_image_temp[i,j]=abs(int(image_back[i,j])-int(frame_temp[i,j]))
            if (new_image_temp[i,j]<SEILLE_PIXEL):
                new_image_temp[i,j]=0
            else:
                somme+=new_image_temp[i,j]
                new_image_temp[i,j]=255
    return [new_image_temp,somme]

def maj_back(image_back,frame):
    tab=[]
    tab.append(image_back)
    tab.append(image_back)
    tab.append(frame[YMIN:YMAX,XMIN:XMAX])
    return moyenne_images(tab)

def verrifier(image_info):
    if (image_info[1]>SEILLE_IMAGE):
        kernel = np.ones((3,3),np.uint8)
        #image_info[0] = cv2.erode(image_info[0] ,kernel,iterations = 1)
        #image_info[0] = cv2.dilate(image_info[0] ,kernel,iterations = 1)
        #image_info[0] = cv2.morphologyEx(image_info[0], cv2.MORPH_OPEN, kernel) 
        image_info[0] = cv2.morphologyEx(image_info[0], cv2.MORPH_OPEN, kernel) #opening


        #image_info[0] = cv2.dilate(image_info[0] ,kernel,iterations = 1)
        #image_info[0] = cv2.erode(image_info[0] ,kernel,iterations = 1)
        image_info[0] = cv2.morphologyEx(image_info[0], cv2.MORPH_CLOSE, kernel) #closing

        ## nchoufou akbar objet w nahsseb missaha ta3ou 
        npaContours, npaHierarchy = cv2.findContours(image_info[0],             # entrer l'image, utiliser la copie, puisque cette function change cette image au cours de la recherche des contours
                                             cv2.RETR_EXTERNAL,         # utilise seulement les contours externe
                                             cv2.CHAIN_APPROX_SIMPLE)   # compress les segments horizontal, vertical, et diagonal  et laisse les points d'extremeter
        all_area=[]
        imageaffichage=image_info[0].copy()
        imageaffichage=cv2.cvtColor(imageaffichage,cv2.COLOR_GRAY2BGR) 
        cv2.drawContours(imageaffichage, npaContours, -1, (0,255,0), 1)

        for contour in npaContours: 
            # [intX, intY, intWidth, intHeight] = cv2.boundingRect(contour)
            fltArea = cv2.contourArea(contour)
            if fltArea>0:
                all_area.append(fltArea)
                print(str(fltArea)+"--------- \n")
            #if fltArea>100:
            #    cv2.drawContours(image_info[0], contour, -1, (0,255,0), 3)
        print("le max est "+str(max(all_area)))
        #cv2.imshow("fenetrre1",image_info[0])
        
        cv2.imshow("imageaffichage",imageaffichage)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            a=0
    else:
        cv2.imshow("fenetrre2",image_info[0])
        cv2.waitKey(0)
    return True


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
