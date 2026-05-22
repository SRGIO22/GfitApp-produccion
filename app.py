from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

DATABASE = 'gFitBBDDPrueba.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# --- ENDPOINTS DE CLASES ---
@app.route('/clases', methods=['GET'])
def get_clases():
    conn = get_db()
    clases = conn.execute('SELECT * FROM clases').fetchall()
    conn.close()
    return jsonify([dict(c) for c in clases])

@app.route('/clases', methods=['POST'])
def crear_clase():
    data = request.json
    conn = get_db()
    conn.execute('''INSERT INTO clases 
        (id_entrenador, nombre_clase, descripcion_clase, fecha_clase, hora_clase, duracion_clase, capacidad_max)
        VALUES (?,?,?,?,?,?,?)''',
        (data['id_entrenador'], data['nombre_clase'], data['descripcion_clase'],
         data['fecha_clase'], data['hora_clase'], data['duracion_clase'], data['capacidad_max']))
    conn.commit()
    conn.close()
    return jsonify({"mensaje": "Clase creada correctamente"}), 201

# --- ENDPOINTS DE SOCIOS ---
@app.route('/socios', methods=['GET'])
def get_socios():
    conn = get_db()
    socios = conn.execute('SELECT * FROM socios').fetchall()
    conn.close()
    return jsonify([dict(s) for s in socios])

@app.route('/socios/<int:id>', methods=['GET'])
def get_socio(id):
    conn = get_db()
    socio = conn.execute('SELECT * FROM socios WHERE id_socio = ?', (id,)).fetchone()
    conn.close()
    if socio:
        return jsonify(dict(socio))
    return jsonify({"error": "Socio no encontrado"}), 404

@app.route('/socios', methods=['POST'])
def crear_socio():
    data = request.json
    conn = get_db()
    conn.execute('''INSERT INTO socios 
        (nombre_socio, apellidos_socio, email_socio, telefono_socio, fecha_alta_socio, activo)
        VALUES (?,?,?,?,?,?)''',
        (data['nombre_socio'], data['apellidos_socio'], data['email_socio'],
         data['telefono_socio'], data['fecha_alta_socio'], data['activo']))
    conn.commit()
    conn.close()
    return jsonify({"mensaje": "Socio creado correctamente"}), 201

# --- ENDPOINTS DE RESERVAS ---
@app.route('/reservas', methods=['GET'])
def get_reservas():
    conn = get_db()
    reservas = conn.execute('SELECT * FROM reservas').fetchall()
    conn.close()
    return jsonify([dict(r) for r in reservas])

@app.route('/reservas', methods=['POST'])
def crear_reserva():
    data = request.json
    conn = get_db()
    conn.execute('''INSERT INTO reservas 
        (id_socio, id_clase, fecha_reserva, estado_reserva)
        VALUES (?,?,?,?)''',
        (data['id_socio'], data['id_clase'], data['fecha_reserva'], data['estado_reserva']))
    conn.commit()
    conn.close()
    return jsonify({"mensaje": "Reserva creada correctamente"}), 201

@app.route('/reservas/<int:id>', methods=['DELETE'])
def cancelar_reserva(id):
    conn = get_db()
    reserva = conn.execute('SELECT * FROM reservas WHERE id_reserva = ?', (id,)).fetchone()
    if reserva:
        conn.execute('UPDATE reservas SET estado_reserva = ? WHERE id_reserva = ?', ('Cancelada', id))
        conn.commit()
        conn.close()
        return jsonify({"mensaje": "Reserva cancelada correctamente"})
    conn.close()
    return jsonify({"error": "Reserva no encontrada"}), 404

if __name__ == '__main__':
    app.run(debug=True)