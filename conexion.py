import mysql.connector
class DB:
    def __init__(self):
        self.conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="escuela"
        )
        self.cursor = self.conexion.cursor()