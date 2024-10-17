# Encabezado de la tabla de verdad
print("A | B | A OR B")
print("--|---|-------")

# Posibles combinaciones de valores booleanos para A y B
for A in [0, 1]:
    for B in [0, 1]:
        resultado = A or B  # Operación OR
        print(f"{A} | {B} |   {resultado}")
