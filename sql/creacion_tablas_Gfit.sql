-- =========================================
-- CREACIÓN DE LA BASE DE DATOS GfitApp
-- SQLite
-- =========================================


-- =========================================
-- TABLA: ENTRENADORES
-- =========================================

CREATE TABLE entrenadores (

    id_entrenador INTEGER PRIMARY KEY AUTOINCREMENT,

    nombre_entrenador TEXT NOT NULL,

    apellidos_entrenador TEXT NOT NULL,

    email_entrenador TEXT NOT NULL UNIQUE,

    especialidad_entrenador TEXT NOT NULL

);

-- =========================================
-- TABLA: CLASES
-- =========================================

CREATE TABLE clases (

    id_clase INTEGER PRIMARY KEY AUTOINCREMENT,

    id_entrenador INTEGER NOT NULL,

    nombre_clase TEXT NOT NULL,

    descripcion_clase TEXT,

    fecha_clase DATE NOT NULL,

    hora_clase TEXT NOT NULL,

    duracion_clase INTEGER NOT NULL CHECK (duracion_clase > 0),

    capacidad_max INTEGER NOT NULL CHECK (capacidad_max > 0),

    FOREIGN KEY (id_entrenador) REFERENCES entrenadores(id_entrenador)

);

-- =========================================
-- TABLA: SOCIOS
-- =========================================

CREATE TABLE socios (

    id_socio INTEGER PRIMARY KEY AUTOINCREMENT,

    nombre_socio TEXT NOT NULL,

    apellidos_socio TEXT NOT NULL,

    email_socio TEXT NOT NULL UNIQUE,

    telefono_socio TEXT,

    fecha_alta_socio DATE NOT NULL,

    activo INTEGER NOT NULL CHECK (activo IN (0,1))

);

-- =========================================
-- TABLA: RESERVAS
-- =========================================

CREATE TABLE reservas (

    id_reserva INTEGER PRIMARY KEY AUTOINCREMENT,

    id_socio INTEGER NOT NULL,

    id_clase INTEGER NOT NULL,

    fecha_reserva DATE NOT NULL,

    estado_reserva TEXT NOT NULL CHECK (estado_reserva IN ('Activa','Cancelada','Asistida')),

    FOREIGN KEY (id_socio) REFERENCES socios(id_socio),

    FOREIGN KEY (id_clase) REFERENCES clases(id_clase),

    UNIQUE (id_socio, id_clase)

);


-- =========================================
-- TABLA: MEMBRESIAS
-- =========================================

CREATE TABLE membresias (

    id_membresia INTEGER PRIMARY KEY AUTOINCREMENT,

    id_socio INTEGER NOT NULL,

    tipo_membresia TEXT NOT NULL CHECK (tipo_membresia IN ('Mensual','Trimestral','Anual')),

    fecha_inicio DATE NOT NULL,

    fecha_fin DATE NOT NULL,

    precio_membresia REAL NOT NULL CHECK (precio_membresia >= 0),

    activa_membresia INTEGER NOT NULL CHECK (activa_membresia IN (0,1)),

    FOREIGN KEY (id_socio) REFERENCES socios(id_socio),

    CHECK (fecha_fin > fecha_inicio)

);

-- =========================================
-- TABLA: INCIDENCIAS
-- =========================================

CREATE TABLE incidencias (

    id_incidencia INTEGER PRIMARY KEY AUTOINCREMENT,

    id_socio INTEGER NOT NULL,

    descripcion_incidencia TEXT NOT NULL,

    fecha_incidencia DATE NOT NULL,

    estado_incidencia TEXT NOT NULL CHECK (estado_incidencia IN ('Abierta','En proceso','Cerrada')),

    FOREIGN KEY (id_socio) REFERENCES socios(id_socio)

);
