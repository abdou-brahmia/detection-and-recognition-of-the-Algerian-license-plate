import cv2
import numpy as np

def moyenne_image(video, nbr):
    cap=cv2.VideoCapture(video)
    tab_image=[]
    for f in range(nbr):
        ret, frame=cap.read()
        if ret is False:
            break
        image=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        tab_image.append(image)
    tab_image=np.array(tab_image)
    return np.mean(tab_image, axis=0)



def calcul_mask(image, fond, seuil):
    image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    height, width=image.shape
    mask=np.zeros([height, width], np.uint8)
    image=image.astype(np.int32)
    for y in range(height):
        for x in range(width):
            if abs(fond[y][x]-image[y][x])>seuil:
                mask[y][x]=255
    kernel=np.ones((5, 5), np.uint8)
    mask=cv2.erode(mask, kernel, iterations=1)
    mask=cv2.dilate(mask, kernel, iterations=3)
    return mask




##########################main


import cv2
import numpy as np
import common

fond=common.moyenne_image(video, 500)
cv2.imshow('fond', fond.astype(np.uint8))
fond=fond.astype(np.int32)
cap=cv2.VideoCapture(video)



image=common.moyenne_image('autoroute.mp4', 100)
cv2.imshow('fond', image.astype(np.uint8))
cv2.waitKey()
cap.release()
cv2.destroyAllWindows()










while True:
    ret, frame=cap.read()
    tickmark=cv2.getTickCount()
    mask=common.calcul_mask(frame[ymin:ymax, xmin:xmax], fond, seuil)
    elements=cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    nbr=0
    for e in elements:
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
