import PracticaParcial as func
url_archivo = r"D:\UTN\Utn Ingreso\Prog\python_prog_I\data_stark (1).json"

def menu_principal():
    while(True):
        func.imprimir_menu()
        respuesta = input("ingrese opcion > ")
        respuesta_validada = func.validar_respuesta(respuesta)

        if(respuesta_validada == False):continue
        lista_ordenada = []
        lista_original = func.import_json(url_archivo)
        if(respuesta_validada == 1):
            respuesta_heroe = input("ingrese cantidad de heroes > ")
            respuesta_validada = func.validar_respuesta(respuesta_heroe)
            lista_ordenada = func.listar_personajes(lista_original,respuesta_validada)
            print(lista_ordenada)
        elif(respuesta_validada == 2):
            pass

menu_principal()