import PracticaParcial as func

url_archivo = r"D:\UTN\Utn Ingreso\Prog\python_prog_I\data_stark (1).json"

def menu_principal():
    msg = ""
    while(True):
        func.imprimir_menu()
        respuesta = input("ingrese opcion (0 para salir) > ")
        respuesta_validada = func.validar_respuesta(respuesta)

        if(respuesta_validada == 0):break
        elif(respuesta_validada == False):continue
        
        lista_original = func.import_json(url_archivo)
        if(respuesta_validada == 1):
            respuesta_heroe = input("ingrese cantidad de heroes > ")
            respuesta_validada = func.validar_respuesta(respuesta_heroe)
            if(respuesta_validada != False):
                max_lista = len(lista_original)
                if(respuesta_validada < max_lista):
                    msg = func.fun_mostrar_cantidad_especifica(lista_original[:respuesta_validada])
                else:
                    print("limite excedido")
                    continue
            else:
                print("error")
                continue
        elif(respuesta_validada == 2):
            respuesta_asc_desc = input("Altura ascendente o descendente?(asc/desc) > ")
            respuesta_validada = func.validar_RegEx(respuesta_asc_desc, "asc|desc")
            if(respuesta_validada != False):
                msg = func.fun_mostrar(func.ordenar_por_altura(lista_original,respuesta_validada))
            else:
                print("Error")
                continue

        elif(respuesta_validada == 3):
            respuesta_asc_desc = input("Fuerza ascendente o descendente?(asc/desc) > ")
            respuesta_validada = func.validar_RegEx(respuesta_asc_desc, "asc|desc")
            if(respuesta_validada != False):
                msg = func.fun_mostrar(func.listar_por_fuerza(lista_original,respuesta_asc_desc),"fuerza")
            else:
                print("Error")
                continue

        elif(respuesta_validada == 4):
            respuesta_menor_mayor = input("Quiere los menores al promedio o los mayores? (menor\mayor) > ")
            respuesta_validada_menor_mayor= func.validar_RegEx(respuesta_menor_mayor, "menor|mayor")
            respuesta_key = input("que tipo de promedio quiere (altura/fuerza/peso)")
            respuesta_validada_key = func.validar_RegEx(respuesta_key,"altura|fuerza|peso")
            if(respuesta_validada != False and respuesta_validada_key != False and respuesta_menor_mayor!=False):
                msg = func.fun_mostrar(func.calcular_promedio_key_numerica(lista_original,respuesta_key ,respuesta_menor_mayor),respuesta_key)
            else:
                print("Error")
                continue

        elif(respuesta_validada == 5):
            respuesta_tipo = input("Ingrese tipo de inteligencia (good/average/high)")
            
            print(func.fun_mostrar(func.buscar_por_inteligencia(lista_original,respuesta_tipo),"inteligencia"))
            
        elif(respuesta_validada == 6):
            nombre_archivo = input("ingrese nombre archivo > ")
            nombre_archivo_validado = func.validar_RegEx(nombre_archivo,"[a-z]+")
            if(nombre_archivo_validado != False):
                func.exportar_CSV(msg,nombre_archivo_validado)
            else:
                print("Error")
                continue
            
menu_principal()