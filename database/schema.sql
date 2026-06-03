-- Estructura de datos para GfitApp 
DROP TABLE IF EXISTS usuarios;
DROP TABLE IF EXISTS clases;

CREATE TABLE usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    apellidos TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,  -- Aquí irá el hash de seguridad
    rol TEXT NOT NULL DEFAULT 'socio' -- 'socio' o 'admin'
);

CREATE TABLE clases (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre_clase TEXT NOT NULL,
    instructor TEXT NOT NULL,
    capacidad_max INTEGER DEFAULT 20 -- Para el control de aforo 
);

CREATE TABLE IF NOT EXISTS membresias (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario_id INTEGER,
    tipo TEXT,
    estado TEXT,
    fecha_inicio TEXT,
    fecha_fin TEXT,
    precio DECIMAL,
    FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
);

CREATE TABLE historial (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario_id INTEGER NOT NULL,
    accion TEXT NOT NULL,
    fecha TEXT NOT NULL,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);

CREATE TABLE notificaciones (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario_id INTEGER NOT NULL,
    mensaje TEXT NOT NULL,
    leida INTEGER DEFAULT 0,
    fecha TEXT NOT NULL,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);