import cv2 as cv2
import numpy as np

MIN_CONTOUR_AREA =50
MAX_CONTOUR_AREA = 500
MIN_RATIO = 0.1
MAX_RATIO = 0.6

MIN_CONTOUR_AREA_PLAQUE = 1000
MAX_CONTOUR_AREA_PLAQUE = 40000
MIN_RATIO_PLAQUE = 2
MAX_RATIO_PLAQUE = 6

TAIllE_IMAGE = (894,383)
TAILLE_IMAGE_NOMBRE =(40,60)



def image(img,typecolor):  
    trouve=False
    imgcopy=cv2.GaussianBlur(img, (3,3), 0)
    abcd=[]
    numbers= []
    for sss in numbers:
        del(sss)
    imgcopy2=img.copy()
    if (typecolor==1):
        imgcopy2=cv2.cvtColor(imgcopy2,cv2.COLOR_BGR2GRAY)
    elif(typecolor==2):
        imgcopy2 = cv2.cvtColor(imgcopy2,cv2.COLOR_BGR2YCrCb)
        imgcopy2 = imgcopy2[:,:,0]
    
    imgThresh = cv2.Canny(img, 200, 255)
    imgThreshCopy = imgThresh.copy()

    imgThreshCopy3=imgThreshCopy.copy()
    npaContours, npaHierarchy = cv2.findContours(imgThreshCopy,  
                                                cv2.RETR_EXTERNAL,
                                                cv2.CHAIN_APPROX_SIMPLE)  
    for number in npaContours: 
        [intX, intY, intWidth, intHeight] = cv2.boundingRect(number)
        fltArea = cv2.contourArea(number)
        ratio=(intWidth)/(intHeight)
    
        if (ratio > MIN_RATIO) & (ratio < MAX_RATIO):
            if (fltArea > MIN_CONTOUR_AREA) & (fltArea < MAX_CONTOUR_AREA):

            
                numbers.append([intX, intY, intWidth, intHeight])  
    
    numbers = sorted(numbers, key=lambda selule:selule[0] , reverse = False)
    
    for nmr in numbers:
        conteurState=0
        conteurI=nmr[0]
        conteurJ=nmr[1]

        while(conteurI<=nmr[2]+nmr[0]):
            while(conteurJ<=nmr[3]+nmr[1]):
                if ((imgcopy2[conteurJ,conteurI] < 225) & (imgcopy2[conteurJ,conteurI] > 40)):
                    conteurState+=1
                conteurJ+=1
            conteurI+=1 
        if ((conteurState *100) /( nmr[2]*nmr[3]) > 20 ):
            del(nmr)
    
    abcd = sorted(numbers, key=lambda selule:selule[1] , reverse = False)
    cont1 =0
    cont2 =-1
    prec=0
    state=False
    for nmr in abcd:
        
        if state==False:
            if cont2==-1:
                prec=nmr[1]
                cont1+=1
                cont2=0
            else:
                if (abs (nmr[1] - prec ) > 5):
                    cont2+=cont1
                    cont1=1
                else:
                    cont1+=1
                if cont1 ==10 :
                    state=True 
                prec=nmr[1]
        else:
            del(abcd[cont2])

    for iii in range(0,cont2):
        del (abcd[0])
    
    if state==True:
        trouve=True
        abcd = sorted(abcd, key=lambda selule:selule[0] , reverse = False)
        
        for aaaa in abcd:
    
            image_implimentation=imgThresh.copy()
            image_implimentation=cv2.cvtColor(image_implimentation,cv2.COLOR_GRAY2BGR)

            cv2.rectangle(image_implimentation
                        ,(aaaa [0] -2, aaaa [1] -2)     # coint haut gauche
                        ,(aaaa [2]+aaaa [0] +2, aaaa [3]+aaaa [1]+2)
                        , (0,0,255)
                        , 2)

    
    elif state==False:
        for kk in numbers:
            del(kk)
        for ss in npaContours:
            del(ss)
        for jj in abcd :
            del(jj)
        bnbn=imgThreshCopy.copy()
        npaContours2, npaHierarchy2 = cv2.findContours(imgThreshCopy,             # entrer l'image, utiliser la copie, puisque cette function change cette image au cours de la recherche des contours
                                         cv2.RETR_TREE,         # utilise seulement les contours externe
                                         cv2.CHAIN_APPROX_SIMPLE)   # compress les segments horizontal, vertical, et diagonal  et laisse les points d'extremeter

        for nmrr in npaContours2:
            [intX, intY, intWidth, intHeight] = cv2.boundingRect(nmrr)
            fltArea = cv2.contourArea(nmrr) 
            ratio=(intWidth)/(intHeight)
        
            if (ratio > MIN_RATIO_PLAQUE) & (ratio < MAX_RATIO_PLAQUE) :
                if (fltArea > MIN_CONTOUR_AREA_PLAQUE) & (fltArea < MAX_CONTOUR_AREA_PLAQUE):
           
                    intXX=intX
                    intYY=intY
                    intWidthX=intX+intWidth
                    intHeightY=intY+intHeight
        
                    imgThreshCopy2 = imgThresh.copy()
        
                    npaContours5, npaHierarchy = cv2.findContours(imgThreshCopy2,             # entrer l'image, utiliser la copie, puisque cette function change cette image au cours de la recherche des contours
                                                             cv2.RETR_TREE,         # utilise seulement les contours externe
                                                             cv2.CHAIN_APPROX_SIMPLE)   # compress les segments horizontal, vertical, et diagonal  et laisse les points d'extremeter
        
                    for number in npaContours5:
                        [intX, intY, intWidth, intHeight] = cv2.boundingRect(number)
                        if (intX>=intXX and intX+intWidth<=intWidthX)and(intY>=intYY and intY+intHeight<=intHeightY):
                            fltArea = cv2.contourArea(number)
                            ratio=(intWidth)/(intHeight)
                            if (fltArea > MIN_CONTOUR_AREA) & (fltArea < MAX_CONTOUR_AREA):
                                if (ratio > MIN_RATIO) & (ratio < MAX_RATIO) :    
                                    numbers.append([intX, intY, intWidth, intHeight])   
                    numbers = sorted(numbers, key=lambda selule:selule[0] , reverse = False)
                    for nmr in numbers:
                        conteurState=0
                        conteurI=nmr[0]
                        conteurJ=nmr[1]
                        while(conteurI<nmr[2]):
                            while(conteurJ<nmr[3]):
                                
                                if ((imgcopy[conteurI,conteurJ] < 230) and (imgcopy[conteurI,conteurJ] > 25)):
                                    conteurState+=1
                                    
                        if ((conteurState *100) /( nmr[2]*nmr[3]) > 20 ):
                            del(nmr)
            
                    abcd = sorted(numbers, key=lambda selule:selule[1] , reverse = False)
                    cont1 =0
                    cont2 =0
                    prec=0
                    state=False
                    for nmr5 in abcd:

                        if state==False:
                            if cont1==0:
                                prec=nmr5[1]
                                
                                cont1+=1
                            else:
                                if (abs (nmr5[1] - prec ) > 5):
                                    cont2+=cont1
                                    cont1=0
                                else:
                                    cont1+=1
                                if cont1 ==10 :
                                    state=True 
                                prec=nmr5[1]
                        else:
                            del(nmr5)       
                    
                    end = [] 
                    for i in abcd: 
                        if i not in end: 
                            end.append(i) 
                    for i in abcd:
                        del(i)
                    abcd = sorted(end, key=lambda selule:selule[0] , reverse = False)
                    
                    
                    for kkk in abcd:
                        [intX, intY, intWidth, intHeight]=kkk
                        cv2.destroyAllWindows()
                    
                    trouve=state

    
    return [trouve,abcd]
