import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="zoo"
)

class animal:
    def __init__(self, nom, race, id_cage, date_de_naissance,pays_origine, id = None):
        self.nom = nom
        self.race = race
        self.id_cage = id_cage
        self.date_de_naissance = date_de_naissance
        self.pays_origine = pays_origine
        self.id = id

    def afficher(self):
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM animal INNER JOIN cage ON animal.id_cage = cage.id WHERE nom = %s", (self.nom,))
        animal = cursor.fetchall()
        cursor.close()
        print (f"Voici  l'animal demandé : {animal}")

    def afficher_tous(self):
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM animal INNER JOIN cage ON animal.id_cage = cage.id")
        animal = cursor.fetchall()
        cursor.close()
        print (f"Voilà tous les animaux du zoo : {animal}")

    def ajouter(self):
        cursor = mydb.cursor()
        cursor.execute("INSERT INTO animal (nom,race,id_cage,date_de_naissance,pays_origine,id) VALUES (%s, %s, %s, %s, %s, %s)", (self.nom, self.race, self.id_cage, self.date_de_naissance, self.pays_origine, self.id))
        mydb.commit()
        cursor.close()
    
    def supprimer(self):
        cursor = mydb.cursor()
        cursor.execute("DELETE FROM animal WHERE nom = %s", (self.nom,))
        mydb.commit()
        cursor.close()
    
    def modifier(self):
        cursor = mydb.cursor()
        cursor.execute("UPDATE animal SET nom = %s, race = %s, id_cage = %s, date_de_naissance = %s, pays_origine = %s, id = %s ", (self.nom, self.race, self.id_cage, self.date_de_naissance, self.pays_origine, self.id))

class cage:
    def __init__(self, superficie, capacite, id = None):
        self.superficie = superficie
        self.capacite = capacite
        self.id = id

    def afficher(self):
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM cage INNER JOIN animal ON cage.id = animal.id_cage WHERE cage.id = %s", (self.id,))
        cage = cursor.fetchall()
        cursor.close()
        print (f"Voici la cage et les animaux qu'elle renferme : {cage}")

    def ajouter(self):
        cursor = mydb.cursor()
        cursor.execute("INSERT INTO cage (superficie, capacite, id) VALUES (%s, %s, %s)", (self.superficie, self.capacite, self.id))
        mydb.commit()
        cursor.close()

    def supprimer(self):
        cursor = mydb.cursor()
        cursor.execute("DELETE FROM cage WHERE id = %s", (self.id,))
        mydb.commit()
        cursor.close()

    def modifier(self):
        cursor = mydb.cursor()
        cursor.execute("UPDATE cage SET superficie = %s, capacite = %s WHERE id = %s", (self.superficie, self.capacite, self.id))
        mydb.commit()
        cursor.close()


def calculer_superficie_totale():
    cursor = mydb.cursor()
    cursor.execute("SELECT SUM(superficie) FROM cage")
    superficie_totale = cursor.fetchone()[0]
    cursor.close()
    print (f"La superficie totale du zoo est de {superficie_totale} m2")
    
    

cage1 = cage(40, 4, 1)
animal1 = animal("Youcef", "Pangolin", 1 , "2020-01-01", "France", 1)

animal1.ajouter()
cage1.ajouter()

animal1.afficher()
cage1.afficher()

animal1.race = "Chameau"
animal1.modifier()

cage2 = cage(50, 5, 2)
cage2.ajouter()

animal2 = animal("Pierre", "Chameau", 2 , "2020-01-01", "France", 2)
animal2.ajouter()
cage2.afficher()

animal1.afficher_tous()
calculer_superficie_totale()

animal1.supprimer()
animal2.supprimer()
cage1.supprimer()
cage2.supprimer()
