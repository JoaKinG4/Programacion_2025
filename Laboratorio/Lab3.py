print("====REGISTROS AÑOS 2025 DE TRES CIUDADES ARCHIPIELAGO DE CHILOE====")

#DICCIONARIO DE REGISTROS (A)
registros = {
    5700000 : {'Ciudad':  'Castro', 'Temperatura Promedio Anual (°C)': 11.8, 'Precipitacion Total (mm)': 2000},
    5770000: {'Ciudad': 'Chonchi', 'Temperatura Promedio Anual (°C)': 8.3, 'Precipitacion Total (mm)': 2800},
    5790000: {'Ciudad': 'Quellón', 'Temperatura Promedio Anual (°C)': 10.2, 'Precipitacion Total (mm)': 2950}
}
print(registros)


#CLIMA DE CADA CIUDAD DE ACUERDO A SU TEMPERATURA (B)
try:
    temp_castro = registros[5700000]['Temperatura Promedio Anual (°C)']
    if temp_castro < 10:
            print('Clima Frio')
    elif temp_castro >= 10 < 15:
            print("Clima Templado")
    else:
        print("Clima Calido")
except:
    registros[5700000]['Temperatura Promedio Anual (°C)'] = 'Desconocida'

try:
    temp_chonchi = registros[5770000]['Temperatura Promedio Anual (°C)']
    if temp_chonchi < 10:
            print('Clima Frio')
    elif temp_chonchi >= 10 < 15:
            print("Clima Templado")
    else:
        print("Clima Calido")
except:
    registros[5770000]['Temperatura Promedio Anual (°C)'] = 'Desconocida'

try:
    temp_quellon = registros[5790000]['Temperatura Promedio Anual (°C)']
    if temp_quellon < 10:
            print('Clima Frio')
    elif temp_quellon >= 10 < 15:
            print("Clima Templado")
    else:
        print("Clima Calido")
except:
    registros[5790000]['Temperatura Promedio Anual (°C)'] = 'Desconocida'

#MESES LLUVIOSOS CASTRO (C)
meses_lluviosos = ()



#CAMBIO DE VALOR CIUDAD PARA CHONCHI (D)





#CREAR LISTA LLUVIAS (E)
lluvias = (2000, 2800, 2950)
suma_total_lluvias = sum(lluvias)
lluvia_min = min(lluvias)
lluvia_max = max(lluvias)
print('El total de precipitaciones es: ')
print(suma_total_lluvias)
print('La lluvia minima es de:')
print(lluvia_min)
print("La lluvia maxima es de: ")
print(lluvia_max)


#IMPRIMIR NUEVAMENTE EL DICCIONARIO CON SUS CAMBIOS
print(registros)



