import cv2
import numpy as np
import meth




def calcule_matricule(image):
    frame=image.copy()
    cv2.circle(frame, (int(x)+xmin, int(y)+ymin), 5, color_infos, 10)
    cv2.waitKey()
    cap.release()
    cv2.destroyAllWindows()


##########################     main

SEILLE_RAYON=20
seuil =10
i=0
tab_image=[]


video='voiture.mp4'
cap=cv2.VideoCapture(video)
while i<10:
    ret, frame=cap.read()
    tab_image.append(frame)
    i+=1
image_back=meth.moyenne_images(tab_image)

i=0
while True:
    ret, frame=cap.read()
    tickmark=cv2.getTickCount()
    mask=meth.calcul_mask(frame,image_back, seuil)
    elements=cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    for e in elements:
        ## contour_area = cv2.contourArea(e)
        ## if (contour_area > MIN_CONTOUR_AREA) : 
        ((x, y), rayon)=cv2.minEnclosingCircle(e)
        if rayon>SEILLE_RAYON:
            fps=cv2.getTickFrequency()/(cv2.getTickCount()-tickmark)
            cv2.putText(frame, "FPS: {:05.2f}  Seuil: {:d}".format(fps, seuil), (10, 30), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, color_infos, 1)
            calcule_matricule(frame)
            i=0   
        
        else :
            fps=cv2.getTickFrequency()/(cv2.getTickCount()-tickmark)
            cv2.putText(frame, "FPS: {:05.2f}  Seuil: {:d}".format(fps, seuil), (10, 30), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, color_infos, 1)
            cv2.imshow('frame', frame)
            i+=1


        if (i==50):
            image_back=meth.moyenne_images(tab_image)
            i=0
        if (i>=40):
            tab_image[i-40]=frame
            

""" key=cv2.waitKey(1)&0xFF
if key==ord('q'):
    break
if key==ord('p'):
    seuil+=1
if key==ord('m'):
    seuil-=1
stop=0
if not stop:
if key==ord('s'):
    stop=not stop
 """