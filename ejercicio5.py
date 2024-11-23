# Cree una funcion que calcule el Factorial de un numero entero positivo

def calcular_factorial():
    try:
        # Solicitar un número al usuario
        numero = int(input("Ingrese un número entero positivo: "))
        
        # Validar que el número sea positivo
        if numero < 0:
            print("El número debe ser entero y positivo.")
            return
        
        # Calcular el factorial
        factorial = 1
        for i in range(1, numero + 1):
            factorial *= i
        
        # Mostrar el resultado
        print(f"El factorial de {numero} es: {factorial}")
    except ValueError:
        print("Por favor, ingrese un número entero válido.")

# Llamar a la función
calcular_factorial()
