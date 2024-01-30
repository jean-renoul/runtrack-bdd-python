import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="patesaup0ulet",
    database="laplateforme"
)

cursor = mydb.cursor()
cursor.execute("SELECT  SUM(superficie) FROM etage")
superficie = cursor.fetchone()[0]
cursor.close()
print (f"La superficcie de la Plateforme est de {superficie} m2")