# Cree una funcion que determine si un color es primario o no, se debe imprimir porpantalla la leyenda “el color X es primero “ o “el color X no es primario”

def determinar_color_primario():
    # Lista de colores primarios
    colores_primarios = {"rojo", "azul", "amarillo"}
    
    # Pedir al usuario que ingrese un color
    color = input("Ingrese un color: ").strip().lower()
    
    # Verificar si el color está en la lista de colores primarios
    if color in colores_primarios:
        print(f"El color {color} es primario.")
    else:
        print(f"El color {color} no es primario.")

# Llamar a la función
determinar_color_primario()
