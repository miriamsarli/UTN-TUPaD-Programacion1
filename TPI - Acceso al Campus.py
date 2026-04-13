# Credenciales fijas

usuario_correcto = "alumno"
clave_correcta = "python123"

# Limitación de intento de acceso

intentos_max = 3

# Intentos de ingreso
# Al haber ingresado ya una vez usuario y clave, se lo considera el primer intento
intento = 1
print(f"Intento {intento}/{intentos_max}")
usuario = input("Usuario: ")
clave = input("Clave: ")


while not (usuario == usuario_correcto and clave == clave_correcta) and intento < intentos_max:
    print("Error. Credenciales inválidas.")
    intento += 1
    print(f"Intento {intento}/{intentos_max}")
    usuario = input("Usuario: ")
    clave = input("Clave: ")
    

if usuario == usuario_correcto and clave == clave_correcta:
    print("Acceso concedido.")

    # Menú repetitivo
    while True:
        print("Menú: \n1. Estado\n2. Cambiar clave\n3. Mensaje\n4.Salir\n")
        opcion = input("Opción: ").strip()

         #Validar que la opción ingresada sea un número

        if not opcion.isdigit():
            print("Error. Ingrese un número válido")
            continue
        
        opcion = int(opcion)
    
        # Validar que la opción está dentro del rango:

        if opcion == 1:
            print("Inscripto")
        elif opcion == 2:
            clave_correcta = input("Nueva clave: ")
            confirmar_clave = input("Confirmar nueva clave: ")

            if len(clave_correcta) < 6:
                print("Error. Mínimo 6 caracteres.")            
            elif clave_correcta != confirmar_clave:
                print("Las claves no coinciden")
            else: 
                print("Se cambió la clave existosamente.")

        elif opcion == 3:
            print("Primero resuelve el problema, después escribe el código.")
        elif opcion == 4:
            print("Saliendo del programa...")
            break
        else:
            print("Error. Opción fuera de rango.")
else:
    print("Cuenta bloqueada")