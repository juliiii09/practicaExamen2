Fitness Membership Console

1. Contexto general

El centro deportivo VitalGym necesita una herramienta en consola desarrollada en Python que permita administrar:

    Miembros
    Entrenamientos
    Asistencias
    Pagos de membresías
    Reportes mensuales

Toda la persistencia debe manejarse con archivos CSV.

2. Inicio de sesión

Al iniciar, la aplicación solicita usuario y contraseña.
Archivo: usuarios.csv

Campos:

    usuario
    contrasena
    rol

Reglas:

    Validar contra el CSV.
    No se permite registrar nuevos usuarios.

3. Persistencia CSV
3.1 Miembros — miembros.csv

Campos:

    miembro_id
    nombre
    documento
    telefono
    correo
    plan (BÁSICO | PREMIUM | FULL)
    fecha_inicio
    fecha_fin_plan
    estado (ACTIVO | INACTIVO)

3.2 Asistencias — asistencias.csv

Campos:

    asistencia_id
    miembro_id
    nombre
    fecha
    hora
    tipo (ENTRADA | SALIDA)

3.3 Pagos — pagos.csv

Campos:

    pago_id
    miembro_id
    nombre
    monto
    fecha_pago
    mes_pagado
    año
    metodo (EFECTIVO | TARJETA | TRANSFERENCIA)

3.4 Entrenamientos — entrenamientos.csv

Campos:

    entrenamiento_id
    miembro_id
    fecha
    duracion_min
    tipo (CARDIO | FUERZA | HIIT | ESTIRAMIENTO)
    calorias_estimadas

4. Reglas de negocio
4.1 Estado de membresía

    Solo miembros ACTIVOS pueden entrenar o registrar asistencia.
    Al vencer fecha_fin_plan → estado = INACTIVO.

4.2 Planes y pagos

    Un pago renueva el plan por 30 días.
    No se permiten pagos duplicados del mismo mes y año.

4.3 Cálculo de calorías estimadas

    CARDIO: duracion * 8
    FUERZA: duracion * 5
    HIIT: duracion * 12
    ESTIRAMIENTO: duracion * 3

5. Requerimientos funcionales
5.1 Gestión de miembros

    Registrar miembro
    Listar miembros (con estado)
    Buscar miembro
    Renovar plan con pago

5.2 Asistencias

    Registrar entrada/salida
    Historial por miembro

5.3 Entrenamientos

    Registrar entrenamiento
    Calcular calorías

5.4 Reportes CSV

Incluye:

    miembro_id
    nombre
    total_asistencias
    minutos_entrenados
    calorias_totales
    tipo entrenamiento

6. Requerimientos técnicos

Separar en módulos:

    main.py
    usuarios.py
    miembros.py
    asistencias.py
    entrenamientos.py
    pagos.py
    reportes.py

7. README.md requerido

Debe incluir:

    Descripción general
    Instrucciones de ejecución
    CSV necesarios
    Reglas de cálculo
    Mejoras futuras

8. Diagrama
Diagrama sugerido: flujo de login → menú → registrar actividad.
