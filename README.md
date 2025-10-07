# Plataforma Gestión de Productos

Este proyecto corresponde al ejercicio individual del módulo Django, cuyo objetivo fue desarrollar una plataforma de gestión de productos con un sistema administrativo que permita manejar roles, permisos y restricciones de acceso.

Se implementaron distintos tipos de usuarios, grupos con permisos específicos y un manejador de errores 403 personalizado para usuarios sin autorización.

## Tecnologías utilizadas:

- **Django 5.2
- **Python 3.12
- **HTML + Bootstrap 5

![Página de inicio del proyecto](img.home.jpg)

## Estructura del Proyecto

El proyecto está organizado en una aplicación principal llamada producto, dentro del proyecto gestor.
```bash
gestor/
├── gestor/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── producto/
│   ├── models.py
│   ├── views.py
│   ├── admin.py
│   └── templates/
│       └── producto/
│           ├── home.html
│           ├── listado.html
│           ├── base.html
│           └── 403.html
└── manage.py
```

## Usuarios Creados

A continuación se listan los usuarios utilizados para probar los distintos niveles de permisos.
NOTA: Las contraseñas se incluyen solo con fines demostrativos para la revisión del ejercicio.

Usuario	Contraseña	Rol / Grupo	Permisos	Observación
- **admin_local	administrador123	Administrador	Ver, agregar, editar, eliminar	No es superusuario
- **admin_local2	administrador123	Administrador	Ver, agregar, editar, eliminar	
- **gestor_AM1	gestorgrupo1	Gestor	Ver, agregar, editar	No puede eliminar
- **gestor_PM2	equipo2123	Gestor sin permisos	Ninguno	Genera error 403
- **trabajador1	equipo123	Solo lectura	Solo “view”	No puede modificar
- **trabajador2	equipo123	Solo lectura	Solo “view”	No puede modificar

![Página de usuarios](img.usuarios_admin.png)

## Grupos y Permisos

Se configuraron dos grupos principales en el panel administrativo:

Administradores:
- **Permisos: add_producto, change_producto, delete_producto, view_producto.
- **Acceso total a la gestión de productos.

Gestores de Productos:
- **Permisos: add_producto, change_producto, view_producto.
- **No pueden eliminar productos.

![grupos de usuarios](img.grupos_usuarios.png)

## Limitación de Acceso al Sitio Administrativo

El acceso al panel /admin/ fue configurado para restringirse solo a usuarios autenticados con la marca is_staff=True.
- **Los usuarios no autenticados son redirigidos al formulario de login.
- **Los usuarios sin is_staff reciben un mensaje de “No tienes permiso para acceder a esta página”.
- **Los usuarios staff sin permisos ven el mensaje “No cuenta con permiso para ver ni editar nada”.

## Página Principal (Home)

La página principal (home.html) actúa como punto de entrada para los usuarios autenticados, permitiéndoles decidir entre:
- **Ir al Panel Administrativo
- **Ver Productos (si tienen permiso view_producto)
- **Además, la barra de navegación muestra el nombre del usuario y las opciones para cerrar sesión o acceder al admin.

## Listado de Productos
- **La vista /productos/ permite listar los productos registrados.
- **Solo los usuarios con permiso view_producto pueden acceder.
- **Si un usuario sin permisos intenta ingresar, Django lanza un PermissionDenied, que activa la plantilla personalizada 403.html.

## Vista de Error 403 Personalizada

Para manejar accesos denegados, se configuró un manejador de error personalizado en urls.py:
```bash
handler403 = "producto.views.custom_403"
Y la vista:

def custom_403(request, exception=None):
    return render(request, "403.html", status=403)
```
![error](img.error_403.png)

Prueba:
Usuario gestor_PM2 (sin permisos) intenta acceder a /productos/ o /solo-superuser/ → muestra la vista 403 personalizada.

## Login y Logout

Al iniciar sesión (desde /admin/login/?next=/), el usuario es redirigido al home del proyecto.
Al cerrar sesión, se redirige automáticamente al home gracias a la configuración:
```bash
LOGIN_URL = '/admin/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
```

![natvar](img.natvar.png)

## Flujo General de Acceso
- **Situación	Resultado esperado
- **Usuario no autenticado accede a /admin/	Redirige al login
- **Usuario autenticado sin is_staff	Acceso denegado
- **Usuario is_staff sin permisos	Puede entrar al admin, pero sin acciones disponibles
- **Usuario con permisos	Puede gestionar productos
- **Usuario sin permisos intenta /productos/	Muestra 403.html personalizado

## Conclusión

Este proyecto demuestra la correcta implementación del sistema de autenticación, roles, permisos y control de acceso en Django.
Se configuraron distintos usuarios y grupos, se personalizó la respuesta de error 403 y se limitó el acceso al sitio administrativo, cumpliendo con todos los requerimientos del ejercicio.
