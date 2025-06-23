# CREANDO EL DICCIONARIO
vendedores = {
"Joaquin": [250000, 150000, 200000, 300000, 100000],
"Yerko": [500000, 250000, 300000, 220000, 180000],
"Matias": [170000, 190000, 210000, 350000, 210000]
}

# SUELDO BASE
sueldo_base = 529000

# FUNCION PARA VER SI LE CORRESPONDE EL BONO
def calcular_bono(total_ventas):
    if total_ventas > 1500000:
        return sueldo_base * 0.20
    elif total_ventas > 1000000:
        return sueldo_base * 0.10
    elif total_ventas > 500000:
        return sueldo_base * 0.05
    else:
        return 0
    
print("REPORTE DE SUELDO SEMANAL POR VENDEDOR:\n")

for vendedor, ventas in vendedores.items():
    total_ventas = sum(ventas)
    bono = calcular_bono(total_ventas)
    sueldo_total = sueldo_base + bono
    promedio_ventas = total_ventas / len(ventas)

    print(f"Vendedor: {vendedor}")
    print(f"  Total ventas semanales: ${total_ventas:,.0f}")
    print(f"  Bono: ${bono:,.0f}")
    print(f"  Promedio diario de ventas: ${promedio_ventas:,.0f}")
    print(f"  Sueldo total a pagar: ${sueldo_total:,.0f}")
    print("-" * 40)