import sqlite3
import os

# Ruta base de datos
db_path = os.path.join('database', 'gfit.db')

def actualizar_db():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Borra tablas viejas para no tener conflictos de columnas
    cursor.execute('DROP TABLE IF EXISTS socios')
    cursor.execute('DROP TABLE IF EXISTS reservas')

    # Creamos la tabla de SOCIOS con los campos que pediste
    cursor.execute('''
        CREATE TABLE socios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            dni TEXT UNIQUE,
            plan TEXT DEFAULT 'Ninguno',
            es_admin INTEGER DEFAULT 0
        )
    ''')

    # Crea la tabla de RESERVAS
    cursor.execute('''
        CREATE TABLE reservas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            socio_id INTEGER,
            clase TEXT,
            fecha TEXT,
            hora TEXT,
            FOREIGN KEY(socio_id) REFERENCES socios(id)
        )
    ''')

    # Insertamos ADMIN (Pass: 0000)
    cursor.execute("""
        INSERT INTO socios (nombre, email, password, dni, plan, es_admin) 
        VALUES ('Admin GFit', 'admin@gfit.com', '0000', '00000000A', 'Premium', 1)
    """)

    conn.commit()
    conn.close()
    print("Base de datos actualizada con éxito.")

if __name__ == "__main__":
    actualizar_db()