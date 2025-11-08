# Módulo: main.py
# Orquestador del Trabajo Práctico Integrador
# Maneja el menú principal e importa la funcionalidad de otros módulos.

# Importamos las funcionalidades de los módulos auxiliares
import utilidades
import busquedas_filtros
import ordenamiento
import estadisticas

# Importaciones específicas para CRUD (Crear, Modificar, Guardar, Validar)
from utilidades import guardar_datos_csv
from validaciones import solicitar_datos_pais_validados, solicitar_datos_edicion_validados

# Variable global para almacenar todos los datos de los países
PAISES = []
NOMBRE_ARCHIVO = "dataset_paises.csv" 

def inicializar_datos():
    """Carga los datos al iniciar el programa."""
    global PAISES
    # Llamamos a la función de utilidades para la carga
    PAISES = utilidades.cargar_datos_desde_csv()

def mostrar_menu():
    """Muestra el menú de opciones en consola."""
    print("\n" + "="*50)
    print("GESTIÓN DE DATOS DE PAÍSES (TPI)".center(50))
    print("="*50)
    print("1. Cargar/Recargar Datos (CSV)")
    print("2. Mostrar Todos los Países") 
    print("--- Operaciones CRUD ---")
    print("3. Alta de Registro (Crear Nuevo País)")
    print("4. Modificar Registro (Editar País Existente)")
    print("5. Eliminar Registro (Baja)") 
    print("--- Consultas y Análisis ---")
    # Las opciones 6, 7, 8, 9 se mapean a las funciones originales
    print("6. Búsqueda por Nombre") 
    print("7. Filtrar Países (Continente/Rango)") 
    print("8. Ordenar Países") 
    print("9. Mostrar Estadísticas") 
    print("0. Salir del Programa")
    print("="*50)

# ------------------------------------------------------------------
# Funciones de CRUD (Alta, Modificación, Baja)
# ------------------------------------------------------------------

def alta_registro(lista_paises):
    """Permite crear y agregar un nuevo país a la lista."""
    print("\n--- CREACIÓN DE NUEVO REGISTRO ---")
    if not lista_paises:
        print("⚠️ Advertencia: La lista de países está vacía. Se creará el primer registro.")

    # Llama a la función en validaciones.py para solicitar y validar datos
    new_pais = solicitar_datos_pais_validados(lista_paises)

    if new_pais:
        lista_paises.append(new_pais)
        print(f"\n✅ País '{new_pais['nombre']}' agregado exitosamente a la lista en memoria.")
        # Guarda el cambio en el CSV inmediatamente
        guardar_datos_csv(lista_paises, NOMBRE_ARCHIVO)
    else:
        # Esto solo ocurre si la validación falla y no se pudo completar el registro
        print("\n❌ No se pudo crear el registro. Operación cancelada.")


def modificar_registro(lista_paises):
    """Permite buscar y modificar un país existente."""
    print("\n--- MODIFICACIÓN DE REGISTRO ---")
    
    nombre_a_modificar = input("Ingrese el nombre del país a modificar: ").strip()
    
    # Lógica para buscar el país por nombre
    indice_a_modificar = -1
    pais_encontrado = None
    for i, pais in enumerate(lista_paises):
        if pais.get('nombre', '').lower() == nombre_a_modificar.lower():
            indice_a_modificar = i
            pais_encontrado = pais
            break

    if indice_a_modificar != -1:
        print(f"\n📢 País encontrado: {pais_encontrado['nombre']} - Datos actuales:")
        utilidades.mostrar_lista_paises([pais_encontrado], "Registro a Modificar")
        
        # Llama a la función en validaciones.py para solicitar y validar los cambios
        datos_actualizados = solicitar_datos_edicion_validados(pais_encontrado, lista_paises)

        if datos_actualizados:
            # Actualizar el diccionario con los nuevos datos
            pais_encontrado.update(datos_actualizados)
            print(f"\n✅ País '{pais_encontrado['nombre']}' modificado exitosamente en memoria.")
            # Guarda el cambio en el CSV
            guardar_datos_csv(lista_paises, NOMBRE_ARCHIVO)
        else:
            print("\n❌ Modificación cancelada (no se ingresó ningún dato válido para actualizar).")
    else:
        print(f"\n❌ ERROR: No se encontró ningún país con el nombre '{nombre_a_modificar}'.")


