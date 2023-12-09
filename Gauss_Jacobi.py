def gauss_Jacobi(matriz_coeficientes,vectores,tolerancia = 1e-10,max_iteraciones=1000):
    num = len(matriz_coeficientes)
    x = [0.0] * num

    iteraciones_deseadas = int(input("Ingrese el número máximo de iteraciones que quieras calcular: "))
    for iteraciones in range(iteraciones_deseadas):
        x_anterior = x.copy()
        for i in range(num):
            suma = sum(matriz_coeficientes[i][j] * x_anterior[j] for j in range(num) if i != j)
            x[i] = (vectores[i] - suma) / matriz_coeficientes[i][i]

            # Calcular el error
            errores = [abs((x[i] - x_anterior[i]) / x[i]) * 100 if x[i] != 0 else 0 for i in range(num)]
            error_max = max(errores)

            print(f"Iteración {iteraciones + 1}:")
            for i in range(num):
                variable = chr(ord('x') + i)
                print(f"{variable}{iteraciones + 1} = {x[i]:.6f}   Error{variable} = {errores[i]:.6f}%")

            print(f"Error máximo = {error_max:.6f}%")

            # Comprobar convergencia
            if error_max < tolerancia:
                print("\nConvergencia alcanzada.")
                return x
    raise Exception(f"No se alcanzó la convergencia después de {max_iteraciones} iteraciones.")

def ingresar_matriz():
    n = int(input("Ingrese el tamaño de la matriz (n): "))
    matriz_coeficientes = []
    vector_constantes = []

    print("Ingrese los coeficientes de la matriz:")
    for i in range(n):
        fila = [float(input(f"Coeficiente a[{i+1}][{j+1}]: ")) for j in range(n)]
        matriz_coeficientes.append(fila)

    print("\nIngrese el vector de términos constantes:")
    for i in range(n):
        constante = float(input(f"Término constante b[{i+1}]: "))
        vector_constantes.append(constante)

    return matriz_coeficientes, vector_constantes

if __name__ == "__main__":
    matriz_coeficientes, vectores = ingresar_matriz()
    try:
        solucion = gauss_Jacobi(matriz_coeficientes,vectores)
        print("\nLa solución del sistema de ecuaciones es:")
        for i, valor in enumerate(solucion):
            variable = chr(ord('x') + i)
            print(f"{variable}{len(solucion)} = {valor}")
    except ValueError as e:
        print(e)
