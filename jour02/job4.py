import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="laplateforme"
)

cursor = mydb.cursor()
cursor.execute("SELECT nom, capacite FROM salle")
salle = cursor.fetchall()
cursor.close()
print (salle)