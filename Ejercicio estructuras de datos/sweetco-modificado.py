def pedirEntero(mensaje, minimo=0):
    """Pide un número entero y vuelve a preguntar si el dato no es válido."""
    while True:
        try:
            valor = int(input(mensaje))
            if valor < minimo:
                print(f"  El valor debe ser mayor o igual a {minimo}.")
            else:
                return valor
        except ValueError:
            print("  Debes ingresar un número entero.")


def llenarDatos(dias):
    """Llena la lista de precios y la matriz de ventas con datos del usuario."""
    numProductos = pedirEntero("¿Cuántos productos vende SweetCO? ", 1)

    lstPrecios = []
    matVentas = []

    for p in range(numProductos):
        print(f"\n--- Producto {p + 1} ---")
        precio = pedirEntero(f"Precio del producto {p + 1}: $", 1)
        lstPrecios.append(precio)

        fila = []
        for d in range(len(dias)):
            unidades = pedirEntero(f"  Unidades vendidas el {dias[d]}: ")
            fila.append(unidades)
        matVentas.append(fila)

    return matVentas, lstPrecios


# Ingresos totales por producto en la semana
def lstTotalesProdxSem(ventas, precios):
    filas = len(ventas)
    cols = len(ventas[0])
    lstTotales = []
    for f in range(filas):
        suma = 0
        for c in range(cols):
            suma = suma + ventas[f][c] * precios[f]
        lstTotales.append(suma)
    return lstTotales


#  Ingresos totales por día de la semana
def lstTotalesDiaxSem(ventas, precios):
    filas = len(ventas)
    cols = len(ventas[0])
    lstTotales = []
    for c in range(cols):
        suma = 0
        for f in range(filas):
            suma = suma + ventas[f][c] * precios[f]
        lstTotales.append(suma)
    return lstTotales




dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

print("===== SweetCO: control de ventas semanales =====")
matVentas, lstPrecios = llenarDatos(dias)

lstTotales = lstTotalesProdxSem(matVentas, lstPrecios)
maxTotal = max(lstTotales)
prodVentasMax = lstTotales.index(maxTotal) + 1
print(f"\nEl producto {prodVentasMax} es el que más ingresos genera a la semana: ${maxTotal:,}")


lstTotalesDia = lstTotalesDiaxSem(matVentas, lstPrecios)
maxDia = max(lstTotalesDia)
diaMax = dias[lstTotalesDia.index(maxDia)]
print(f"El día con mayores ingresos es el {diaMax}: ${maxDia:,}")