# Orquestador del Trabajo Práctico Integrador
# Maneja el menú principal e importa la funcionalidad de otros módulos.

# Importamos solo las funciones específicas que necesitamos de cada módulo
import utilidades
import busquedas_filtros
import ordenamiento
import estadisticas

# Variable global para almacenar todos los datos de los países
PAISES = []

def inicializar_datos():
    """Carga los datos al iniciar y los muestra."""
    global PAISES
    # utilidades.cargar_datos_desde_csv() devuelve la lista de países
    PAISES = utilidades.cargar_datos_desde_csv()
    utilidades.mostrar_lista_paises(PAISES, "Datos Iniciales Cargados")

def mostrar_menu():
    """Muestra el menú de opciones en consola."""
    print("\n" + "*"*50)
    print("GESTIÓN DE DATOS DE PAÍSES (TPI)".center(50))
    print("*"*50)
    print("1. Cargar/Recargar Datos (CSV)")
    print("2. Buscar País por Nombre")
    print("3. Filtrar Países (Continente/Rango)")
    print("4. Ordenar Países")
    print("5. Mostrar Estadísticas")
    print("0. Salir")
    print("*"*50)

def main():
    """Función principal del programa."""
    global PAISES
    
    inicializar_datos() 

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        # Validar si hay datos cargados para las opciones que lo requieren
        if opcion in ['2', '3', '4', '5'] and not PAISES:
            print("\nADVERTENCIA: No hay datos cargados para esta operación. Use la Opción 1 primero.")
            continue

        if opcion == '1':
            inicializar_datos()
            
        elif opcion == '2':
            # Llamamos a la función del módulo busquedas_filtros
            busquedas_filtros.buscar_pais_por_nombre(PAISES)
            
        elif opcion == '3':
            # Llamamos a la función del módulo busquedas_filtros
            busquedas_filtros.filtrar_paises(PAISES)
            
        elif opcion == '4':
            # Llamamos a la función del módulo ordenamiento
            ordenamiento.ordenar_paises(PAISES)
            
        elif opcion == '5':
            # Llamamos a la función del módulo estadisticas
            estadisticas.calcular_estadisticas(PAISES)
            
        elif opcion == '0':
            print("¡Gracias por usar el sistema! Saliendo...")
            break
            
        else:
            print("Opción no válida. Por favor, ingrese un número del 0 al 5.")

if __name__ == "__main__":
    main()
