# Realizando variables
suma = 500
actual = 500
aumento = 54
menos = 56
operatoria = True  # True = suma, False = resta

# Bucle llegando hasta al 800 o pasandolo
while actual < 800:
    if operatoria:
        actual += aumento
        aumento += 12  # patrón creciente
    else:
        actual -= menos
        menos += 12
    suma += actual
    operatoria = not operatoria

# Resultado
print("La sumatoria es:", suma)
