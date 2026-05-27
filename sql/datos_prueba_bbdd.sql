-- =========================================
-- DATOS DE PRUEBA
-- =========================================

-- ENTRENADORES
INSERT INTO entrenadores (nombre_entrenador, apellidos_entrenador, email_entrenador, especialidad_entrenador)
VALUES
('Laura', 'Gómez Ruiz', 'laura.gomez@gfit.com', 'Yoga'),
('Carlos', 'Martín Pérez', 'carlos.martin@gfit.com', 'Crossfit'),
('Ana', 'Santos Díaz', 'ana.santos@gfit.com', 'Pilates');

-- SOCIOS
INSERT INTO socios (nombre_socio, apellidos_socio, email_socio, telefono_socio, fecha_alta_socio, activo)
VALUES
('Noa', 'Fernández López', 'noa@example.com', '611223344', '2024-01-10', 1),
('Mario', 'Sánchez Ruiz', 'mario@example.com', '622334455', '2024-02-15', 1),
('Lucía', 'Pérez Díaz', 'lucia@example.com', '633445566', '2024-03-20', 1);

-- CLASES
INSERT INTO clases (id_entrenador, nombre_clase, descripcion_clase, fecha_clase, hora_clase, duracion_clase, capacidad_max)
VALUES
(1, 'Yoga Suave', 'Clase de relajación', '2024-05-20', '10:00', 60, 20),
(2, 'Crossfit Intenso', 'Entrenamiento avanzado', '2024-05-21', '18:00', 45, 15),
(3, 'Pilates Core', 'Fortalecimiento del core', '2024-05-22', '12:00', 50, 18);

-- RESERVAS
INSERT INTO reservas (id_socio, id_clase, fecha_reserva, estado_reserva)
VALUES
(1, 1, '2024-05-10', 'Activa'),
(2, 2, '2024-05-11', 'Activa'),
(3, 3, '2024-05-12', 'Cancelada');

-- MEMBRESIAS
INSERT INTO membresias (id_socio, tipo_membresia, fecha_inicio, fecha_fin, precio_membresia, activa_membresia)
VALUES
(1, 'Mensual', '2024-05-01', '2024-05-31', 29.99, 1),
(2, 'Trimestral', '2024-04-01', '2024-06-30', 79.99, 1),
(3, 'Anual', '2024-01-01', '2024-12-31', 199.99, 1);

-- INCIDENCIAS
INSERT INTO incidencias (id_socio, descripcion_incidencia, fecha_incidencia, estado_incidencia)
VALUES
(1, 'Problema con la reserva', '2024-05-05', 'Cerrada'),
(2, 'Error en la membresía', '2024-05-06', 'En proceso'),
(3, 'Acceso denegado', '2024-05-07', 'Abierta');
