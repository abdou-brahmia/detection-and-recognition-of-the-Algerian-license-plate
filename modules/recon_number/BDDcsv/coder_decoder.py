import csv
import cv2
import numpy as np
import os

def csv_to_img(csv_file,nom_file_img):
    
    with open(csv_file, mode='r') as file:
        reader = csv.reader(file)
        lignes = list(reader)
        for element in lignes:
            tab  =np.asarray(element)
            image=np.zeros((60,40),dtype=np.uint8)
            for w in range (60):
                for h in range (40):
                    image[w,h]=tab[(w*40+h)]
  

def read_bdd(i):
    path=""
    if i ==2:
        path="./modules/recon_number/BDDcsv/BDD1.txt"
    elif i==4:
        path="./modules/recon_number/BDDcsv/BDD2.txt"
    with open(path, mode='r') as file:
        reader = csv.reader(file)
        all_numbers=[]
        
        lignes = list(reader)
        for element in lignes:
            tab  =np.asarray(element)
            image=np.zeros((int(tab[1]),int(tab[2])),dtype=np.uint8)
            for h in range (int(tab[1])):
                for w in range (int(tab[2])):
                    image[h,w]=tab[(h*int(tab[2])+w+3)]
  
            all_numbers.append([tab[0],image])
    return all_numbers


