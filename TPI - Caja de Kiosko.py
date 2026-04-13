# Ejercicio 1: Simular una compra con validaciones y cálculo de total

nombre_cliente = input("Ingrese nombre: ").strip()

# Corroboro que el usuario ingresa un dato válido

while nombre_cliente == "" or not nombre_cliente.isalpha():
    print("Error. Ingrese un nombre válido.")
    nombre_cliente = input("Ingrese nombre: ").strip()

cantidad_productos = input("Ingrese cantidad: ").strip()

# Verifico primero que la cantidad ingresada sea un dígito y luego si ese dígito es un 0
while not cantidad_productos.isdigit() or int(cantidad_productos) == 0:
    print("Error. Ingrese una cantidad válida: ")
    cantidad_productos = input("Ingrese cantidad: ").strip

# Una vez verificado que el dato ingresado es un número, convierto la variable cantidad_productos en un entero

cantidad_productos = int(cantidad_productos)

# Inicializo variables con y sin descuento

total_sin_descuento = 0
total_con_descuento = 0.0

# Para cada producto, pido precio del mismo.

for i in range(1,cantidad_productos + 1):
    precio_str = input(f"Producto {i} - Precio: ").strip()

    while not precio_str.isdigit() or int(precio_str) == 0:
        print("Error. Ingrese un precio válido")
        precio_str = input(f"Producto {i} - Precio: ").strip()
    
    precio = int(precio_str)

# Preguntar si el producto tiene descuento
    desc = input("Descuento (S/N): ").strip().lower()

# Valido que el dato ingresado es una "s" o una "n". Primero valido si el dato no es una s y luego si no es una n.
    while desc != "s" and desc != "n":
        print("Error. Ingrese S o N")
        desc = input("Descuento (S/N): ").strip().lower()
    
    # Sumatoria de todos los productos luego de ingresado cada precio

    total_sin_descuento += precio

    # Verificar si corresponde descuento

    if desc == "s":
        precio_final = precio * 0.9
    else:
        precio_final = precio
    
    # Sumatoria de productos con y sin descuentos

    total_con_descuento += precio_final

# Cálculo del ahorro y promedio por producto

ahorro = total_sin_descuento - total_con_descuento

promedio = total_con_descuento / cantidad_productos

print(f"Total sin descuento: ${total_sin_descuento}")
print(f"Total con descuento: ${total_con_descuento:.2f}")
print(f"Ahorro total: ${ahorro:.2f}")
print(f"Promedio: ${promedio:.2f}")



