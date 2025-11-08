# Módulo para validar las entradas del usuario.

def validar_entero_positivo(prompt, puede_ser_cero=True):
    while True:
        valor_str = input(prompt).strip()
        if not valor_str:
            return None 
        
        try:
            valor = int(valor_str)
            if valor < 0:
                print("Error: El valor debe ser un número positivo (o cero).")
            elif valor == 0 and not puede_ser_cero:
                print("Error: El valor no puede ser cero.")
            else:
                return valor
        except ValueError:
            print("Error: Ingrese solo números enteros válidos.")


def existe_nombre_pais(lista_paises, nombre_a_verificar, pais_actual=None):

    for pais in lista_paises:
        # Si estamos en modificación y el país en la lista es el mismo que editamos, lo ignoramos
        if pais_actual and pais is pais_actual:
            continue
        
        if pais.get('nombre', '').lower() == nombre_a_verificar.lower():
            return True
    return False

# Función de Alta 

def solicitar_datos_pais_validados(lista_paises):
    nuevo_pais = {}
    print("\n-- Ingrese los datos del nuevo país --")
    
    while True:
        nombre = input(" -> Nombre: ").strip()
        if not nombre:
            print("El nombre no puede estar vacío.")
        elif existe_nombre_pais(lista_paises, nombre):
            print(f"ERROR: El país '{nombre}' ya existe en el dataset. Intente con otro nombre.")
        else:
            nuevo_pais['nombre'] = nombre
            break

    while True:
        continente = input(" -> Continente: ").strip()
        if not continente:
            print("El continente no puede estar vacío.")
        else:
            nuevo_pais['continente'] = continente
            break

    while True:
        # Se pasa un prompt vacío ya que la función ya usa input() internamente
        poblacion = validar_entero_positivo(" -> Población (entero): ", puede_ser_cero=True)
        # Si validar_entero_positivo devuelve None (porque se dejó vacío), lo tratamos como error en Alta
        if poblacion is not None:
            nuevo_pais['poblacion'] = poblacion
            break
        else:
            print("La población es un campo obligatorio para la Alta.")
        
    while True:
        superficie = validar_entero_positivo(" -> Superficie (entero, km²): ", puede_ser_cero=True)
        if superficie is not None:
            nuevo_pais['superficie'] = superficie
            break
        else:
            print("La superficie es un campo obligatorio para la Alta.")
            
    return nuevo_pais

# Función de Modificación (solicita solo los campos a editar)

def solicitar_datos_edicion_validados(pais_actual, lista_paises):
    # Solicita nuevos datos para un país, validando solo los campos ingresados.
    datos_actualizados = {}
    
    print("\n-- Deje el campo vacío para mantener el valor actual --")
    
    # 1. Modificar Nombre
    nombre_nuevo = input(f" -> Nombre (Actual: {pais_actual['nombre']}): ").strip()
    if nombre_nuevo:
        if existe_nombre_pais(lista_paises, nombre_nuevo, pais_actual):
            print(f"ERROR: El nombre '{nombre_nuevo}' ya está en uso por otro país. No se modificó el nombre.")
        else:
            datos_actualizados['nombre'] = nombre_nuevo

    # 2. Modificar Continente
    continente_nuevo = input(f" -> Continente (Actual: {pais_actual['continente']}): ").strip()
    if continente_nuevo:
        datos_actualizados['continente'] = continente_nuevo

    # 3. Modificar Población
    # Llamamos a validar_entero_positivo con el prompt ya formateado
    valor_poblacion = validar_entero_positivo(f" -> Población (Actual: {pais_actual['poblacion']:,d}, Ingrese nuevo valor): ", puede_ser_cero=True)
    
    if valor_poblacion is not None:
        # Solo se actualiza si el valor es válido (no None)
        datos_actualizados['poblacion'] = valor_poblacion
    elif valor_poblacion is None and input("¿Desea cambiar el valor a 0? (s/N): ").lower() == 's':
        datos_actualizados['poblacion'] = 0


    # 4. Modificar Superficie
    valor_superficie = validar_entero_positivo(f" -> Superficie (Actual: {pais_actual['superficie']:,d}, Ingrese nuevo valor): ", puede_ser_cero=True)
    
    if valor_superficie is not None:
        # Solo se actualiza si el valor es válido (no None)
        datos_actualizados['superficie'] = valor_superficie
    elif valor_superficie is None and input("¿Desea cambiar el valor a 0? (s/N): ").lower() == 's':
        datos_actualizados['superficie'] = 0
            
    return datos_actualizados