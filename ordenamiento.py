# Módulo para la opción de ordenamiento.

import utilidades

def ordenar_paises(lista_paises):

    if not lista_paises:
        print("ERROR: No hay datos cargados para ordenar.")
        return

    while True:
        print("\n--- Submenú de Ordenamiento ---")
        print("1. Por Nombre (Alfabético)")
        print("2. Por Población")
        print("3. Por Superficie")
        print("0. Volver al Menú Principal")
        opcion_campo = input("Seleccione el campo para ordenar: ").strip()

        if opcion_campo == '0':
            break
        
        elif opcion_campo == '1':
            key = 'nombre'
            titulo_campo = 'Nombre'
            # Orden alfabetico ascendente
            _aplicar_ordenamiento(lista_paises, key, titulo_campo, reverse=False)
            break
            
        elif opcion_campo in ['2', '3']:
            key = 'poblacion' if opcion_campo == '2' else 'superficie'
            titulo_campo = 'Población' if opcion_campo == '2' else 'Superficie'
            
            while True:
                orden = input(f"Ordenar por {titulo_campo}: (A)scendente o (D)escendente? ").strip().lower()
                if orden in ['d', 'a']:
                    reverse = (orden == 'd')
                    _aplicar_ordenamiento(lista_paises, key, titulo_campo, reverse)
                    return # Regresa al menú principal después de mostrar el resultado
                else:
                    print("Opción no válida. Ingrese 'A' o 'D'.")
        else:
            print("Opción no válida. Intente de nuevo.")


def _aplicar_ordenamiento(lista_paises, key, titulo_campo, reverse):

    # Utilice sorted() para crear una NUEVA lista ordenada
    lista_ordenada = sorted(
        lista_paises, 
        key=lambda pais: pais[key], 
        reverse=reverse
    )
    
    direccion = "Descendente" if reverse else "Ascendente"
    utilidades.mostrar_lista_paises(
        lista_ordenada, 
        f"Países Ordenados por {titulo_campo} ({direccion})"
    )