def baja_registro(lista_paises):
    """Permite buscar y eliminar un país existente."""
    print("\n--- ELIMINACIÓN DE REGISTRO (BAJA) ---")
    
    nombre_a_eliminar = input("Ingrese el nombre del país a ELIMINAR: ").strip()
    
    # Lógica para buscar el país por nombre
    indice_a_eliminar = -1
    pais_encontrado = None
    for i, pais in enumerate(lista_paises):
        if pais.get('nombre', '').lower() == nombre_a_eliminar.lower():
            indice_a_eliminar = i
            pais_encontrado = pais
            break

    if indice_a_eliminar != -1:
        print(f"\n⚠️ REGISTRO ENCONTRADO PARA ELIMINAR:")
        utilidades.mostrar_lista_paises([pais_encontrado], f"País {pais_encontrado['nombre']}")
        
        # Importante: confirmar antes de borrar
        confirmacion = input("¿Está seguro de que desea eliminar este país? (S/N): ").strip().lower()
        
        if confirmacion == 's':
            
            longitud_inicial = len(lista_paises) 
            
            # ELIMINACIÓN: Remueve de la lista en memoria usando el índice
            pais_eliminado = lista_paises.pop(indice_a_eliminar)
            
            longitud_final = len(lista_paises) 

            print(f"\n✅ País '{pais_eliminado['nombre']}' ELIMINADO exitosamente de la memoria.")
            print(f"   (Longitud: {longitud_inicial} -> {longitud_final})") 

            # GUARDA EN EL CSV: Sobrescribe el archivo con la lista actualizada
            guardar_datos_csv(lista_paises, NOMBRE_ARCHIVO)
            
            # MUESTRA VISUAL: Confirma la lista actualizada
            print("\n--- Vista de la Lista después de la Baja (en Memoria) ---")
            utilidades.mostrar_lista_paises(lista_paises, "Lista Actualizada en Memoria (Opción 5)")

        else:
            print("\n❌ Eliminación cancelada por el usuario.")
    else:
        print(f"\n❌ ERROR: No se encontró ningún país con el nombre '{nombre_a_eliminar}'.")


# ------------------------------------------------------------------
# Función principal (Loop del programa)
# ------------------------------------------------------------------

def main():
    """Función principal del programa."""
    global PAISES
    
    inicializar_datos() 

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        # Validar si hay datos cargados para las opciones que lo requieren
        if opcion in ['2', '3', '4', '5', '6', '7', '8', '9'] and not PAISES:
            print("\nADVERTENCIA: No hay datos cargados para esta operación. Use la Opción 1 primero.")
            continue
            
        elif opcion == '1':
            inicializar_datos()
        
        elif opcion == '2':
            # Muestra todos los países 
            utilidades.mostrar_lista_paises(PAISES, "LISTA COMPLETA DE PAÍSES")
            
        elif opcion == '3':
            alta_registro(PAISES)
            
        elif opcion == '4':
            modificar_registro(PAISES)
            
        elif opcion == '5':
            baja_registro(PAISES) 
            
        elif opcion == '6':
            # NOTA: Tu módulo busquedas_filtros.py tiene una función buscar_pais_por_nombre
            busquedas_filtros.buscar_pais_por_nombre(PAISES)
            
        elif opcion == '7':
            # NOTA: Tu módulo busquedas_filtros.py tiene una función filtrar_paises
            busquedas_filtros.filtrar_paises(PAISES)
            
        elif opcion == '8':
            # NOTA: Tu módulo ordenamiento.py tiene una función ordenar_paises
            ordenamiento.ordenar_paises(PAISES)
            
        elif opcion == '9':
            # NOTA: Tu módulo estadisticas.py tiene una función calcular_estadisticas
            estadisticas.calcular_estadisticas(PAISES)

        elif opcion == '0':
            print("¡Gracias por usar el sistema! Saliendo...")
            break
        else:
            print("❌ Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()