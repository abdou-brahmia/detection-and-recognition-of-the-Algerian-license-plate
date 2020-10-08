
import cv2
import numpy as np

def moyenne_image(images):
    tab_image=np.array(images)
    image_moyenne=np.mean(tab_image, axis=0)
    return image_moyenne.astype(np.uint8)


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

i=0
tab_image=[]
video='voiture.mp4'
cap=cv2.VideoCapture(video)
while i<10:
    ret, frame=cap.read()
    tab_image.append(frame)
    i+=1
image_moyenne=moyenne_image(tab_image)


cv2.imshow('fond', moyenne)
cv2.waitKey()
