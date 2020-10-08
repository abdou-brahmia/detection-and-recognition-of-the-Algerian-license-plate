
import numpy as np
import cv2



def detectCar(image,background,resolution,SEILLE_PIXEL,SEILLE_IMAGE_1,SEILLE_IMAGE_2):
    new_image=cv2.resize(image, resolution, interpolation = cv2.INTER_AREA)
    new_image=cv2.cvtColor(new_image, cv2.COLOR_BGR2GRAY )
    image_info=sub_image(new_image,background,SEILLE_PIXEL)
    state=verrifier(image_info,SEILLE_IMAGE_1,SEILLE_IMAGE_2)
    return state


def take_back_ground_debut(cap,resolution,nombreFrameMaj):
    i=0
    tab_image=[]
    while i<nombreFrameMaj:
        
        ret, frame=cap.read()
        if ret ==True:
            frame=cv2.resize(frame, resolution, interpolation = cv2.INTER_AREA)
            new_frame=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY )

            tab_image.append(new_frame)
            i+=1
        else:
            cv2.destroyAllWindows()
            break
    image_back=moyenne_images(tab_image)
    
    return image_back


def moyenne_images(images):
    tab_image=np.array(images)
    image_moyenne=np.mean(tab_image, axis=0)
 
    return image_moyenne.astype(np.uint8) 

def sub_image(image_back,frame,SEILLE_PIXEL): 

    new_image_temp=image_back.copy()
    somme=0
            
    for i in range(new_image_temp.shape[0]):
        for j in range(new_image_temp.shape[1]):
            new_image_temp[i,j]=abs(int(image_back[i,j])-int(frame[i,j]))
            if (new_image_temp[i,j]<SEILLE_PIXEL):
                new_image_temp[i,j]=0
            else:
                somme+=1
                new_image_temp[i,j]=255
  
    return [new_image_temp,somme]

def maj_back(image_back,frame):
    tab=[]
    tab.append(image_back)
    tab.append(image_back)
    tab.append(frame)
    img=moyenne_images(tab)
  
    return img

def verrifier(image_info,SEILLE_IMAGE_1,SEILLE_IMAGE_2):
    stateValue=False
    image=image_info[0]

    image5=image_info[0]
    Place=None
    if (image_info[1]>SEILLE_IMAGE_1):
        kernel = np.ones((3,3),np.uint8)
        image = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
        image = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
        image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
        image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

        npaContours, npaHierarchy = cv2.findContours(image.copy(), 
                                                     cv2.RETR_EXTERNAL,   
                                             cv2.CHAIN_APPROX_SIMPLE)   
        all_area=[]
        imageaffichage=image.copy()
        imageaffichage=cv2.cvtColor(imageaffichage,cv2.COLOR_GRAY2BGR) 
        maxArea=0
  
        for contour in npaContours:
            fltArea = cv2.contourArea(contour)
            if fltArea>maxArea:
                maxArea =fltArea
                [intX, intY, intWidth, intHeight] = cv2.boundingRect(contour)
                Place=[intX, intY, intWidth, intHeight]
        if (maxArea>SEILLE_IMAGE_2) :
            stateValue=True
        else:
            stateValue=False
        
    return [stateValue,Place]
