# Módulo para funciones auxiliares: carga de datos y presentación.

import csv
import os

NOMBRE_ARCHIVO = "dataset_paises.csv"
FIELDNAMES = ['nombre', 'poblacion', 'superficie', 'continente']

def cargar_datos_desde_csv():
    datos = []
    
    if not os.path.exists(NOMBRE_ARCHIVO):
        print(f"ERROR CRÍTICO: No se encontró el archivo '{NOMBRE_ARCHIVO}'. Asegúrese de que esté en el mismo directorio.")
        return datos

    try:
        with open(NOMBRE_ARCHIVO, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file, fieldnames=FIELDNAMES)
            next(reader) 
            
            for row in reader:
                try:
                    pais = {
                        'nombre': row['nombre'].strip(),
                        'poblacion': int(row['poblacion']),
                        'superficie': int(row['superficie']),
                        'continente': row['continente'].strip()
                    }
                    if pais['poblacion'] > 0 and pais['superficie'] > 0:
                        datos.append(pais)
                    else:
                        print(f"ADVERTENCIA: Saltando país '{pais['nombre']}' por datos numéricos inválidos.")
                        
                except ValueError:
                    print(f"ERROR: Error de formato en un registro (población/superficie no es un número). Registro: {row.get('nombre', 'Desconocido')}. Saltando.")
                except KeyError as e:
                    print(f"ERROR: Falta el campo {e} en un registro del CSV. Verifique las columnas.")

    except IOError as e:
        print(f"ERROR: No se pudo abrir o leer el archivo CSV: {e}")
        
    print(f"\n[+] Lectura completa. Total de {len(datos)} países cargados.")
    return datos

def mostrar_lista_paises(lista_paises, titulo="Lista de Países"):

    print("\n" + "="*80)
    print(f"{titulo.center(80)}")
    print("="*80)
    
    if not lista_paises:
        print("No se encontraron resultados para mostrar.")
        print("="*80)
        return

    # Table de encabezados
    print(f"{'Nombre':<20} | {'Población (hab)':<20} | {'Superficie (km²)' :<20} | {'Continente':<15}")
    print("-" * 80)
    
    # Mostrar cada pais
    for pais in lista_paises:
        #Formatear números grandes para una mejor legibilidad
        poblacion_fmt = f"{pais['poblacion']:,}".replace(",", ".")
        superficie_fmt = f"{pais['superficie']:,}".replace(",", ".")
        
        print(
            f"{pais['nombre']:<20} | {poblacion_fmt:<20} | {superficie_fmt:<20} | {pais['continente']:<15}"
        )
    
    print("="*80)
