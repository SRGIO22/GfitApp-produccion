# \# GfitApp – API REST



\## ¿Qué es esto?

Backend de GfitApp, una aplicación de gestión de socios y clases de gimnasio.

Desarrollado por Miguel Ángel Fernández Sánchez (1º DAM – Colegio Santa Gema Galgani).



\## ¿Cómo ejecutar la API?



1\. Instalar Flask:

pip install flask



2\. Ejecutar la API:

python app.py



3\. Abrir el navegador en:

http://127.0.0.1:5000



\## Endpoints disponibles



\### Clases

\- GET http://127.0.0.1:5000/clases → devuelve todas las clases

\- POST http://127.0.0.1:5000/clases → crea una clase nueva



\### Socios

\- GET http://127.0.0.1:5000/socios → devuelve todos los socios

\- POST http://127.0.0.1:5000/socios → registra un socio nuevo



\### Reservas

\- GET http://127.0.0.1:5000/reservas → devuelve todas las reservas

\- POST http://127.0.0.1:5000/reservas → crea una reserva nueva



\## Tecnología usada

\- Python 3

\- Flask

