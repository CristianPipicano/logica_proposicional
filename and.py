# Encabezado de la tabla de verdad
print("A | B | A AND B")
print("--|---|--------")

# Posibles combinaciones de valores booleanos para A y B
for A in [0, 1]:
    for B in [0, 1]:
        resultado = A and B  # Operación AND
        print(f"{A} | {B} |   {resultado}")

