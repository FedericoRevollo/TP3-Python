# Cree una funcion que calcule el promedio de N notas

def calcular_promedio():
    try:
        n = int(input("Ingrese la cantidad de notas: "))
        if n <= 0:
            print("La cantidad de notas debe ser mayor que cero.")
            return
        
        notas = []
        for i in range(n):
            nota = float(input(f"Ingrese la nota {i + 1}: "))
            if nota < 0 or nota > 10:
                print("La nota debe estar entre 0 y 10.")
                return
            notas.append(nota)
        
        promedio = sum(notas) / n
        print(f"El promedio de las notas es: {promedio:.2f}")
    except ValueError:
        print("Por favor, ingrese valores numéricos válidos.")

# Llamar a la función
calcular_promedio()
