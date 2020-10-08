import cv2 as cv2
import numpy as np

MIN_CONTOUR_AREA = 280
MAX_CONTOUR_AREA = 2000
MIN_RATIO = 0.2
MAX_RATIO = 0.9

COLOR_GREEN=(0, 255, 0)
COLOR_RED=(0, 0, 255)


TAIllE_IMAGE = (894,383 )
TAILLE_IMAGE_NOMBRE =(40,60)


images=[]







"""
imgs=cv2.imread('./img/24.jpg')
#imgs=cv2.imread('./img/FHD0072.JPG')

#imgs = cv2.resize(imgs, (int(imgs.shape[1] / 3), int(imgs.shape[0]/3)),interpolation = cv2.INTER_AREA)
#imgs = cv2.resize(imgs, (894,383 ),interpolation = cv2.INTER_AREA)
imgs = cv2.resize(imgs, (1024,438 ),interpolation = cv2.INTER_AREA)
#imgs=imgs

imgaffichage=imgs.copy()
imgGray = cv2.cvtColor(imgs, cv2.COLOR_BGR2GRAY)

#imgBlurred = imgGray
#imgBlurred = cv2.blur(imgGray, (3, 3))
imgBlurred = cv2.GaussianBlur(imgGray, (3,3), 0)
# image seuillage adaptatif (grayscale to black and white)
#imgBlurred=cv2.equalizeHist(imgBlurred)



#imgThresh = cv2.adaptiveThreshold(imgBlurred,                           # image
#                                255,                                  # limiter le plafond a 255 pour les valeurs qui dépassent
#                                cv2.ADAPTIVE_THRESH_GAUSSIAN_C,       # utiliser le gaussian mieu que le moyenneur (mean),
#                                cv2.THRESH_BINARY_INV,                # inverser les black and white, le foreground = white, background = black
#                                3,                                   # taille du voisinage pour calculer le seuil
#                                2)                                    # constant la soustraction de la moyenne avec les les poids


#_ , imgThresh = cv2.threshold(imgBlurred, 200, 255, cv2.THRESH_BINARY)
imgThresh = cv2.Canny(imgBlurred, 220, 255)


kernel = np.ones((3,3),np.uint8)
imgThresh = cv2.dilate(imgThresh,kernel,iterations = 1)
imgThresh = cv2.erode(imgThresh,kernel,iterations = 1)

#imgThresh = cv2.erode(imgThresh,kernel,iterations = 1)
#imgThresh = cv2.dilate(imgThresh,kernel,iterations = 1)


cv2.imshow("contour",imgThresh)

imgThreshCopy = imgThresh.copy()        # copie de l'image seuiller,
npaContours, npaHierarchy = cv2.findContours(imgThreshCopy,             # entrer l'image, utiliser la copie, puisque cette function change cette image au cours de la recherche des contours
                                             cv2.RETR_EXTERNAL,         # utilise seulement les contours externe
                                             cv2.CHAIN_APPROX_SIMPLE)   # compress les segments horizontal, vertical, et diagonal  et laisse les points d'extremeter

value_test=False
for number in npaContours: # parcouris chaque contour
    
    [intX, intY, intWidth, intHeight] = cv2.boundingRect(number)
    fltArea = cv2.contourArea(number)
    ratio=(intWidth)/(intHeight)

    if (fltArea > MIN_CONTOUR_AREA) & (fltArea < MAX_CONTOUR_AREA):        # vérifier la surface
        if (ratio > MIN_RATIO) & (ratio < MAX_RATIO):
            #print('contoure      '+str(fltArea))
            #print("racio         "+str(ratio))
            #print("Width         "+str(intWidth)+"\nHeidth        "+str(intHeight)+"\n \n")            

            cv2.rectangle(imgaffichage,                                        # dessiner un rectangle sur l'image originale
                        (intX, intY),     # coint haut gauche
                        (intX + intWidth, intY + intHeight),      # coin bas droite
                        COLOR_GREEN,              # couleur de ligne verte
                        2)                        # episseur
            
            imgROI = imgs[intY-3 : intY + intHeight+3,intX-3 : intX + intWidth+3]     # couper chaque sous image des etiquette detecter avec leurs taille mais sur l'image seuillée                                               
            images.append((imgROI,intX))                  #j'ai crée un tableau pour contenir tout les sous-images
            
            if (value_test==False):
                value_test=True
                print (intY)

            print("yes \n")

            if  intX < local_mat [0] :
                local_mat [0] =intX
            if intY < local_mat [1] :
                local_mat [1] =intY
            if  intX + intWidth > local_mat [2] :
                local_mat [2] =intX + intWidth
            if intY +intHeight > local_mat [3] :
                local_mat [3] =intY +intHeight
        else:
            print ("\n ------ ratio \nintY : "+str(intY))
            print ("intX : "+str(intX))
            print ("ratio : "+str(ratio))
            print ("fltArea : "+str(fltArea))
    else:
        print ("\n ------ fltArea( \nintY : "+str(intY))
        print ("intX : "+str(intX))
        print ("ratio : "+str(ratio))
        print ("fltArea : "+str(fltArea))
    


cv2.rectangle(imgaffichage,                                        # dessiner un rectangle sur l'image originale
                        (local_mat [0] -5 , local_mat [1] -5 ),     # coint haut gauche
                        (local_mat [2] +5 , local_mat [3] +5 ),      # coin bas droite
                        COLOR_RED,              # couleur de ligne verte
                        2)                        # episseur



                        ##############  4 ligne

cv2.imshow("image",imgaffichage)

numbers = sorted(images, key=lambda nmbr: nmbr[1] , reverse = True)
i=0

for nmr in numbers:    
    #cv2.imshow(str(i) ,nmr[0])
    if len(nmr[0])!=0:
        
        img1 = cv2.resize(nmr[0], (60,30),interpolation = cv2.INTER_AREA)
        img1 = cv2.GaussianBlur(img1, (5,5), 0)
        img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
        
        img2 = cv2.adaptiveThreshold(img1,                           # image
                                    255,                                  # limiter le plafond a 255 pour les valeurs qui dépassent
                                    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,       # utiliser le gaussian mieu que le moyenneur (mean),
                                    cv2.THRESH_BINARY_INV,                # inverser les black and white, le foreground = white, background = black
                                    7,                                   # taille du voisinage pour calculer le seuil
                                    2)   
        # Copy the thresholded image.
        im_floodfill = img2.copy()

        # Mask used to flood filling.
        # Notice the size needs to be 2 pixels than the image.
        h, w = img2.shape[:2]
        mask = np.zeros((h+2, w+2), np.uint8)

        # Floodfill from point (0, 0)
        cv2.floodFill(im_floodfill, mask, (0,0), 255);

        # Invert floodfilled image
        im_floodfill_inv = cv2.bitwise_not(im_floodfill)

        # Combine the two images to get the foreground.
        im_out = img2 | im_floodfill_inv

        kernel = np.ones((3,3),np.uint8)
        im_out = cv2.dilate(im_out,kernel,iterations = 1)
        im_out = cv2.erode(im_out,kernel,iterations = 1)
        
        im_out = cv2.erode(im_out,kernel,iterations = 1)
        im_out = cv2.dilate(im_out,kernel,iterations = 1)

        
        #cv2.imshow(str(i)+"  " ,im_out)
        
        cntt, _ = cv2.findContours(im_out,             # entrer l'image, utiliser la copie, puisque cette function change cette image au cours de la recherche des contours
                                cv2.RETR_EXTERNAL,         # utilise seulement les contours externe
                                cv2.CHAIN_APPROX_SIMPLE)   # compress les segments horizontal, vertical, et diagonal  et laisse les points d'extremeter

        print ("\n number "+ str(i))
        for ii in cntt: 
            fltArea = cv2.contourArea(ii)
            if fltArea > 30:
                print('contoure      '+str(fltArea))

        #cv2.imshow(str(i) ,img2)


        i+=1
cv2.waitKey(200000)
 """

