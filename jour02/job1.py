import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="patesaup0ulet",
    database="laplateforme"
)
cursor = mydb.cursor()
cursor.execute("SELECT * FROM etudiants")
etudiants = cursor.fetchall()
cursor.close()
print (etudiants)