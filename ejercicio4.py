# Cree una funcion que dibuje un rectangulo de X filas y X columnas determinadas por elusuario

def dibujar_rectangulo():
    try:
        # Solicitar filas y columnas al usuario
        filas = int(input("Ingrese la cantidad de filas: "))
        columnas = int(input("Ingrese la cantidad de columnas: "))
        
        if filas <= 0 or columnas <= 0:
            print("La cantidad de filas y columnas debe ser mayor que cero.")
            return
        
        # Dibujar el rectángulo
        for _ in range(filas):
            print("*" * columnas)
    except ValueError:
        print("Por favor, ingrese números válidos.")

# Llamar a la función
dibujar_rectangulo()
