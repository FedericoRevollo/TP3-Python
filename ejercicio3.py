# Cree una funcion que determine que numero de una serie de N numeros es mayor

def encontrar_mayor():
    try:
        # Solicitar la cantidad de números
        n = int(input("Ingrese la cantidad de números: "))
        if n <= 0:
            print("La cantidad de números debe ser mayor que cero.")
            return
        
        # Inicializar el mayor
        mayor = None
        
        # Recopilar los números y encontrar el mayor
        for i in range(n):
            numero = float(input(f"Ingrese el número {i + 1}: "))
            if mayor is None or numero > mayor:
                mayor = numero
        
        # Imprimir el mayor
        print(f"El número mayor de la serie es: {mayor}")
    except ValueError:
        print("Por favor, ingrese un número válido.")

# Llamar a la función
encontrar_mayor()
