# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtCore import QByteArray, qFuzzyCompare, Qt, QTimer, QDateTime
from PyQt5.QtWidgets import (QAction, QActionGroup, QApplication, QDialog,
        QMainWindow, QMessageBox)
from PyQt5 import QtWidgets, uic, QtCore, QtGui

import cv2
import numpy as np
import serial
import time

import threading
from datetime import datetime
import modules.xml.module_xml as module_xml
from PyQt5.QtMultimedia import (QAudioEncoderSettings, QCamera,
        QCameraImageCapture, QImageEncoderSettings, QMediaMetaData,
        QMediaRecorder, QMultimedia, QVideoEncoderSettings)
import modules.recon_number.main as recon_number
import modules.detection_car.main as detection_car
import modules.extract_matrecule.Main as extract_matrecule
import modules.gestion_bdd.Main as gestion_bdd

SCALAR_BLACK = (0.0, 0.0, 0.0)
SCALAR_WHITE = (255.0, 255.0, 255.0)
SCALAR_YELLOW = (0.0, 255.0, 255.0)
SCALAR_GREEN = (0.0, 255.0, 0.0)
SCALAR_RED = (0.0, 0.0, 255.0)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow,w,h):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(w, h)
    
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, w-20, h-20))
        self.label.setText("")
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 330, h-20))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")

        #1
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(10,10, 150,30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(170,10, 150,30))
        self.pushButton_2.setObjectName("pushButton_2")
        #2
        #self.comboBox = QtWidgets.QComboBox(self.groupBox)
        #self.comboBox.setGeometry(QtCore.QRect(10,50, 310,30))
        #self.comboBox.setObjectName("comboBox")
        #3
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_3.setGeometry(QtCore.QRect(10,90, 150,30))
        self.checkBox_3.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_2.setGeometry(QtCore.QRect(170,90, 150,30))
        self.checkBox_2.setObjectName("checkBox_2")
        #4
        self.checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox.setGeometry(QtCore.QRect(10,130, 150,30))
        self.checkBox.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_4.setGeometry(QtCore.QRect(170,130, 150,30))
        self.checkBox_4.setObjectName("checkBox_4")
        #5
        self.checkBox_5 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_5.setGeometry(QtCore.QRect(10,170, 150,30))
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_6 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_6.setGeometry(QtCore.QRect(170,170, 150,30))
        self.checkBox_6.setObjectName("checkBox_6")
        #6
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 220, 310,30))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton.setGeometry(QtCore.QRect(0, 0, 150, 30))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_2.setGeometry(QtCore.QRect(160, 0, 150, 30))
        self.radioButton_2.setObjectName("radioButton_2")
        #7
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 260, 310,30))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_3.setGeometry(QtCore.QRect(0, 0, 150, 30))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_4.setGeometry(QtCore.QRect(160, 0, 150, 30))
        self.radioButton_4.setObjectName("radioButton_4")
        #8
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 300, 310,30))
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox")
        self.radioButton_7 = QtWidgets.QRadioButton(self.groupBox_5)
        self.radioButton_7.setGeometry(QtCore.QRect(0, 0, 150, 30))
        self.radioButton_7.setObjectName("radioButton_7")
        self.radioButton_8 = QtWidgets.QRadioButton(self.groupBox_5)
        self.radioButton_8.setGeometry(QtCore.QRect(160, 0, 150, 30))
        self.radioButton_8.setObjectName("radioButton_8")
        #9
        #10
        self.label_1 = QtWidgets.QLabel(self.groupBox)
        self.label_1.setGeometry(QtCore.QRect(10, 380, 240,30))
        self.label_1.setObjectName("label")
        self.spinBox = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox.setGeometry(QtCore.QRect(260, 380, 60,30))
        self.spinBox.setObjectName("spinBox")
        self.spinBox.setMaximum(99)
        #11
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 420, 240,30))
        self.label_2.setObjectName("label_2")
        self.spinBox_2 = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_2.setGeometry(QtCore.QRect(260, 420, 60,30))
        self.spinBox_2.setObjectName("spinBox_2")
        self.spinBox_2.setMaximum(999)
        #12
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 460, 240,30))
        self.label_3.setObjectName("label_3")
        self.spinBox_3 = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_3.setGeometry(QtCore.QRect(260, 460, 60,30))
        self.spinBox_3.setObjectName("spinBox_3")
        self.spinBox_3.setMaximum(999)
        #14
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 500, 240,30))
        self.label_4.setObjectName("label_4")
        self.spinBox_4 = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_4.setGeometry(QtCore.QRect(260, 500, 60,30))
        self.spinBox_4.setObjectName("spinBox_4")
        self.spinBox_4.setMaximum(99999)
        



        self.groupBox_8 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_8.setGeometry(QtCore.QRect(350, 10, 240, 240))
        self.groupBox_8.setTitle("")
        self.groupBox_8.setObjectName("groupBox_8")
        self.textEdit_5 = QtWidgets.QTextEdit(self.groupBox_8)
        self.textEdit_5.setGeometry(QtCore.QRect(20, 20, 191, 31))
        self.textEdit_5.setObjectName("textEdit_5")
        self.textEdit_6 = QtWidgets.QTextEdit(self.groupBox_8)
        self.textEdit_6.setGeometry(QtCore.QRect(20, 60, 191, 31))
        self.textEdit_6.setObjectName("textEdit_6")
        self.textEdit_7 = QtWidgets.QTextEdit(self.groupBox_8)
        self.textEdit_7.setGeometry(QtCore.QRect(20, 140, 191, 31))
        self.textEdit_7.setObjectName("textEdit_7")
        self.textEdit_8 = QtWidgets.QTextEdit(self.groupBox_8)
        self.textEdit_8.setGeometry(QtCore.QRect(20, 100, 191, 31))
        self.textEdit_8.setObjectName("textEdit_8")
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox_8)
        self.pushButton_8.setGeometry(QtCore.QRect(70, 190, 86, 31))
        self.pushButton_8.setObjectName("pushButton_8")
        self.groupBox_8.hide()



        self.groupBox_9 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_9.setGeometry(QtCore.QRect(350, 270 , 240, 100))
        self.groupBox_9.setTitle("")
        self.groupBox_9.setObjectName("groupBox_9")
        self.textEdit_4 = QtWidgets.QTextEdit(self.groupBox_9)
        self.textEdit_4.setGeometry(QtCore.QRect(20, 10, 191, 31))
        self.textEdit_4.setObjectName("textEdit_4")
        self.pushButton_9 = QtWidgets.QPushButton(self.groupBox_9)
        self.pushButton_9.setGeometry(QtCore.QRect(70, 50, 86, 31))
        self.pushButton_9.setObjectName("pushButton_9")
        self.groupBox_9.hide()



        self.groupBox_10 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_10.setGeometry(QtCore.QRect(350, 380 , 240, 100))
        self.groupBox_10.setTitle("")
        self.groupBox_10.setObjectName("groupBox_10")
        self.textEdit_10 = QtWidgets.QTextEdit(self.groupBox_10)
        self.textEdit_10.setGeometry(QtCore.QRect(20, 10, 191, 31))
        self.textEdit_10.setObjectName("textEdit_10")
        self.pushButton_10 = QtWidgets.QPushButton(self.groupBox_10)
        self.pushButton_10.setGeometry(QtCore.QRect(70, 50, 86, 31))
        self.pushButton_10.setObjectName("pushButton_10")
        self.groupBox_10.hide()



        self.textEdit_4.setPlaceholderText("Serial Number")
        self.textEdit_5.setPlaceholderText("Serial Number")
        self.textEdit_6.setPlaceholderText("Last Name")
        self.textEdit_7.setPlaceholderText("Phone Number")
        self.textEdit_8.setPlaceholderText("First Name")
        self.textEdit_10.setPlaceholderText("Serial Number")


        #13
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(10,540, 310,30))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4.setGeometry(QtCore.QRect(10,580, 310,30))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_5.setGeometry(QtCore.QRect(10,660, 310,30))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_6.setGeometry(QtCore.QRect(10,620, 310,30))
        self.pushButton_6.setObjectName("pushButton_6")







        MainWindow.setCentralWidget(self.centralwidget)


        self.groupBox.hide()
        
        self.label.mousePressEvent =self.etat_panel
        self.label.setStyleSheet("background-color: rgba(0,0,0,0);")
        self.groupBox.setStyleSheet("background-color: rgba(90, 90, 90, 90);")
        self.groupBox_2.setStyleSheet("background-color: rgba(0,0,0,0);")
        self.groupBox_3.setStyleSheet("background-color: rgba(0,0,0,0);")
        self.groupBox_8.setStyleSheet("background-color: rgba(90, 90, 90, 90);")
        self.groupBox_9.setStyleSheet("background-color: rgba(90, 90, 90, 90);")
        self.groupBox_10.setStyleSheet("background-color: rgba(90, 90, 90, 90);")
        self.groupBox_5.setStyleSheet("background-color: rgba(0,0,0,0);")
        
        self.checkBox.setStyleSheet("background-color: rgba(90, 90, 90, 90);")
        self.checkBox_2.setStyleSheet("background-color: rgba(90, 90, 90, 90);")
        self.checkBox_3.setStyleSheet("background-color: rgba(90, 90, 90, 90);")
        self.checkBox_4.setStyleSheet("background-color: rgba(90, 90, 90, 90);")
        self.checkBox_5.setStyleSheet("background-color: rgba(90, 90, 90, 90);")
        self.checkBox_6.setStyleSheet("background-color: rgba(90, 90, 90, 90);")
        self.radioButton.setStyleSheet("background-color: rgba(90, 90, 90, 90);")
        self.radioButton_2.setStyleSheet("background-color: rgba(90, 90, 90, 90);")
        self.radioButton_3.setStyleSheet("background-color: rgba(90, 90, 90, 90);")
        self.radioButton_4.setStyleSheet("background-color: rgba(90, 90, 90, 90);")
        self.radioButton_7.setStyleSheet("background-color: rgba(90, 90, 90, 90);")
        self.radioButton_8.setStyleSheet("background-color: rgba(90, 90, 90, 90);")
        #self.pushButton.setStyleSheet("background-color: rgba(90, 90, 90, 90);")
        #self.setWindowOpacity(0.8) 
        self.label.setToolTip('click to change setup')
        self.getConfigurationInterface()
        self.checkBox.clicked.connect(lambda: self.setConfigurationInterface("modifer/DisplayGray",self.checkBox.isChecked()) )
        self.checkBox_2.clicked.connect(lambda: self.setConfigurationInterface("modifer/DisplayHeurAndDate",self.checkBox_2.isChecked()) )
        self.checkBox_3.clicked.connect(lambda: self.setConfigurationInterface("type",self.checkBox_3.isChecked()) )
        self.checkBox_4.clicked.connect(lambda: self.setConfigurationInterface("modifer/Threading",self.checkBox_4.isChecked()) )
        self.checkBox_5.clicked.connect(lambda: self.setConfigurationInterface("modifer/DisplayMatborder",self.checkBox_5.isChecked()) )
        self.checkBox_6.clicked.connect(lambda: self.setConfigurationInterface("modifer/DisplayMatNum",self.checkBox_6.isChecked()) )
        self.radioButton.clicked.connect(lambda: self.setConfigurationInterface("modifer/ColorYcrcbOrGray",True))
        self.radioButton_2.clicked.connect(lambda: self.setConfigurationInterface("modifer/ColorYcrcbOrGray",False))
        self.radioButton_3.clicked.connect(lambda: self.setConfigurationInterface("modifer/BDDCsvImages",True))
        self.radioButton_4.clicked.connect(lambda: self.setConfigurationInterface("modifer/BDDCsvImages",False))
        self.radioButton_7.clicked.connect(lambda: self.setConfigurationInterface("modifer/BDD",True))
        self.radioButton_8.clicked.connect(lambda: self.setConfigurationInterface("modifer/BDD",False))
        self.pushButton.clicked.connect(self.start)
        self.pushButton_2.clicked.connect(self.stop)
        self.pushButton_3.clicked.connect(self.newclient)
        self.pushButton_4.clicked.connect(self.manualcarlogin)
        self.pushButton_5.clicked.connect(self.majBackground)
        self.pushButton_6.clicked.connect(self.deleteclient)
        self.pushButton_8.clicked.connect(self.newclient_methode)
        self.pushButton_9.clicked.connect(self.manualcarlogin_methode_2)
        self.pushButton_10.clicked.connect(self.deleteclient_methode)


        self.type_bdd=1
        self.typecolor=1
        video='./Vedeo/test2.mov'
        #self.cap = cv2.VideoCapture(0)
        self.cap=cv2.VideoCapture(video)
        self.stateBackground=False
        self.timercam = QTimer()
        self.timercam.timeout.connect(self.vedeo)
        self.resolution=(480,240)
        self.ser = serial.Serial('/dev/ttyACM0', 9800)




        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PFE"))
        self.pushButton.setText(_translate("MainWindow", "Start"))
        self.pushButton_2.setText(_translate("MainWindow", "Stop"))
        self.checkBox.setText(_translate("MainWindow", "Display on Gray"))
        self.checkBox_2.setText(_translate("MainWindow", "Display Heur/Date"))
        self.checkBox_3.setText(_translate("MainWindow", "Default Config"))
        self.checkBox_4.setText(_translate("MainWindow", "Threading"))
        self.checkBox_5.setText(_translate("MainWindow", "Display border"))
        self.checkBox_6.setText(_translate("MainWindow", "Display SerialNumber"))

        self.radioButton.setText(_translate("MainWindow", "Use Y Color"))
        self.radioButton_2.setText(_translate("MainWindow", "Use Gray Color"))
        self.radioButton_3.setText(_translate("MainWindow", "Use Format CSV"))
        self.radioButton_4.setText(_translate("MainWindow", "Use Format Images"))

        self.radioButton_7.setText(_translate("MainWindow", "Our BDD"))
        self.radioButton_8.setText(_translate("MainWindow", "Imported BDD"))

        self.pushButton_3.setText(_translate("MainWindow", "Ajoute Client"))
        self.pushButton_4.setText(_translate("MainWindow", "Manual Insert"))
        self.pushButton_5.setText(_translate("MainWindow", "Update Background"))
        self.pushButton_6.setText(_translate("MainWindow", "Delete Client"))
        self.label_1.setText(_translate("MainWindow", "Seuille Update"))
        self.label_2.setText(_translate("MainWindow", "Seuille detection 1")) #SEILLE_PIXEL
        self.label_3.setText(_translate("MainWindow", "Seuille detection 2")) #SEILLE_IMAGE
        self.label_4.setText(_translate("MainWindow", "Seuille detection 3")) #SEILLE de detection 3 
        

        self.pushButton_8.setText(_translate("MainWindow", "Add"))
        self.pushButton_9.setText(_translate("MainWindow", "Insert"))
        self.pushButton_10.setText(_translate("MainWindow", "Delete"))
        
        
    def etat_panel(self,even):
        if self.groupBox.isVisible():
            self.groupBox.hide()
            self.groupBox_8.hide()
            self.groupBox_9.hide()
            self.groupBox_10.hide()
        else:
            self.groupBox.show()

    def start(self):
        self.timercam.start(10)
    def stop(self):
        self.timercam.stop()
        
    def newclient(self):
        self.groupBox_8.show()

    def manualcarlogin(self):
        self.groupBox_9.show()
    def majBackground(self):
        self.stateBackground=False
    def deleteclient(self):
        self.groupBox_10.show()
    
    def deleteclient_methode(self):
        matrecule = str( self.textEdit_10.toPlainText())
        self.textEdit_10.setText("")
        
        msg = QMessageBox()
        msg.setWindowTitle("delete client")
        if len(matrecule) ==10 and matrecule.isnumeric():
            val =gestion_bdd.suprimer_voiture(matrecule)
        
            if val == 1:
                msg.setText("delete avec successe !")
                msg.setIcon(QMessageBox.Information)

            elif val == 2 :
                msg.setText("nexiste pas dans la base!")
                msg.setIcon(QMessageBox.Warning)

            elif  val==3:
                msg.setText("erreur bas de donnée connexion ")
                msg.setIcon(QMessageBox.Critical)

        else:
            msg.setText("erreur Serial number incorecte")
            msg.setIcon(QMessageBox.Critical)
        
        self.groupBox_10.hide()

        x = msg.exec_()  

    def manualcarlogin_methode(self):
        matrecule = str( self.textEdit_4.toPlainText())
        self.textEdit_4.setText("")
        
        msg = QMessageBox() 
        msg.setWindowTitle("login client")
        if len(matrecule) ==10 and matrecule.isnumeric():
            val =gestion_bdd.ajouter_voiture_entrer(matrecule)
        
            if val == 1:
                msg.setText("ajoute avec successe !")
                msg.setIcon(QMessageBox.Information)
                return True
            elif val == 2 :
                msg.setText("nexiste pas dans la base!")
                msg.setIcon(QMessageBox.Warning)
                return False
            elif  val==3:
                msg.setText("erreur bas de donnée connexion ")
                msg.setIcon(QMessageBox.Critical)
                return False
        else:
            msg.setText("erreur matricule incorecte")
            msg.setIcon(QMessageBox.Critical)
            return False
        self.groupBox_9.hide()

        x = msg.exec_()  
    
    def manualcarlogin_methode_2(self):
        a=self.manualcarlogin_methode()
    def newclient_methode(self):
        matrecule = str( self.textEdit_5.toPlainText())
        nom = str (self.textEdit_6.toPlainText())
        prenom = str (self.textEdit_8.toPlainText())
        nmr = str( self.textEdit_7.toPlainText())
        self.textEdit_5.setText("")
        self.textEdit_6.setText("")
        self.textEdit_7.setText("")
        self.textEdit_8.setText("")
        
        msg = QMessageBox()
        msg.setWindowTitle("New client")

        if len(matrecule) ==10 and matrecule.isnumeric():
            val=gestion_bdd.ajouter_voiture(matrecule,nom,prenom,nmr)
    
            
            if val == 1:
                msg.setText("ajoute avec successe !")
                msg.setIcon(QMessageBox.Information)


            elif  val==3:
                msg.setText("erreur bas de donnée connexion ")
                msg.setIcon(QMessageBox.Critical)

        else:
            msg.setText("erreur matricule incorecte")
            msg.setIcon(QMessageBox.Critical)
        
        self.groupBox_8.hide()
        x = msg.exec_()

    def affiche(self,image):
        image_temp=cv2.cvtColor(image,cv2.COLOR_BGR2RGB) 
        height, width, channels = image_temp.shape
        bytesPerLine = channels * width
        qImg = QtGui.QImage(image_temp.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888)
        pixmap01 = QtGui.QPixmap.fromImage(qImg)
        pixmap_image = QtGui.QPixmap(pixmap01)

        self.label.setPixmap(pixmap_image)
        self.label.setScaledContents(True)
       
    def simplest_cb(self,img, percent):
        out_channels = []
        channels = cv2.split(img)
        totalstop = channels[0].shape[0] * channels[0].shape[1] * percent / 200.0
        for channel in channels:
            bc = np.bincount(channel.ravel(), minlength=256)
            lv = np.searchsorted(np.cumsum(bc), totalstop)
            hv = 255-np.searchsorted(np.cumsum(bc[::-1]), totalstop)
            out_channels.append(cv2.LUT(channel, np.array(tuple(0 if i < lv else 255 if i > hv else round((i-lv)/(hv-lv)*255) for i in np.arange(0, 256)), dtype="uint8")))
        return cv2.merge(out_channels)


    def vedeo(self):
        
        if self.stateBackground==False:
            self.background= detection_car.take_back_ground_debut(self.cap,self.resolution,self.NombreFrameMaj)

            self.stateBackground=True
        for cont in range(9):
            ret,self.image = self.cap.read()
            if ret==False:
                self.timercam.stop()
                self.cap.release()
                cv2.destroyAllWindows()
                break            
 
        if not(type(self.image)==type(None)):            
            self.image=cv2.resize(self.image,(1280,720), interpolation = cv2.INTER_AREA)

            detection_car_result=detection_car.detectCar(self.image,self.background,self.resolution,self.SEILLE_PIXEL,self.SEILLE_IMAGE,self.SEILLE_IMAGE_2)
            self.image_after_processing=self.processing(self.image) 

            if detection_car_result[0]==True:
     
                a=720/240
                b=1280/480
                [intX, intY, intWidth, intHeight]=detection_car_result[1]
                intX=int(b*intX)
                intY=int(a*intY)
                intWidth=int(intWidth*b)
                intHeight=int(intHeight*a)
                img_traiter=self.image[intY :intY+intHeight,intX:intX+intWidth ]

                if (self.radioButton_2.isChecked()):
                    self.typecolor=1
                elif (self.radioButton.isChecked()):
                    self.typecolor=2
     
                state = extract_matrecule.image(img_traiter,self.typecolor)

                if state[0]==True:
                    numbers=state[1]

                    if (self.radioButton_7.isChecked()):                        
                        if (self.radioButton_4.isChecked()):
                            self.type_bdd=1                    #1 my bdd images
                        elif (self.radioButton_3.isChecked()):
                            self.type_bdd=2                    #2 my bdd csv
                    elif (self.radioButton_8.isChecked()):
                        if (self.radioButton_4.isChecked()):
                            self.type_bdd=3                    #3 bdd net images
                        elif (self.radioButton_3.isChecked()):
                            self.type_bdd=4                    #4 bdd net csv

                    bdd=recon_number.read_bdd(self.type_bdd)


                    local_mat=[10000,10000,0,0]
                    s=""
                    valx=intX
                    valy=intY
                        
                    if self.checkBox_4.isChecked():
                        ab=recon_number.recon_number_th(numbers,self.image,bdd)
                        local_mat=ab[1]
                        for m in ab[0]:
                            s+=m
                    else:
                        for nmbr in numbers:
                            
                            [intX, intY, intWidth, intHeight]=nmbr
                            nmrImage=cv2.cvtColor(img_traiter[intY :intY+intHeight,intX:intX+intWidth ],cv2.COLOR_BGR2GRAY)
                            nmrImage=self.simplest_cb(nmrImage,1)
                            mmmm=str(recon_number.is_number(nmrImage,bdd))
                            s+=mmmm

                            if  intX < local_mat [0] :
                                local_mat [0] =intX
                            if intY < local_mat [1] :
                                local_mat [1] =intY
                            if  intX + intWidth > local_mat [2] :
                                local_mat [2] =intX + intWidth
                            if intY +intHeight > local_mat [3] :
                                local_mat [3] =intY +intHeight


                    font = cv2.FONT_HERSHEY_SIMPLEX
                    
                    if (self.checkBox_6.isChecked()):
                        cv2.putText(self.image_after_processing,s,(local_mat [0] +valx , local_mat [1] -20+valy ), font, 1,(0,0,255),2)
                    else:
                        cv2.putText(self.image_after_processing,"detected",(local_mat [0] +valx , local_mat [1] -20+valy ), font, 1,(0,0,255),2)
                    
                    if (self.checkBox_6.isChecked()):
                        cv2.rectangle(self.image_after_processing
                            ,(local_mat [0] -5 +valx , local_mat [1] -5+valy )     # coint haut gauche
                            ,(local_mat [2] +5+valx , local_mat [3] +5 +valy)
                            , (0,0,255)
                            , 2)
          
                    self.textEdit_4.setText(s)
                    state_3=self.manualcarlogin_methode()
                    

                    if state_3==True:
                        

                        self.ser.write(b'H')
                        state_a=False
                        while (not(state_a)):
                            
                            b = self.ser.readline()
                            str_rn = b.decode()
                            str_end = str_rn.rstrip()
                            if (str_end=="1"):
                                state_a=True

                                


            self.affiche(self.image_after_processing)
            self.timercam.start(10)

    def processing(self,image):
        image_inter_processing=image
        if (self.checkBox.isChecked()):
            image_inter_processing=cv2.cvtColor(image_inter_processing,cv2.COLOR_RGB2GRAY)
        
        if (self.checkBox_2.isChecked()):
            current_Date = datetime.now()
            date_now = current_Date.strftime('%Y-%m-%d')
            time_now = current_Date.strftime('%H:%M:%S')
            cv2.putText(image_inter_processing, date_now, (1100,20),cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, SCALAR_RED,1)
            cv2.putText(image_inter_processing, time_now, (1100,40),cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, SCALAR_RED,1)
        if (len(image_inter_processing.shape)==2):
            image_inter_processing=cv2.cvtColor(image_inter_processing,cv2.COLOR_GRAY2RGB)
        
        return image_inter_processing

    def getConfigurationInterface(self):
        
        typeConfiguration=module_xml.get_Val("type")
        if typeConfiguration==1:
            self.checkBox_3.setChecked(True)


            if module_xml.get_Val("default/DisplayGray")==1:
                self.checkBox.setChecked(True)
            else:
                self.checkBox.setChecked(False)
            if module_xml.get_Val("default/DisplayHeurAndDate")==1:
                self.checkBox_2.setChecked(True)
            else:
                self.checkBox_2.setChecked(False)
            if module_xml.get_Val("default/Threading")==1:
                self.checkBox_4.setChecked(True)
            else:
                self.checkBox_4.setChecked(False)
            if module_xml.get_Val("default/DisplayMatborder")==1:
                self.checkBox_5.setChecked(True)
            else:
                self.checkBox_5.setChecked(False)
            if module_xml.get_Val("default/DisplayMatNum")==1:
                self.checkBox_6.setChecked(True)
            else:
                self.checkBox_6.setChecked(False)
            if module_xml.get_Val("default/ColorYcrcbOrGray")==1:
                self.radioButton.setChecked(True)
            else:
                self.radioButton_2.setChecked(True)
            if module_xml.get_Val("default/BDDCsvImages")==1:
                self.radioButton_3.setChecked(True)
            else:
                self.radioButton_4.setChecked(True)
            if module_xml.get_Val("default/BDD")==1:
                self.radioButton_7.setChecked(True)
            else:
                self.radioButton_8.setChecked(True)

            self.NombreFrameMaj = module_xml.get_Val("default/NombreFrameMaj")
            self.spinBox.setValue(self.NombreFrameMaj)            
            self.SEILLE_PIXEL = module_xml.get_Val("default/SEILLE_PIXEL")
            self.spinBox_2.setValue(self.SEILLE_PIXEL)
            self.SEILLE_IMAGE = module_xml.get_Val("default/SEILLE_IMAGE")
            self.spinBox_3.setValue(self.SEILLE_IMAGE )
            self.SEILLE_IMAGE_2 = module_xml.get_Val("default/SEILLE_IMAGE_2")
            self.spinBox_4.setValue(self.SEILLE_IMAGE_2 )
            
            self.checkBox.setEnabled(False)
            self.checkBox_2.setEnabled(False)
            self.checkBox_4.setEnabled(False)
            self.checkBox_5.setEnabled(False)
            self.checkBox_6.setEnabled(False)
            self.radioButton.setEnabled(False)
            self.radioButton_2.setEnabled(False)
            self.radioButton_3.setEnabled(False)
            self.radioButton_4.setEnabled(False)
            self.radioButton_7.setEnabled(False)
            self.radioButton_8.setEnabled(False)
            


            self.spinBox.setEnabled(False)
            self.spinBox_2.setEnabled(False)
            self.spinBox_3.setEnabled(False)
            self.spinBox_4.setEnabled(False)
            

            
        elif typeConfiguration==0:
            self.checkBox_3.setChecked(False)

            if module_xml.get_Val("modifer/DisplayGray")==1:
                self.checkBox.setChecked(True)
            else:
                self.checkBox.setChecked(False)
            if module_xml.get_Val("modifer/DisplayHeurAndDate")==1:
                self.checkBox_2.setChecked(True)
            else:
                self.checkBox_2.setChecked(False)
            if module_xml.get_Val("modifer/Threading")==1:
                self.checkBox_4.setChecked(True)
            else:
                self.checkBox_4.setChecked(False)
            if module_xml.get_Val("modifer/DisplayMatborder")==1:
                self.checkBox_5.setChecked(True)
            else:
                self.checkBox_5.setChecked(False)
            if module_xml.get_Val("modifer/DisplayMatNum")==1:
                self.checkBox_6.setChecked(True)
            else:
                self.checkBox_6.setChecked(False)
            if module_xml.get_Val("modifer/ColorYcrcbOrGray")==1:
                self.radioButton.setChecked(True)
            else:
                self.radioButton_2.setChecked(True)
            if module_xml.get_Val("modifer/BDDCsvImages")==1:
                self.radioButton_3.setChecked(True)
            else:
                self.radioButton_4.setChecked(True)
            if module_xml.get_Val("modifer/BDD")==1:
                self.radioButton_7.setChecked(True)
            else:
                self.radioButton_8.setChecked(True)

            self.NombreFrameMaj = module_xml.get_Val("modifer/NombreFrameMaj")
            self.spinBox.setValue(self.NombreFrameMaj)            
            self.SEILLE_PIXEL = module_xml.get_Val("modifer/SEILLE_PIXEL")
            self.spinBox_2.setValue(self.SEILLE_PIXEL)
            self.SEILLE_IMAGE = module_xml.get_Val("modifer/SEILLE_IMAGE")
            self.spinBox_3.setValue(self.SEILLE_IMAGE )
            self.SEILLE_IMAGE_2 = module_xml.get_Val("modifer/SEILLE_IMAGE_2")
            self.spinBox_4.setValue(self.SEILLE_IMAGE_2 )
            
            
            self.spinBox.setEnabled(True)
            self.spinBox_2.setEnabled(True)
            self.spinBox_3.setEnabled(True)
            self.spinBox_4.setEnabled(True)
            


            self.checkBox.setEnabled(True)
            self.checkBox_2.setEnabled(True)
            self.checkBox_4.setEnabled(True)
            self.checkBox_5.setEnabled(True)
            self.checkBox_6.setEnabled(True)
            self.radioButton.setEnabled(True)
            self.radioButton_2.setEnabled(True)
            self.radioButton_3.setEnabled(True)
            self.radioButton_4.setEnabled(True)
            self.radioButton_7.setEnabled(True)
            self.radioButton_8.setEnabled(True)
    
    def affi(self):
        self.affiche(self.image)

        time.sleep(1)
        state=False
        while not(state):
            ret,self.image = self.cap.read()
            if ret==False:
                self.timercam.stop()
                self.cap.release()
                cv2.destroyAllWindows()
                state=True
            else:
                self.affiche(self.image) 
                time.sleep(0.3)           
        

    def setConfigurationInterface(self,Name_Val,Val):
    
        if Val==True:
            module_xml.set_Val(Name_Val,1)
        else:
            module_xml.set_Val(Name_Val,0)
        
        if (Name_Val=="type"):
            self.getConfigurationInterface()





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    V = app.desktop().screenGeometry()
    h = V.height()-10
    w = V.width()-10

    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow,w,h)
    MainWindow.show()
    sys.exit(app.exec_())


