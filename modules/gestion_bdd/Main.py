import mysql.connector
from mysql.connector import Error
from datetime import datetime


def verifier_voiture(mat):
    try:
        connection = mysql.connector.connect(host='localhost',database='project_fin_etude',user='root',password='')
        cursor = connection.cursor()
        sql_update_query = """SELECT * FROM voiture_client  where (matricule_client=%s) """
        input = (mat,)
        cursor.execute(sql_update_query,input)
        records = cursor.fetchall()
        if cursor.rowcount==1:
            return True

        else:
            return False

        if (connection.is_connected()):
            connection.close()
       
    except mysql.connector.Error as error:
        return False
        
            




def ajouter_voiture(mat,nom,prenom,teleph):    
    try:
        connection = mysql.connector.connect(host='localhost',database='project_fin_etude',user='root',password='')
        cursor = connection.cursor()
        sql_update_query = """INSERT INTO voiture_client (matricule_client,nom_client,prenom_client,telephone_client) VALUES(%s,%s,%s,%s)"""
        input = (mat,nom,prenom,teleph)
        cursor.execute(sql_update_query, input)
        connection.commit()
        
        if (connection.is_connected()):
            connection.close()
        return 1

    except mysql.connector.Error as error:
        return 3

        
            


def suprimer_voiture(mat):   
    try:
        connection = mysql.connector.connect(host='localhost',database='project_fin_etude',user='root',password='')
        if verifier_voiture(mat):
        
            cursor = connection.cursor()
            sql_update_query = """Delete from voiture_client where(matricule_client	= %s)"""
            input = (mat,)
            cursor.execute(sql_update_query, input)
            connection.commit()
            return 1
        else:
            return 2
        
        if (connection.is_connected()):
            connection.close()
        
    except mysql.connector.Error as error:
       
        return 3

def ajouter_voiture_entrer(mat):  
    try:
        if verifier_voiture(mat):
            connection = mysql.connector.connect(host='localhost',database='project_fin_etude',user='root',password='')
            cursor = connection.cursor()
            sql_update_query = """INSERT INTO voiture_entrer (matricule_entrer, date_entre, heure_entrer) VALUES(%s,%s,%s)"""
            current_Date = datetime.now()
            date_now = current_Date.strftime('%Y-%m-%d')
            time_now = current_Date.strftime('%H:%M:%S')
            input = (mat,date_now,time_now)
            cursor.execute(sql_update_query, input)
            connection.commit()
            return 1
      
        else:
            return 2
      
        if (connection.is_connected()):
            connection.close()
      
      
    except mysql.connector.Error as error:
        return 3



