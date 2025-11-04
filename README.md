🌎 TPI - Gestión de Datos de Países (Programación 1)

Este proyecto implementa un sistema en consola desarrollado en Python para gestionar, consultar y analizar datos geográficos y demográficos de una base de datos de países (almacenada en formato CSV).

El objetivo principal es afianzar el uso de estructuras de datos (Listas y Diccionarios), la modularización con funciones, y aplicar técnicas de filtrado, ordenamiento y cálculo de estadísticas, tal como se requiere en la materia Programación 1.

⚙️ Estructura del Proyecto (Modularización)

El código cumple con la consigna de modularización al dividir la lógica en archivos independientes, donde cada módulo tiene una única responsabilidad.

Archivo

Responsabilidad Principal

main.py

Orquestador: Muestra el menú principal, maneja el flujo del programa y llama a las funciones de otros módulos.

dataset_paises.csv

Datos: Contiene el dataset de entrada en formato CSV.

Utilidades.py

I/O: Funciones para la carga inicial del CSV y la visualización tabular de resultados.

Validaciones.py

Validación: Funciones para el control de errores en la entrada de datos (ej: asegurar que un input sea numérico).

busquedas_filtros.py

Consultas: Implementa la búsqueda por nombre y los filtros por Continente, Rango de Población y Rango de Superficie.

ordenamiento.py

Ordenamiento: Implementa la lógica para ordenar la lista de países por Nombre, Población o Superficie.

estadisticas.py

Cálculos: Funciones para el cálculo de indicadores clave (promedios, máximo/mínimo, conteo por continente).

🚀 Instrucciones de Uso

1. Requisitos

Tener instalado Python 3.x.

Asegurar que todos los archivos .py y el .csv estén en el mismo directorio.

2. Ejecución

Abre tu terminal (CMD, PowerShell o Git Bash).

Navega hasta la carpeta del proyecto.

Ejecuta el programa principal:

python main.py


3. Ejemplos de Entradas y Salidas

El programa inicializa mostrando los datos cargados y presenta un menú:

Ejemplo de Ordenamiento (Opción 4)

Entradas:

Seleccione una opción: 4

Seleccione el campo para ordenar (a/b/c): b (Población)

Seleccione el orden (A: Ascendente, D: Descendente): D (Descendente)

Salida (Recorte):

================================================================================
           Lista ordenada por Población (Descendente)           
================================================================================
Nombre               | Población (hab)      | Superficie (km²)     | Continente     
--------------------------------------------------------------------------------
China                | 1.444.216.107        | 9.596.961            | Asia           
India                | 1.434.190.000        | 3.287.263            | Asia           
Estados Unidos       | 341.000.000          | 9.833.520            | America        
...


Ejemplo de Estadísticas (Opción 5)

Salida (Recorte):

==================================================
                 INDICADORES ESTADÍSTICOS                 
==================================================
🥇 País con Mayor Población: China (1.444.216.107 hab)
🥉 País con Menor Población: Nueva Zelanda (5.132.530 hab)
--------------------------------------------------
📊 Promedio de Población: 147.165.811 habitantes
📐 Promedio de Superficie: 3.321.432 km²
--------------------------------------------------
🌍 Conteo de Países por Continente:
  - America: 8 países
  - Asia: 6 países
  - Europa: 5 países
  - Africa: 3 países
  - Oceania: 2 países
==================================================



Integrantes: Joseph Oliveros