import cv2
import numpy as np
import meth


NMBR_IMAGE_MAJ=15
conteur_maj=0


video='voiture.mp4'
cap=cv2.VideoCapture(video)

image_back=meth.take_back_ground_debut(cap)
cv2.imshow("hhh",image_back)
cv2.waitKey(0)


##################

state=False
while True:
    i=0
    while ((i<NMBR_IMAGE_MAJ) and (not (state))):
        ret, frame=cap.read()
        new_frame=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY )
        state=meth.sub_image(image_back,new_frame)
        if state !=True:
            i+=1
    
    if i ==NMBR_IMAGE_MAJ:
        meth.maj_back(image_back,new_frame)
        break
    
    if state==True:
        print("mouvemment")
        

"""




def calcule_matricule(image):
    cv2.imshow('frame', image)
    cv2.waitKey()
    cap.release()
    cv2.destroyAllWindows()


##########################     main



SEILLE_RAYON=20
seuil =10
i=0
tab_image=[]
color_infos=(0, 0, 255)



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
            cv2.circle(frame, (int(x)+xmin, int(y)+ymin), 5, color_infos, 10)
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

    fps=cv2.getTickFrequency()/(cv2.getTickCount()-tickmark)
    cv2.putText(frame, "FPS: {:05.2f}  Seuil: {:d}".format(fps, seuil), (10, 30), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, color_infos, 1)
          """  
