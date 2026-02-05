NUEVO PLANTEAMIENTO – PRUEBA DE DESEMPEÑO (NICHO: TECHLAB)

1. Contexto general
El Laboratorio de Innovación Tecnológica (TechLab) necesita una herramienta de consola para gestionar el inventario de equipos tecnológicos y los préstamos que realizan estudiantes, instructores o personal interno. Actualmente, el proceso manual genera errores en disponibilidad, tiempos de préstamo, retrasos y reportes.

La aplicación debe permitir:
- Iniciar sesión como administrador
- Gestionar equipos
- Registrar, aprobar o rechazar préstamos
- Registrar devoluciones y cálculos de retraso
- Exportar reportes por mes y año
- Mantener todo en CSV

2. Inicio de sesión
Debe existir un archivo usuarios.csv con un único usuario administrador:
- usuario
- contrasena
- rol (ADMIN)

Reglas:
- Máximo 3 intentos
- Validación obligatoria antes del menú principal

3. Persistencia en CSV
Archivos:
- usuarios.csv
- equipos.csv → equipo_id, nombre_equipo, categoria, estado_actual, fecha_registro
- prestamos.csv → prestamo_id, equipo_id, nombre_equipo, usuario_prestatario, tipo_usuario, fechas, días, retraso, estado, mes, anio

4. Reglas de préstamo
Tiempo máximo según tipo de usuario:
- Estudiante: 3 días
- Instructor: 7 días
- Administrativo: 10 días

Un equipo solo puede prestarse si está DISPONIBLE.  
Al devolver:
- Calcular días usados
- Determinar retraso

5. Requerimientos funcionales
- Registrar, listar y consultar equipos
- Solicitar préstamos (pendiente)
- Aprobar o rechazar
- Registrar devoluciones con cálculo de retraso
- Historial por usuario o equipo
- Exportar reporte CSV mensual/anual

6. Requerimientos técnicos
- Python
- Consola
- Múltiples archivos .py (main.py, usuarios.py, equipos.py, prestamos.py, reportes.py)
- Uso obligatorio de funciones, if/else, bucles

7. README.md
Debe incluir:
- Título, autor y descripción
- Instrucciones de ejecución
- CSV requeridos
- Reglas del sistema
- Estructura del proyecto
- Limitaciones y mejoras

8. Diagrama de flujo
Representar:
- Inicio de sesión + menú
O
- Flujo de préstamo (validaciones, aprobación/rechazo)

Formato: PNG/JPG/PDF

9. Entrega
ZIP llamado NOMBRE_APELLIDO.zip con:
- Archivos .py
- CSV
- README.md
- Diagrama de flujo

10. Restricciones
- Prohibido usar IA
- Prohibido Copilot o autocompletados
- Solo documentación oficial de Python