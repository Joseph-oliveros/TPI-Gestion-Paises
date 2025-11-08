import csv
import os

NOMBRE_ARCHIVO = "dataset_paises.csv"

FIELDNAMES = ['nombre', 'poblacion', 'superficie', 'continente']

def guardar_datos_csv(lista_paises, nombre_archivo=NOMBRE_ARCHIVO):
    """Guarda la lista de diccionarios de países de vuelta al archivo CSV."""
    if not lista_paises:
        print("ADVERTENCIA: La lista de países está vacía, se creará un CSV vacío.")
    
    # Usamos FIELDNAMES como guía para asegurar el orden de las columnas al guardar
    campos = FIELDNAMES

    try:
        # 'w' sobrescribe el archivo
        with open(nombre_archivo, 'w', newline='', encoding='utf-8') as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()  # Escribe la primera fila (encabezados)
            escritor.writerows(lista_paises)
        print(f"\nDatos guardados exitosamente en '{nombre_archivo}'.")
    except Exception as e:
        print(f"\nERROR al guardar los datos en el CSV: {e}")

def cargar_datos_desde_csv():
    # Carga los datos del archivo CSV en una lista de diccionarios.
    datos = []
    
    if not os.path.exists(NOMBRE_ARCHIVO):
        print(f"\nERROR CRÍTICO: No se encontró el archivo '{NOMBRE_ARCHIVO}'. Asegúrese de que esté en el mismo directorio.")
        return datos

    try:
        with open(NOMBRE_ARCHIVO, mode='r', newline='', encoding='utf-8') as file:
            # Usamos DictReader con FIELDNAMES para asegurar la correcta lectura de tus columnas
            reader = csv.DictReader(file, fieldnames=FIELDNAMES)
            next(reader) # Saltar la primera fila de encabezados si se está leyendo un archivo ya creado
            
            for row in reader:
                try:
                    pais = {
                        'nombre': row['nombre'].strip(),
                        # Convertir a INT
                        'poblacion': int(row['poblacion']),
                        'superficie': int(row['superficie']),
                        'continente': row['continente'].strip()
                    }
                    # Validar datos al cargar (como lo tenías antes)
                    if pais['poblacion'] >= 0 and pais['superficie'] >= 0:
                        # Solo agregamos si los números son válidos (positivos o cero)
                        datos.append(pais)
                    else:
                        print(f"ADVERTENCIA: Saltando país '{pais['nombre']}' por datos numéricos no válidos.")
                        
                except ValueError:
                    print(f"ERROR: Error de formato en un registro (población/superficie no es un número). Registro: {row.get('nombre', 'Desconocido')}. Saltando.")
                except KeyError as e:
                    print(f"ERROR: Falta el campo {e} en un registro del CSV. Verifique las columnas.")

    except IOError as e:
        print(f"\nERROR: No se pudo abrir o leer el archivo CSV: {e}")
        
    print(f"\n[+] Lectura completa. Total de {len(datos)} países cargados.")
    return datos

def mostrar_lista_paises(lista_paises, titulo="Lista de Países"):
    # Muestra la lista de países en un formato legible.
    print("\n" + "="*80)
    print(f"{titulo.center(80)}")
    print("="*80)
    
    if not lista_paises:
        print("No se encontraron resultados para mostrar.")
        print("="*80)
        return

    # Table de encabezados (ajustado a tus campos)
    print(f"{'Nombre':<20} | {'Población (hab)':<20} | {'Superficie (km²)' :<20} | {'Continente':<15}")
    print("-" * 80)
    
    # Mostrar cada pais
    for pais in lista_paises:
        # Formatear números grandes para una mejor legibilidad
        poblacion_fmt = f"{pais['poblacion']:,}".replace(",", ".")
        superficie_fmt = f"{pais['superficie']:,}".replace(",", ".")
        
        print(
            f"{pais['nombre']:<20} | {poblacion_fmt:<20} | {superficie_fmt:<20} | {pais['continente']:<15}"
        )
    
    print("="*80)