productos = []

def añadir_producto():
    print("Nombre:")
    name = input()
    while True:
        print("Precio:")
        price = input()
    
        if price.isdecimal():
            price = int(price)
            break
        else:
            print('Por favor, introduzca una cantidad válida en números')
            continue
    print("Cantidad:")
    while True:
        qty = input()
        if qty.isdecimal():
            qty = int(qty)
            break
        else:
            print('Por favor, introduzca una cantidad válida en números')
            continue
    post = f'{len(productos)} Nombre: {name} Precio: {price} Cantidad: {qty}'
    productos.append(f"{post}")
    print(f'Producto añadido. Lista actualizada: {productos}')
    pass

def ver_productos():
    if len(productos) >= 1:
        print('Productos hasta el momento:')
        print(productos)
    else:
        print("No hay productos hasta el momento.")
    pass

def actualizar_producto():
    print("Elija el número del producto que quiere actualizar.")
    while True:
        if len(productos)<1:
            print("No se puede actualizar, porque la lista no tiene productos.")
            break
        else:
            print(f'{productos}')
            point = int(input())
            if point<0 or point>len(productos):
                print("Elija una opción válida.")
                continue
            else:
                print("Nombre:")
                name = input()
                while True:
                    print("Precio:")
                    price = input()
                
                    if price.isdecimal():
                        price = int(price)
                        break
                    else:
                        print('Por favor, introduzca una cantidad válida en números')
                        continue
                print("Cantidad:")
                while True:
                    qty = input()
                    if qty.isdecimal():
                        qty = int(qty)
                        break
                    else:
                        print('Por favor, introduzca una cantidad válida en números')
                        continue
                post = f'{point} Nombre: {name} Precio: {price} Cantidad: {qty}'
                productos[point]=f'{post}'
                print(f'Producto añadido. Lista actualizada: {productos}')
                break
    pass

def eliminar_producto():
    print("Elija el número del producto que quiere eliminar.")
    while True:
        if len(productos)<1:
            print("No se puede eliminar, porque la lista no tiene productos.")
            break
        else:
            print(f'{productos}')
            point = int(input())
            if point<0 or point>len(productos):
                print("Elija una opción válida.")
                continue
            else:
                del productos[point]
                print(f"Producto eliminado. Lista actualizada: {productos}")
                for index, producto in enumerate(productos, start=0):
                    post = f'{index} ' + ' '.join(producto.split()[1:])
                    productos[index] = post
            break
    pass

def guardar_datos():
    file_pc = open("productos.txt", 'w')
    for producto in productos:
        file_pc.write(f'{producto}\n')
    file_pc.close()
    print('Los datos fueron guardados')
    pass

def cargar_datos():
    read_file = open(f"productos.txt", "r")
    new_data = read_file.readlines()
    read_file.close()
    if len(new_data)>0:
        productos.extend([line.strip() for line in new_data])
    else:
        pass
    pass

def menu():
    while True:
        print("1: Añadir producto")
        print("2: Ver productos")
        print("3: Actualizar producto")
        print("4: Eliminar producto")
        print("5: Guardar datos y salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            añadir_producto()
        elif opcion == '2':
            ver_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            guardar_datos()
            break
        else:
            print("Por favor, selecciona una opción válida.")

cargar_datos()
menu()