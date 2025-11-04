
# Módulo para calcular y mostrar estadísticas clave.

def contar_por_continente(lista_paises):
    conteo = {}
    for pais in lista_paises:
        continente = pais['continente']
        conteo[continente] = conteo.get(continente, 0) + 1
    return conteo


def calcular_estadisticas(lista_paises):
    if not lista_paises:
        print("ERROR: No hay datos cargados para calcular estadísticas.")
        return
        
    print("\n" + "="*60)
    print("RESUMEN DE ESTADÍSTICAS GLOBALES".center(60))
    print("="*60)

    # 1. Países con mayor y menor población
    pais_mayor_pob = max(lista_paises, key=lambda p: p['poblacion'])
    pais_menor_pob = min(lista_paises, key=lambda p: p['poblacion'])
    
    print("A) País con Mayor Población:".ljust(35) + f"{pais_mayor_pob['nombre']} ({pais_mayor_pob['poblacion']:,})")
    print("B) País con Menor Población:".ljust(35) + f"{pais_menor_pob['nombre']} ({pais_menor_pob['poblacion']:,})")
    print("-" * 60)
    
    # 2. Población y área promedio
    total_poblacion = sum(p['poblacion'] for p in lista_paises)
    total_superficie = sum(p['superficie'] for p in lista_paises)
    
    num_paises = len(lista_paises)
    
    promedio_poblacion = total_poblacion / num_paises
    promedio_superficie = total_superficie / num_paises
    
    print("C) Promedio de Población:".ljust(35) + f"{promedio_poblacion:,.0f} habitantes")
    print("D) Promedio de Superficie:".ljust(35) + f"{promedio_superficie:,.0f} km²")
    print("-" * 60)

    # 3. Número de países por continente
    conteo_continentes = contar_por_continente(lista_paises)
    print("E) Cantidad de países por Continente:")
    for continente, count in conteo_continentes.items():
        print(f"   - {continente}: {count} países")
        
    print("="*60)