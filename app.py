import random
import csv

regis_consumidores = []
consumidores = {
                "codigo": "",
                "nombre": "",
                "edad": "",
                "equipo": "",
                "consum_vier": "",
                "consum_saba": "",
                "consum_dom": ""
            }
            

def menu():
    print("--- MENU ---")
    print("1. Registrar consumo\n2. Listar los todos los consumos\n3. Imprimir hoja consumo\n4. Buscar un consumo por ID\n5. Salir del programa")
    try:
        opc = int(input("Ingrese la opcion: "))
        if opc == 1:           
            print("--- Registro de consumo ---")
            while True:
                nomb = input("Ingrese el Nombre: ")
                if nomb != "":
                    consumidores["nombre"] = nomb
                    consumidores["codigo"]= random.randint(100000, 999999)

                    edad = int(input("Ingrese la edad: "))
                    if edad != "":
                        consumidores["edad"] = edad
                        equipo = input("El equipo que pertenece: ")
                        if equipo != "":
                            consumidores["equipo"] = equipo
                            while True:
                                consumo_cafe_v = int(input("Consumo de cafe el viernes: "))
                                consumo_cafe_s = int(input("Consumo de cafe el Sabado: "))
                                consumo_cafe_d = int(input("Consumo de cafe el domingo: "))
                                consumo_total = consumo_cafe_v + consumo_cafe_s + consumo_cafe_d
                                if consumo_total < 3:
                                    print("--- El sonsumo total de los 3 dias debe ser minimo 3 ---")
                                elif consumo_total >= 3:
                                    consumidores["consum_vier"] = consumo_cafe_v
                                    consumidores["consum_saba"] = consumo_cafe_s
                                    consumidores["consum_dom"] = consumo_cafe_d
                                    regis_consumidores.append(consumidores)
                                    menu()
                                    break
                        else: 
                            break
                    else: 
                        break
                else: 
                    break
        elif opc == 2:
            print("--- Lista de consumos ---")
            print("ID Consumo   Jugador Edad    Equipo  Viernes Sabado  Domingo")
            #for a in regis_consumidores:
            print(regis_consumidores)
            #print(f"{regis_consumidores["codigo"]}")
            #print(f"{consumidores["codigo"]} {consumidores["nombre"]} {consumidores["edad"]} {consumidores["equipo"]} {consumidores["consum_vier"]} {consumidores["consum_saba"]} {consumidores["consum_dom"]}")
                #print(f"{i[consumidores["codigo"]]} {i[consumidores["nombre"]]} {i[consumidores["edad"]]} {i[consumidores["equipo"]]} {i[consumidores["consum_vier"]]} {i[consumidores["consum_saba"]]} {i[consumidores["consum_dom"]]}")
        elif opc == 3:
            print("--- Equipo ---")
            equip = input("1.- Los Genios de la garrafa\n2.- Los Compiladores Despiertos\n3.- Código Borracho\n4.- Los programadores perezosos\n5.- Ctrl+Alt+Derrota\n")
            if equip == 1:
                with open("hoja_consumo.csv" "w") as archivo:
                    archivo.write(regis_consumidores)
        elif opc == 4:
            print()
        elif opc == 5:
            print()
        else:
            menu()
    except:
            menu()

menu()