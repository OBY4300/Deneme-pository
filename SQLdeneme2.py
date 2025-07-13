import sqlite3
from config import DATABASE

class DB_Manager:
    def __init__(self, database):      
        self.database = database

    def create_tables(self):
        conn = sqlite3.connect(self.database)
        with conn:
            # Projeler tablosu
            conn.execute("""
                CREATE TABLE IF NOT EXISTS projects (
                    project_id INTEGER PRIMARY KEY,
                    user_id INTEGER,
                    project_name TEXT NOT NULL,
                    description TEXT,
                    url TEXT,
                    status_id INTEGER,
                    FOREIGN KEY(status_id) REFERENCES status(status_id)
                )
            """)

			#Satır 20: status_id sütunundaki verileri bir FK yaptıktan sonra status tablosundaki diğer status_id değerine bağlıyoruz.

            # Beceriler tablosu
            conn.execute("""
                CREATE TABLE IF NOT EXISTS skills (
                    skill_id INTEGER PRIMARY KEY,
                    skill_name TEXT
                )
            """)

            # Proje-Beceri bağlantı tablosu
            conn.execute("""
                CREATE TABLE IF NOT EXISTS project_skills (
                    project_id INTEGER,
                    skill_id INTEGER,
                    FOREIGN KEY(skill_id) REFERENCES skills(skill_id)
                    FOREIGN KEY(project_id) REFERENCES projects(project_id)
                )
            """)
 
            # Proje durumu tablosu
            conn.execute("""
                CREATE TABLE IF NOT EXISTS status (
                    status_id INTEGER PRIMARY KEY,
                    status_name TEXT
                )
            """)

        print("Veritabanı tabloları başarıyla oluşturuldu!")
        

if __name__ == '__main__':
    manager = DB_Manager(DATABASE)
    manager.create_tables()