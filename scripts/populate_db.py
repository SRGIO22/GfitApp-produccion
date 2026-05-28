import sqlite3
import os
from werkzeug.security import generate_password_hash

def populate():
    # Encontramos la raíz del proyecto 
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    # Rutas exactas apuntando a la carpeta /database
    db_path = os.path.join(base_dir, 'database', 'gfit.db')
    schema_path = os.path.join(base_dir, 'database', 'schema.sql')
    
    print(f"Buscando base de datos en: {db_path}")
    print(f"Buscando esquema en: {schema_path}")
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # 1. Leer y ejecutar el schema.sql desde /database
    if os.path.exists(schema_path):
        with open(schema_path, 'r', encoding='utf-8') as f:
            sql_script = f.read()
        cursor.executescript(sql_script)
        print("¡Tablas creadas desde schema.sql correctamente!")
    else:
        print(f"ERROR: No se encontró el archivo schema.sql en {schema_path}")
        conn.close()
        return

    # 2. Insertar los datos de prueba (Socio y Admin con contraseñas ENCRIPTADAS)
    usuarios_prueba = [
        ('Samuel', 'Moreno Lázaro', 'samuel_mlazaro@alumnos-santagema.es', generate_password_hash('socio123'), 'socio'),
        ('Admin', 'GfitApp', 'admin@gymfever.es', generate_password_hash('admin123'), 'admin')
    ]
    
    cursor.executemany("""
        INSERT INTO usuarios (nombre, apellidos, email, password, rol) 
        VALUES (?, ?, ?, ?, ?)
    """, usuarios_prueba)
    
    # 3. Insertar las clases
    clases_prueba = [
        ('Spinning', 'Carlos Gómez', 20),
        ('Crossfit', 'Laura Martínez', 20),
        ('Yoga', 'Elena Ruiz', 20)
    ]

    membresias_prueba = [
    (1, 'Mensual', 'Activa', '2026-05-01', '2026-06-01'),
    (2, 'Anual', 'Activa', '2026-01-01', '2027-01-01')
]

cursor.executemany("""
    INSERT INTO membresias (usuario_id, tipo, estado, fecha_inicio, fecha_fin) 
    VALUES (?, ?, ?, ?, ?)
""", membresias_prueba)
    
    cursor.executemany("""
        INSERT INTO clases (nombre_clase, instructor, capacidad_max) 
        VALUES (?, ?, ?)
    """, clases_prueba)
    
    conn.commit()
    conn.close()
    print("¡Base de datos gfit.db totalmente poblada con Éxito!")

if __name__ == '__main__':
    populate()