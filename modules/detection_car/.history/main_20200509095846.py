


##########################main


import cv2
import numpy as np
import meth

fond=meth.moyenne_image(video, 500)
cv2.imshow('fond', fond.astype(np.uint8))
fond=fond.astype(np.int32)
cap=cv2.VideoCapture(video)



image=common.moyenne_image('autoroute.mp4', 100)
cv2.imshow('fond', image.astype(np.uint8))
cv2.waitKey()
cap.release()
cv2.destroyAllWindows()



seuil =10
i=0
tab_image=[]
video='voiture.mp4'
cap=cv2.VideoCapture(video)
while i<10:
    ret, frame=cap.read()
    tab_image.append(frame)
    i+=1
image_back=moyenne_images(tab_image)
state=True
i=0

while True:
    ret, frame=cap.read()
    tab_image[i]=frame
    
    tickmark=cv2.getTickCount()
    mask=meth.calcul_mask(frame,image_back, seuil)
    elements=cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    for e in elements:
        fltArea = cv2.contourArea(number)

        ((x, y), rayon)=cv2.minEnclosingCircle(e)
        if rayon>20:
            cv2.circle(frame, (int(x)+xmin, int(y)+ymin), 5, color_infos, 10)
            nbr+=1
    if nbr>nbr_old:
        vehicule+=1
    nbr_old=nbr
    fps=cv2.getTickFrequency()/(cv2.getTickCount()-tickmark)
    cv2.putText(frame, "FPS: {:05.2f}  Seuil: {:d}".format(fps, seuil), (10, 30), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, color_infos, 1)
    cv2.rectangle(frame, (xmin, ymin), (xmax+120, ymax), (255, 0, 0), 5)
    cv2.rectangle(frame, (xmax, ymin), (xmax+120, ymax), (255, 0, 0), cv2.FILLED)
    cv2.putText(frame, "{:04d}".format(vehicule), (xmax+10, ymin+35), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (255, 255, 255), 2)
    cv2.imshow('video', frame)
    cv2.imshow('mask', mask)
    key=cv2.waitKey(1)&0xFF
    if key==ord('q'):
        break
    if key==ord('p'):
        seuil+=1
    if key==ord('m'):
        seuil-=1

cap.release()
cv2.destroyAllWindows()


stop=0

    if not stop:


    if key==ord('s'):
        stop=not stop