def image(img):

    images= []
    for sss in images:
        del(sss)
    #### ces just pour a chaque fois quand on termine limage on efface le resultat du tableuau

    imgs = cv2.resize(img, (1024,438 ),interpolation = cv2.INTER_AREA)

    imgaffichage=imgs.copy()         ##################################################################################################
    ## une copy pour l affichege 
    imgGray = cv2.cvtColor(imgs, cv2.COLOR_BGR2GRAY)
    # convertire to gray
    imgBlurred = cv2.GaussianBlur(imgGray, (3,3), 0)
    # blury limage avec filter gaussian
    imgThresh = cv2.Canny(imgBlurred, 220, 255)
    ## affecter contoure canny
    #cv2.imshow("imgThresh",imgThresh)       ##################################################################################################
    

    kernel = np.ones((3,3),np.uint8)
    imgThresh = cv2.dilate(imgThresh,kernel,iterations = 1)
    imgThresh = cv2.erode(imgThresh,kernel,iterations = 1)

    #cv2.imshow("contour",imgThresh)

    imgThreshCopy = imgThresh.copy()
    ## faire un coppy a limage psq methode find contoure tfezed tswira  
    npaContours, npaHierarchy = cv2.findContours(imgThreshCopy,             # entrer l'image, utiliser la copie, puisque cette function change cette image au cours de la recherche des contours
                                             cv2.RETR_EXTERNAL,         # utilise seulement les contours externe
                                             cv2.CHAIN_APPROX_SIMPLE)   # compress les segments horizontal, vertical, et diagonal  et laisse les points d'extremeter
    ## detect all contoure externe
    for number in npaContours: 
        ## for tout les contoures
        [intX, intY, intWidth, intHeight] = cv2.boundingRect(number)
        ## extract les cordonnée ta 2 point li f les coins ta3 l contoure
        fltArea = cv2.contourArea(number)
        ## nahssbou area ta3 l contoure 
        ratio=(intWidth)/(intHeight)
        ## nahssbou ratio
        if (fltArea > MIN_CONTOUR_AREA) & (fltArea < MAX_CONTOUR_AREA):
            ## nahiw les contoure sghar li ma andhm hata ma3na 
            ## ma drtch bl max 3lajal tssawr kayn matricule b3id w kayn grib
            if (ratio > MIN_RATIO) & (ratio < MAX_RATIO) :             
                ## nzidou nfiltriw b ratio
                cv2.rectangle(imgaffichage,
                            (intX, intY),
                            (intX + intWidth, intY + intHeight)
                            ,COLOR_GREEN,
                            1)
                ##################################################################################################
                ## norssm mouraba3 3la l ra9m
                imgROI = imgBlurred[intY-3 : intY + intHeight+3,intX-3 : intX + intWidth+3] 
                ## n9oss ra9m w nzidlou 6 b dour ta3ou kaml

     ##################################################################################################
                images.append((imgROI,intX))     
                ## najoutih f tableau 

     
    #cv2.imshow(path,imgaffichage)  
    numbers= []

    for nnn in numbers:
        del(nnn)
    

    numbers = sorted(images, key=lambda nmbr: nmbr[1] , reverse = True)
    ## bah nratabhm
    ## cv2.waitKey(100)
    ##################################################################################################


    i=0
    tab_image=[]
    for nmr in numbers:
         ## n3awd noarkourihm akoul madamhm mratbin

        if len(nmr[0])!=0:
            ## lkan mahouch fargh
            ## yglbou b taille fix 
            img1 = cv2.resize(nmr[0], TAILLE_IMAGE_NOMBRE,interpolation = cv2.INTER_AREA)
            img2 = cv2.adaptiveThreshold(img1,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,7,2)  
            ## n3awdou nbinariziwhm psq am f niveau gray 
            kernel = np.ones((3,3),np.uint8)

            im_out = cv2.erode(img2,kernel,iterations = 1)
            im_out = cv2.dilate(im_out,kernel,iterations = 1)
            ##nahiw l bruit

            im_out = cv2.dilate(im_out,kernel,iterations = 2)
            im_out = cv2.erode(im_out,kernel,iterations = 2)
            ## namlaw l bruit li finoss ar9am

            cv2.imshow(str(i)+"  " ,im_out)       ##################################################################################################
            cv2.imshow(str(i) ,img2)      ##################################################################################################
            #cv2.imwrite('./bdd/'+'FHD00'+str(image_fin)+' - '+str(i)+'.JPG' ,im_out)      ##################################################################################################
            i+=1    
            ## ponteur 3lajal le nom ta tssawr brk
            tab_image.append(im_out)

    return tab_image






imgs=cv2.imread('./img.jpg')

image(imgs)