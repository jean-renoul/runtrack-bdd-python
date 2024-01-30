import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="patesaup0ulet",
    database="laplateforme"
)

cursor = mydb.cursor()
cursor.execute("SELECT SUM(capacite) FROM salle")
capacite = cursor.fetchone()[0]
cursor.close()
print (f"La capacité de toutes les salles est de {capacite} m2")