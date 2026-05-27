# Análisis del código de G1 – Sergio Rodríguez García

## Qué he visto hoy
He clonado el repositorio y revisado el código entregado por el Grupo 1.
El backend está desarrollado por Miguel Ángel Fernández en Python con Flask.

## Estructura del proyecto
- app.py: API REST con endpoints para clases, socios y reservas
- gFitBBDDPrueba.db: base de datos SQLite con los datos de prueba
- README.md: documentación del proyecto

## Endpoints disponibles
- GET/POST /clases
- GET/POST /socios
- GET/POST /reservas
- DELETE /reservas/<id>

## Qué voy a ampliar yo
Voy a desplegar esta aplicación en Render.com para que sea accesible 
desde una URL pública. Para ello necesito:
1. requirements.txt con las dependencias (ya creado)
2. Procfile para que Render sepa cómo arrancar la app (ya creado)
3. Conectar el repositorio con Render.com
4. Configurar variables de entorno
5. Verificar que la URL pública funciona correctamente