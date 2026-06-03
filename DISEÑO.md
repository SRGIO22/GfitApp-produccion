# GfitApp
# Diseño de sistema de Login (admin/socio)

**Autor:** Argail Ruiz Cámara

## Requisitos:

- Python
- Flask
- Flask-login
- DB y HTML del G1

## Diseño e implementación:

Utilizando Flask y su extensión Flask-login este sistema gestionará la autenticación de los usuarios y el control de acceso a distintas partes de la aplicación.

Cuando un usuario intente acceder a una ruta protegida el sistema comprobará si el usuario está autenticado, de no estarlo se le redirigirá a la página de inicio de sesión, dónde introducirán sus credenciales, que el sistema comparará con la información almacenada en la base de datos.

Si las credenciales son correctas se crea una sesión Flask-login el usuario vuelve a la ruta que quería acceder y queda autenticado para toda la navegación, si no, permanece en la pantalla de acceso.

Deberá ampliarse la base de datos para incluir los datos de inicio de sesión, ya sea en una tabla usuarios propia o ampliando la tabla de socios para incluir nombre de usuario, contraseña, hash y rol.

El rol (admin/socio) determinará los permisos de acceso del usuario a las zonas de administración de la aplicación.

Además también habré de implementar HTML para crear las páginas de registro e inicio de sesión y hacer que conecten entre sí y con la app principal como he descrito arriba.