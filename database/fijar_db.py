import sqlite3
import os

# Ruta absoluta para no fallar
DB_PATH = os.path.join(os.path.dirname(__file__), 'database', 'gfit.db')

def fijar()
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Creamos la tabla de reservas que falta
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reservas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            socio_id INTEGER,
            clase TEXT,
            fecha TEXT,
            hora TEXT,
            FOREIGN KEY(socio_id) REFERENCES socios(id)
        )
    ''')
    
    # Por si acaso, nos aseguramos de que socios existe
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS socios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT, email TEXT UNIQUE, password TEXT, dni TEXT UNIQUE, plan TEXT
        )
    ''')

    conn.commit()
    conn.close()
    print(Tablas 'reservas' y 'socios' creadas con éxito.)

if __name__ == __main__
    fijar()