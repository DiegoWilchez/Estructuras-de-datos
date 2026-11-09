
inventario = []


def mostrar_inventario():
    if len(inventario) == 0:
        print("El inventario está vacío.")
    else:
        print("Inventario actual:")
        for i in range(len(inventario)):
            print(f"  {i + 1}. {inventario[i]}")


def agregar_producto():
    nombre = input("Nombre del producto: ").strip()
    if nombre == "":
        print("El nombre no puede estar vacío.")
    else:
        inventario.append(nombre)
        print(f"Producto '{nombre}' agregado.")


def agregar_lote():
    
    lote = []
    cantidad = int(input("¿Cuántos productos tiene el lote? "))
    for i in range(cantidad):
        nombre = input(f"Producto {i + 1} del lote: ").strip()
        if nombre != "":
            lote.append(nombre)
    inventario.extend(lote)
    print(f"Se agregó un lote de {len(lote)} productos: {lote}")


def eliminar_producto():
    if len(inventario) == 0:
        print("El inventario está vacío.")
        return
    mostrar_inventario()
    nombre = input("Nombre del producto a eliminar: ").strip()
    if nombre in inventario:
        inventario.remove(nombre)
        print(f"Producto '{nombre}' eliminado.")
    else:
        print("Ese producto no está en el inventario.")


def eliminar_mas_reciente():
    if len(inventario) == 0:
        print("El inventario está vacío.")
    else:
        eliminado = inventario.pop()
        print(f"Se eliminó el producto más reciente: '{eliminado}'.")


def ordenar_alfabeticamente():
    if len(inventario) == 0:
        print("El inventario está vacío.")
    else:
        inventario.sort()
        print("Productos ordenados alfabéticamente.")
        mostrar_inventario()


def mostrar_total():
    print(f"Número total de productos: {len(inventario)}")


opcion = ""
while opcion != "7":
    print("\nMENÚ")
    print("1. Agregar producto")
    print("2. Agregar lote de productos")
    print("3. Eliminar producto del inventario")
    print("4. Eliminar el producto más reciente")
    print("5. Ordenar productos alfabéticamente")
    print("6. Mostrar número total de productos")
    print("7. Salir")
    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        agregar_lote()
    elif opcion == "3":
        eliminar_producto()
    elif opcion == "4":
        eliminar_mas_reciente()
    elif opcion == "5":
        ordenar_alfabeticamente()
    elif opcion == "6":
        mostrar_total()
    elif opcion == "7":
        print("Saliendo del programa. ¡Hasta pronto!")
    else:
        print("Opción no válida. Intente de nuevo.")