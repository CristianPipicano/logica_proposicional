# Encabezado de la tabla de verdad
print("A | B | A → B")
print("--|---|-------")

# Posibles combinaciones de valores booleanos para A y B
for A in [0, 1]:
    for B in [0, 1]:
        resultado = (not A) or B  # Operación de implicación
        print(f"{A} | {B} |   {int(resultado)}")
