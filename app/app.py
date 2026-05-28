from flask import Flask, render_template, request, session, redirect, url_for, flash, jsonify 
import sqlite3
import os
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'clave_maestra_gfit_2026'

# Configuración de sesión y base de datos
app.config['SESSION_COOKIE_NAME'] = 'gfit_session'
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join(BASE_DIR, '..', 'database', 'gfit.db')

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def index():
    usuario = None
    if 'user_id' in session:
        conn = get_db_connection()
        usuario = conn.execute('SELECT * FROM usuarios WHERE id = ?', (session['user_id'],)).fetchone()
        conn.close()
    return render_template('index.html', usuario=usuario)


@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre = request.form.get('nombre', '').strip()
        apellidos = request.form.get('apellidos', '').strip()
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '')

        # VALIDACIONES DE SEGURIDAD
        if len(nombre) < 3:
            return "Error: El nombre es demasiado corto", 400
        if "@" not in email:
            return "Error: Email inválido", 400
        if len(password) < 6:
            return "Error: La contraseña debe tener al menos 6 caracteres", 400

        try:
            conn = get_db_connection()
            # Encriptamos la contraseña antes de guardarla en la BD
            password_encriptada = generate_password_hash(password)
            conn.execute('INSERT INTO usuarios (nombre, apellidos, email, password, rol) VALUES (?, ?, ?, ?, ?)',
                         (nombre, apellidos, email, password_encriptada, 'socio'))
            conn.commit()
            conn.close()
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            return "Error: El Email ya está registrado", 400
            
    return render_template('registro.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        conn = get_db_connection()
        try:
            # Buscamos solo por email ya que la clave está encriptada y no se puede comparar en el WHERE
            user = conn.execute('SELECT * FROM usuarios WHERE email = ?', (email,)).fetchone()
            
            # check_password_hash descifra y compara de forma segura
            if user and check_password_hash(user['password'], password):
                print("\n=== ¡USUARIO ENCONTRADO EN LA BD! ===")
                print(f"ID: {user['id']} | Nombre: {user['nombre']} | Rol: {user['rol']}\n")

                session.clear()
                session['user_id'] = user['id']
                session['user_name'] = user['nombre']
                session['rol'] = user['rol']
                
                if session['rol'] == 'admin':
                    return redirect(url_for('panel_admin'))
                else:
                    return redirect(url_for('index'))
            else:
                print(f"\n[LOGIN FALLIDO] Credenciales incorrectas para: {email}\n")
                return "Email o contraseña incorrectos", 401
        except sqlite3.OperationalError as e:
            return f"Error en la estructura de la base de datos: {str(e)}", 500
        finally:
            conn.close()
    return render_template('login.html')


@app.route('/admin')
def panel_admin():
    if 'user_id' not in session or session.get('rol') != 'admin':
        return "Acceso denegado: No tienes permisos de administrador", 403
        
    conn = get_db_connection()
    todas_reservas = conn.execute('''
        SELECT r.id, u.nombre, u.apellidos, r.clase, r.fecha, r.hora 
        FROM reservas r 
        JOIN usuarios u ON r.socio_id = u.id
    ''').fetchall()
    conn.close()
    
    return render_template('admin.html', reservas=todas_reservas)

@app.route('/admin/borrar_reserva/<int:reserva_id>', methods=['POST'])
def admin_borrar_reserva(reserva_id):
    if 'user_id' not in session or session.get('rol') != 'admin':
        return "Acceso denegado", 403
    
    conn = get_db_connection()
    try:
        conn.execute('DELETE FROM reservas WHERE id = ?', (reserva_id,))
        conn.commit()
    finally:
        conn.close()
        
    return redirect(url_for('panel_admin'))

@app.route('/reservas')
def reservas():
    if 'user_id' not in session: return redirect(url_for('login'))
    
    hoy = datetime.now().strftime('%Y-%m-%d')
    conn = get_db_connection()
    
    turnos = ['08:00 - 09:30', '10:00 - 11:30', '18:00 - 19:30']
    conteos = {}
    for t in turnos:
        c = conn.execute('SELECT COUNT(*) FROM reservas WHERE fecha = ? AND hora = ?', (hoy, t)).fetchone()[0]
        conteos[t] = c
    conn.close()
    return render_template('reservas.html', conteos=conteos)

@app.route('/confirmar_reserva_real', methods=['POST'])
def confirmar_reserva_real():
    if 'user_id' not in session: return jsonify({"status": "error"}), 401
    
    data = request.get_json()
    fecha_reserva = datetime.strptime(data['fecha'], '%Y-%m-%d').date()
    fecha_actual = datetime.now().date()

    if fecha_reserva < fecha_actual:
        return jsonify({"status": "error", "message": "No puedes viajar al pasado"}), 400

    conn = get_db_connection()
    try:
        existe = conn.execute('SELECT id FROM reservas WHERE socio_id = ? AND fecha = ? AND hora = ?',
                             (session['user_id'], data['fecha'], data['hora'])).fetchone()
        if existe:
            return jsonify({"status": "error", "message": "Ya estás apuntado"}), 400

        conn.execute('INSERT INTO reservas (socio_id, clase, fecha, hora) VALUES (?, ?, ?, ?)',
                     (session['user_id'], data['clase'], data['fecha'], data['hora']))
        conn.commit()
        return jsonify({"status": "success"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
    finally:
        conn.close()   

@app.route('/perfil')
def perfil():
    if 'user_id' not in session: 
        return redirect(url_for('login'))
    
    conn = get_db_connection()
    usuario = conn.execute('SELECT * FROM usuarios WHERE id = ?', (session['user_id'],)).fetchone()
    res = conn.execute('SELECT * FROM reservas WHERE socio_id = ?', (session['user_id'],)).fetchall()
    conn.close()
    return render_template('perfil.html', socio=usuario, reservas=res)

@app.route('/borrar_reserva/<int:reserva_id>', methods=['POST'])
def borrar_reserva(reserva_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    conn = get_db_connection()
    try:
        conn.execute('DELETE FROM reservas WHERE id = ? AND socio_id = ?', 
                     (reserva_id, session['user_id']))
        conn.commit()
    finally:
        conn.close()
        
    return redirect(url_for('perfil'))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

@app.route('/api/estadisticas/ocupacion')
def api_estadisticas_ocupacion():
    if 'user_id' not in session or session.get('rol') != 'admin':
        return jsonify({"error": "No autorizado"}), 403
        
    conn = get_db_connection()
    # Contamos cuántas reservas tiene cada clase para la gráfica
    datos = conn.execute('''
        SELECT clase, COUNT(*) as total 
        FROM reservas 
        GROUP BY clase
    ''').fetchall()
    conn.close()
    
    resultado = {row['clase']: row['total'] for row in datos}
    for clase in []:
        if clase not in resultado:
            resultado[clase] = 0
            
    return jsonify(resultado)

@app.route('/api/membresias/<int:usuario_id>')
def api_membresia_usuario(usuario_id):
    if 'user_id' not in session:
        return jsonify({"error": "No autorizado"}), 401
        
    conn = get_db_connection()
    membresia = conn.execute('SELECT * FROM membresias WHERE usuario_id = ?', (usuario_id,)).fetchone()
    conn.close()
    
    if membresia:
        return jsonify({
            "tipo": membresia['tipo'],
            "estado": membresia['estado'],
            "fecha_fin": membresia['fecha_fin']
        })
    return jsonify({"status": "sin_membresia"})

@app.route('/reservar/seleccion')
def nueva_reserva_seleccion():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('reservar_seleccion.html')

@app.route('/reservar/formulario/<actividad>')
def nueva_reserva_formulario(actividad):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('reservar_formulario.html', actividad_seleccionada=actividad)

@app.route('/clases')
def clases():

    conn = get_db_connection()

    try:
        clases = conn.execute('''
            SELECT *
            FROM clases
        ''').fetchall()

        resultado = []

        for clase in clases:
            resultado.append({
                "id": clase["id"],
                "nombre_clase": clase["nombre_clase"],
                "instructor": clase["instructor"],
                "capacidad_max": clase["capacidad_max"]
            })

        return jsonify(resultado)

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

    finally:
        conn.close()


@app.route('/socios')
def socios():

    conn = get_db_connection()

    try:
        socios = conn.execute('''
            SELECT id, nombre, apellidos, email, rol
            FROM usuarios
        ''').fetchall()

        resultado = []

        for socio in socios:
            resultado.append({
                "id": socio["id"],
                "nombre": socio["nombre"],
                "apellidos": socio["apellidos"],
                "email": socio["email"],
                "rol": socio["rol"]
            })

        return jsonify(resultado)

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

    finally:
        conn.close()
    
if __name__ == '__main__':
    app.run(debug=True)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)