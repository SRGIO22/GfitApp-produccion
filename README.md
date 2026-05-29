# GfitApp – Repositorio de Producción
## DevOps / Despliegue – Sergio Rodríguez García
### 1º DAM · Colegio Santa Gema Galgani · Curso 2025-2026

## URL pública
🌐 https://gfitapp-produccion.onrender.com

## ¿Qué es este repositorio?
Repositorio de producción de GfitApp, una aplicación de gestión de socios 
y clases de gimnasio. Este repositorio está conectado a Render.com y 
cualquier cambio que se suba se despliega automáticamente.

## ¿Cómo está desplegado?
- La app corre en Render.com con un servidor Gunicorn
- La base de datos SQLite se inicializa automáticamente al arrancar
- Las variables de entorno están configuradas en Render (SECRET_KEY, FLASK_ENV)

## Archivos clave
- app.py: API REST en Flask con inicialización automática de BD
- requirements.txt: dependencias necesarias (Flask, Gunicorn)
- Procfile: indica a Render cómo arrancar la app
- sql/: scripts SQL para crear tablas y datos de prueba

## Endpoints disponibles
### Socios
- GET /socios → devuelve todos los socios
- GET /socios/<id> → devuelve un socio por id
- POST /socios → registra un socio nuevo

### Clases
- GET /clases → devuelve todas las clases
- POST /clases → crea una clase nueva

### Reservas
- GET /reservas → devuelve todas las reservas
- POST /reservas → crea una reserva nueva
- DELETE /reservas/<id> → cancela una reserva

## Tecnología usada
- Python 3 + Flask
- SQLite
- Gunicorn
- Render.com (plan gratuito)
- Git + GitHub

## Cómo actualizar producción
Cuando un compañero termine su módulo, se integra así:
1. git merge nombre-rama-compañero
2. git push produccion sergio-rodriguez:main
3. Render redespliega automáticamente