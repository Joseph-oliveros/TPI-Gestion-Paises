# Módulo para validar las entradas del usuario.

def validar_entero_positivo(prompt):
    """
    Solicita un valor al usuario y valida que sea un número entero positivo.
    """
    while True:
        valor_str = input(prompt).strip()
        if not valor_str:
            return None
        
        try:
            valor = int(valor_str)
            if valor >= 0:
                return valor
            else:
                print("Error: El valor debe ser un número positivo (o cero).")
        except ValueError:
            print("Error: Ingrese solo números enteros válidos.")
            
def obtener_rango_valido(key_name):
    """
    Solicita un rango (mínimo y máximo) y valida que sean números.
    """
    print(f"\n--- Ingrese Rango de {key_name} ---")
    min_val = validar_entero_positivo(f"Mínimo de {key_name}: ")
    
    if min_val is None:
        return None
    
    max_val = validar_entero_positivo(f"Máximo de {key_name}: ")

    if max_val is None:
        max_val = min_val 
    
    if min_val > max_val:
        print(f"Error: El valor Mínimo ({min_val}) no puede ser mayor que el Máximo ({max_val}).")
        return None
        
    return min_val, max_val
