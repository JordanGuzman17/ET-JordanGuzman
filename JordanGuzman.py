s = "*"*5

productos = {
    '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
    '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
    'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
    'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
    'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
    '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
    '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
    'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']
    }

#stock = {modelo: [precio, stock], ...]
inventario = { 
         '8475HD': [387990,10], 
         '2175HD': [327990,4], 
         'JjfFHD': [424990,1],
         'fgdxFHD': [664990,21], 
         '123FHD': [290890,32], 
         '342FHD': [444990,7],
         'GF75HD': [749990,2],
         'UWU131HD': [349990,1],
         'FS1230HD': [249990,0]
        }

def stock_marca(marca):
    marca= marca.lower()
    total = 0
    for modelo in productos:
        if productos[modelo][0].lower() == marca:
            total += inventario[modelo][1]
    print("\n*******************************************************************")
    print(f"El stock total del modelo es de :", marca.capitalize(), ":", total)
    print("*******************************************************************")

def busqueda_precio():
    while True:
        try:
            p_min = int(input("Ingrese precio minino\n→ $ "))
            p_max = int(input("Ingrese el precio maximo\n→ $"))
            break
        except ValueError:
            print("Solo se puede ingresar numeros")
    resultados = []
    for modelo in inventario:
        precio, stock = inventario[modelo]
        if p_min <= precio <= p_max and stock > 0:
           marca = productos[modelo][0]
           resultados.append(f"\n{marca} -- {modelo}")
    if resultados:
        print("\n*********************")
        print("Productos Encontrados")
        print("*********************")
        for z in resultados:
            print(z)
    else:
        print("\nNo Existen productos en el rango😢")

def actualizar_precio(modelo, nuevo_precio):
    if modelo in inventario:
        inventario[modelo][0] = nuevo_precio
        return True
    return False

while True:
    try:
        print("\n~~~~~~~~~~~~~~~~~~~~~~")
        print(f"{s}Menu Pybooks{s}")
        print("~~~~~~~~~~~~~~~~~~~~~~")
        print(f"\n1)Stock marca.\n2)Búsqueda por precio.\n3)Actualizar precio.\n4)Salir.")

        opc = int(input(f"\n{s}Ingrese una opciona del 1 al 4{s}\n→"))

        if opc == 1:
            marca = input("\nIngrese la marca\n→")
            stock_marca(marca)
        elif opc == 2:
            busqueda_precio()
        elif opc == 3:
            while True:
                try:
                    modelo = input("\nIngrese el modelo a actualizar🫣\n→").upper()
                    nuevo_precio = int(input("\nIngrese el nuevo precio\n💵→"))
                    if actualizar_precio(modelo,nuevo_precio):
                        print(f"\n✔️{s}El precio se ha actualizado correctamente!!!{s}✔️")
                    else:
                        print("\nEl modelo ingresado no existe✖️")
                    try:
                        seguir = int(input("\n¿Deseas actualizar otro modelo? \n1)Si.\n2)No"))
                        if seguir == 1:
                            continue
                        elif seguir == 2:
                            break
                        else:
                            print("Solo se puede ingresar la opcion 1(Si) o 2(No)")
                    except ValueError:
                        print("Error: Solo se puede ingresar numeros❌")
                except ValueError:
                    print("Error:Solo se acetan numeros, vuelva a ingresar❌")
        elif opc == 4:
            print("\n!!!!!!!!!!!!!!!!!!!!")
            print("Programa Finalizado")
            print("!!!!!!!!!!!!!!!!!!!!!👋")

            break
        else:
            print("\nError❌Solo se pueden ingresar un opcion del 1 - 4❌")
    except ValueError:
        print("\nError❌En este menu solo se aceptan numero❌")

