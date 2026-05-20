from flask import Flask, jsonify, request

app = Flask(__name__)

# --- DATOS DE PRUEBA ---
clases = [
    {"id": 1, "nombre": "Yoga", "hora": "10:00", "plazas": 10},
    {"id": 2, "nombre": "Spinning", "hora": "11:00", "plazas": 15},
    {"id": 3, "nombre": "Pilates", "hora": "12:00", "plazas": 8}
]

socios = [
    {"id": 1, "nombre": "Juan García", "email": "juan@email.com"},
    {"id": 2, "nombre": "Ana López", "email": "ana@email.com"}
]

reservas = [
    {"id": 1, "socio_id": 1, "clase_id": 2},
    {"id": 2, "socio_id": 2, "clase_id": 1}
]

# --- ENDPOINTS DE CLASES ---
@app.route('/clases', methods=['GET'])
def get_clases():
    return jsonify(clases)

@app.route('/clases', methods=['POST'])
def crear_clase():
    nueva_clase = request.json
    nueva_clase['id'] = len(clases) + 1
    clases.append(nueva_clase)
    return jsonify(nueva_clase), 201

# --- ENDPOINTS DE SOCIOS ---
@app.route('/socios', methods=['GET'])
def get_socios():
    return jsonify(socios)

@app.route('/socios', methods=['POST'])
def crear_socio():
    nuevo_socio = request.json
    nuevo_socio['id'] = len(socios) + 1
    socios.append(nuevo_socio)
    return jsonify(nuevo_socio), 201

# --- ENDPOINTS DE RESERVAS ---
@app.route('/reservas', methods=['GET'])
def get_reservas():
    return jsonify(reservas)

@app.route('/reservas', methods=['POST'])
def crear_reserva():
    nueva_reserva = request.json
    nueva_reserva['id'] = len(reservas) + 1
    reservas.append(nueva_reserva)
    return jsonify(nueva_reserva), 201

# --- BUSCAR SOCIO POR ID ---
@app.route('/socios/<int:id>', methods=['GET'])
def get_socio(id):
    socio = next((s for s in socios if s['id'] == id), None)
    if socio:
        return jsonify(socio)
    return jsonify({"error": "Socio no encontrado"}), 404

# --- CANCELAR RESERVA ---
@app.route('/reservas/<int:id>', methods=['DELETE'])
def cancelar_reserva(id):
    reserva = next((r for r in reservas if r['id'] == id), None)
    if reserva:
        reservas.remove(reserva)
        return jsonify({"mensaje": "Reserva cancelada correctamente"})
    return jsonify({"error": "Reserva no encontrada"}), 404

if __name__ == '__main__':
    app.run(debug=True)