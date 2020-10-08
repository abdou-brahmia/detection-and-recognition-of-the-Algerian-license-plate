import cv2
import extract_matrecule.Main as extr_mat
import recon_number.csv.main_s as recon_number
import module_bdd.module_bdd as bdd
img=cv2.imread('img.jpg')
print(img.shape)
a=extr_mat.image(img)
print("number detected is "+str(len(a)))
s=""
for i in a :
    s+= str ( recon_number.methodee(i.copy())    )
    cv2.imshow("image",i)
    cv2.waitKey(0)

print (int(s))

bdd.ajouter_voiture_entrer(int(s))