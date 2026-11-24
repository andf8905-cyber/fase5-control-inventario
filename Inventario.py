
# FASE 5 - EVALUACION FINAL POA
# PROBLEMA 3: CONTROL DE INVENTARIO Y REABASTECIMIENTO

# Funcion para calcular la cantidad que se debe solicitar
def calcular_reabastecimiento(stock_actual, stock_minimo):

    if stock_actual < stock_minimo:
        cantidad_pedir = stock_minimo - stock_actual
    else:
        cantidad_pedir = 0

    return cantidad_pedir


# Matriz de inventario
# [Codigo, Nombre, Stock actual, Stock minimo]

inventario = [
    ["A001", "Teclado", 5, 15],
    ["A002", "Mouse", 20, 10],
    ["A003", "Monitor", 3, 8],
    ["A004", "Audifonos", 4, 12],
    ["A005", "Webcam", 15, 15]
]


# Mostrar los resultados del inventario
print("==============================================")
print("       SISTEMA DE CONTROL DE INVENTARIO")
print("==============================================")

for articulo in inventario:

    codigo = articulo[0]
    nombre = articulo[1]
    stock_actual = articulo[2]
    stock_minimo = articulo[3]

    cantidad_pedir = calcular_reabastecimiento(
        stock_actual, stock_minimo
    )

    print("----------------------------------------------")
    print("Codigo:", codigo)
    print("Articulo:", nombre)
    print("Stock actual:", stock_actual)
    print("Stock minimo:", stock_minimo)
    print("Cantidad a solicitar:", cantidad_pedir)

    if cantidad_pedir > 0:
        print("Estado: Requiere reabastecimiento")
    else:
        print("Estado: Stock suficiente")

print("==============================================")
print("       FIN DEL REPORTE DE INVENTARIO")
print("==============================================")
