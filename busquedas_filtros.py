# Módulo para las opciones de búsqueda por nombre y filtrado por criterios.

import utilidades
import validaciones

def buscar_pais_por_nombre(lista_paises):
    """
    (Opción 2) Searches for countries by partial name match.
    """
    if not lista_paises:
        print("ERROR: No hay datos cargados para buscar.")
        return

    termino = input("Ingrese el nombre (o parte del nombre) del país a buscar: ").strip().lower()

    if not termino:
        print("Búsqueda cancelada.")
        return

    resultados = []
    for pais in lista_paises:
        if termino in pais['nombre'].lower():
            resultados.append(pais)

    utilidades.mostrar_lista_paises(resultados, f"Resultados de Búsqueda para '{termino}'")

def filtrar_paises(lista_paises):
    """
    (Opción 3) Shows a submenu to apply different filters.
    """
    if not lista_paises:
        print("ERROR: No hay datos cargados para filtrar.")
        return

    while True:
        print("\n--- Submenú de Filtros ---")
        print("1. Filtrar por Continente")
        print("2. Filtrar por Rango de Población")
        print("3. Filtrar por Rango de Superficie")
        print("0. Volver al Menú Principal")
        opcion = input("Seleccione una opción de filtro: ").strip()

        if opcion == '1':
            filtro_continente(lista_paises)
        elif opcion == '2':
            filtro_por_rango(lista_paises, 'poblacion', 'Población')
        elif opcion == '3':
            filtro_por_rango(lista_paises, 'superficie', 'Superficie')
        elif opcion == '0':
            break
        else:
            print("Opción no válida. Intente de nuevo.")


def filtro_continente(lista_paises):
    """
    Filters the list of countries by the continent entered.
    """
    continente = input("Ingrese el Continente a filtrar (ej: America, Asia): ").strip().capitalize()
    
    if not continente:
        print("Filtro cancelado.")
        return

    resultados = [pais for pais in lista_paises if pais['continente'] == continente]
    
    utilidades.mostrar_lista_paises(resultados, f"Países Filtrados por Continente: {continente}")


def filtro_por_rango(lista_paises, key, display_name):
    """
    Filters the list of countries by a given numerical range (population or area).
    """
    rango = validaciones.obtener_rango_valido(display_name)
    
    if rango is None:
        print(f"Filtro de {display_name} cancelado o inválido.")
        return
        
    min_val, max_val = rango
    
    resultados = [pais for pais in lista_paises if min_val <= pais[key] <= max_val]
    
    utils.mostrar_lista_paises(
        resultados, 
        f"Países Filtrados por Rango de {display_name} ({min_val:,} - {max_val:,})"
    )
