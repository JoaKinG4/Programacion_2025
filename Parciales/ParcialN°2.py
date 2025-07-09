#CREANDO EL DICCIONARIO Y SUB-DICCIONARIOS (A)
gatitos = {
        101 : {"Nombre": "Luna",
            "Peso": 1.2,
            "Edad (Meses)": 3,
            "Tamaño (cm)": 30},

        102 : {"Nombre": "Michi",
            "Peso": 0.8,
            "Edad (Meses)": 2,
            "Tamaño (cm)": 25},

        103 : {"Nombre": "Pepito",
            "Peso": 2.5,
            "Edad (Meses)": 5,
            "Tamaño (cm)": 35}
}

# RECORRER  EL DICCIONARIO CON UN BUCLE
for clasificacion_peso in gatitos:
        if 0 < 1:
            print("Bajo peso")
        elif 1 >= 4:
                print("Peso Normal")
        else:
                print("Sobre peso")

for categoria_etaria in gatitos:
    try:
        if 0 < 4:
            print("Cachorro")
        elif 4 <= 12:
            print("Joven")
        else:
            print("Adulto")
    except:
        print("Desconocida")



# CREAR UNA LISTA CON LOS PESOS 
lista_pesos = (1.2, 0.8, 2.5)
max_peso = max(lista_pesos)
min_peso = min(lista_pesos)
suma_pesos = sum(lista_pesos)
promedio_peso = suma_pesos / 3
print("Maximo Peso:", max_peso,"Peso Minimo:", min_peso, "Peso Promedio:", promedio_peso)


#IMPRIMIR DICCIONARIO COMPLETO
print(gatitos)