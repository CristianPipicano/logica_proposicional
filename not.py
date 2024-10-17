# Encabezado de la tabla de verdad
print("A | NOT A")
print("--|------")

# Posibles valores de la entrada A
for A in [0, 1]:
    resultado = not A  # Operación NOT
    print(f"{A} |   {int(resultado)}")
