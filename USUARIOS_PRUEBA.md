# Usuarios de prueba

Credenciales locales para desarrollo. Todos los usuarios están activos.

| Username | Contraseña | Permisos | Registros de peso |
| --- | --- | --- | --- |
| prueba_ana | Prueba123 | Usuario normal | 30 |
| prueba_luis | Prueba123 | Usuario normal | 30 |
| prueba_sofia | Prueba123 | Usuario normal | 30 |
| prueba_admin | Prueba123 | Administrador y superusuario | 0 |

Se crearon 90 registros ficticios en total: uno diario por usuario normal,
del 14 de octubre al 12 de noviembre de 2026, con pesos en kg y variaciones pequeñas.
Cada registro está asociado a su usuario mediante `Registro.usuario`.
El campo `created_at` corresponde al momento de la inserción.

El usuario administrador puede ingresar a `/admin/`.
Los usuarios y registros que ya existían se conservaron.
