operador = input("Ingrese su nombre: ").strip()

# Validación del nombre del operador
while operador == "" or not operador.isalpha():
    print("Error. Ingrese un nombre válido.")
    operador = input("Ingrese nombre: ").strip()

# Variables para guardar turnos
lunes_1 = ""
lunes_2 = ""
lunes_3 = ""
lunes_4 = ""
martes_1 = ""
martes_2 = ""
martes_3 = ""

# Menú repetitivo
while True:
    print("Menú: \n1. Reservar turno\n2. Cancelar turno\n3. Agenda\n4. Resumen\n5.Cerrar sistema\n")
    opcion = input("Opción: ").strip()

# Validación de la opción.
    if not opcion.isdigit():
        print("Error. Ingrese un número del 1 al 5.")
        continue
        
    opcion = int(opcion)

    match opcion:
        case 1: 
            # Reserva de turno
            while True:
                dia = input("Elija el día: \n1. Lunes\n2. Martes\n3. Volver al menú anterior\n").strip()

                # Validación de día
                while not dia.isdigit() or int(dia) == 0 or int(dia) > 3:
                    print("Error. Ingrese una opción válida.")
                    dia = input("Elija el día: \n1. Lunes\n2. Martes\n3. Volver al menú anterior\n").strip()
                
                dia = int(dia)

                match dia:
                    case 1:
                        if lunes_1 != "" and lunes_2 != "" and lunes_3 != "" and lunes_4 != "":
                            print("No hay turnos disponibles.")
                        else:
                            # Ingreso nombre de paciente y validación
                            nombre_paciente = input("Ingrese nombre del paciente: ").strip()

                            while nombre_paciente == "" or not nombre_paciente.isalpha():
                                print("Error. Ingrese un nombre válido.")
                                nombre_paciente = input("Ingrese nombre del paciente: ").strip()
                            
                            # Verificar si ya existe el nombre en el turno.
                            if nombre_paciente == lunes_1 or nombre_paciente == lunes_2 or nombre_paciente == lunes_3 or nombre_paciente == lunes_4:
                                print("El paciente ya tiene turno reservado.")
                            else:
                            # Asigno turno en el primer espacio libre
                                if lunes_1 == "":
                                    lunes_1 = nombre_paciente
                                elif lunes_2 == "":
                                    lunes_2 = nombre_paciente
                                elif lunes_3 == "":
                                    lunes_3 = nombre_paciente
                                elif lunes_4 == "":
                                    lunes_4 = nombre_paciente
                                print("Turno confirmado.")
                    case 2:
                        if martes_1 != "" and martes_2 != "" and martes_3 != "":
                            print("No hay turnos disponibles.")
                        else: 
                            # Ingreso nombre de paciente y validación
                            nombre_paciente = input("Ingrese nombre del paciente: ").strip()

                            while nombre_paciente == "" or not nombre_paciente.isalpha():
                                print("Error. Ingrese un nombre válido.")
                                nombre_paciente = input("Ingrese nombre del paciente: ").strip()
                            
                            # Verificar si ya existe el nombre en el turno.
                            if nombre_paciente == martes_1 or nombre_paciente == martes_2 or nombre_paciente == martes_3:
                                print("El paciente ya tiene turno reservado.")
                            else:
                                # Asigno turno en el primer espacio libre
                                if martes_1 == "":
                                    martes_1 = nombre_paciente
                                elif martes_2 == "":
                                    martes_2 = nombre_paciente
                                elif martes_3 == "":
                                    martes_3 = nombre_paciente
                                print("Turno confirmado.")
                    case 3:
                        print("Menú anterior")
                        break

        case 2: # Cancelación de turno
            while True:
                dia = input("Elija el día: \n1. Lunes\n2. Martes\n3. Volver al menú anterior\n").strip()
                # Validación de día
                while not dia.isdigit():
                    print("Error. Ingrese una opción válida.")
                    dia = input("Elija el día: \n1. Lunes\n2. Martes\n3. Volver al menú anterior\n").strip()
                
                dia = int(dia)

                if dia == 3:
                    print("Volviendo al menú anterior")
                    break

                nombre_paciente = input("Ingrese nombre del paciente: ").strip()

                while nombre_paciente == "" or not nombre_paciente.isalpha():
                    print("Error. Ingrese un nombre válido.")
                    nombre_paciente = input("Ingrese nombre del paciente: ").strip()

                match dia:
                    case 1:
                        if nombre_paciente == lunes_1:
                            lunes_1 = ""
                            print("Turno cancelado")
                        elif nombre_paciente == lunes_2:
                            lunes_2 = ""
                            print("Turno cancelado")
                        elif nombre_paciente == lunes_3:
                            lunes_3 = ""
                            print("Turno cancelado")
                        elif nombre_paciente == lunes_4:
                            lunes_4 = ""
                            print("Turno cancelado")
                        else:
                            print("El paciente no tiene turno reservado.")
                    case 2:
                        if nombre_paciente == martes_1:
                            martes_1 = ""
                            print("Turno cancelado")
                        elif nombre_paciente == martes_2:
                            martes_2 = ""
                            print("Turno cancelado")
                        elif nombre_paciente == martes_3:
                            martes_3 = ""
                            print("Turno cancelado")
                        else:
                            print("El paciente no tiene turno reservado.")
        case 3: # Agenda del día

            dia = input("Elija el día: \n1. Lunes\n2. Martes\n").strip()

            while not dia.isdigit() or int(dia) == 0 or int(dia) > 3:
                print("Error. Ingrese una opción válida.")
                dia = input("Elija el día: \n1. Lunes\n2. Martes\n").strip()

            dia = int(dia)

            if dia == 1:
                print ("=== Agenda del día ===")
                if lunes_1 == "":
                    print("Libre")
                else:
                    print(f"Turno 1: {lunes_1}")
                if lunes_2 == "":
                    print("Libre")
                else:
                    print(f"Turno 2: {lunes_2}")
                if lunes_3 == "":
                    print("Libre")
                else: 
                    print(f"Turno 3: {lunes_3}")
                if lunes_4 == "":
                    print("Libre")
                else:
                    print(f"Turno 4: {lunes_4}")
            elif dia == 2:
                print ("=== Agenda del día ===")
                if martes_1 == "":
                    print("Libre")
                else:
                    print(f"Turno 1: {martes_1}")
                if martes_2 == "":
                    print("Libre")
                else:
                    print(f"Turno 2: {martes_2}")
                if martes_3 == "":
                    print("Libre")
                else: 
                    print(f"Turno 3: {martes_3}")
               
        case 4: # Resumen de la semana
            print ("=== RESUMEN GENERAL ===")
            if lunes_1 == "":
                print("Libre")
            else:
                print(f"Turno 1: {lunes_1}")
            if lunes_2 == "":
                print("Libre")
            else:
                print(f"Turno 2: {lunes_2}")
            if lunes_3 == "":
                print("Libre")
            else: 
                print(f"Turno 3: {lunes_3}")
            if lunes_4 == "":
                print("Libre")
            else:
                print(f"Turno 4: {lunes_4}")
            if martes_1 == "":
                print("Libre")
            else:
                print(f"Turno 1: {martes_1}")
            if martes_2 == "":
                print("Libre")
            else:
                print(f"Turno 2: {martes_2}")
            if martes_3 == "":
                print("Libre")
            else: 
                print(f"Turno 3: {martes_3}")
            
            # Falta días con más turnos (o empate)

        case 5: # Salir del sistema
            print("Saliendo del sistema...")
            break
        case _:
            print("Error. Ingrese un número del 1 al 5.")