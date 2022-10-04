'''
1 - Listar los personajes ordenados por altura
2 - Mostrar el personaje mas alto de cada genero
3 - 3 - Ordenar los personajes por peso
4 - Armar un buscador de personajes 
5 - Exportar lista personajes a CSV
6 - Salir

'''
import funciones as f
url_archivo = r"D:\UTN\Utn Ingreso\Prog\python_prog_I\Examen\data.json"
def starwars_app():
    lista_personajes = f.cargar_json(url_archivo)
    msg = ""
    while(True):
        print("1 - Listar los personajes ordenados por altura\n2 - Mostrar el personaje mas alto de cada genero\n3 - Ordenar los personajes por peso\n4 - Armar un buscador de personajes\n5 - Exportar lista personajes a CSV\n6 - Salir\n")
        respuesta = input("Ingrese opcion (6 para salir) > ")
        respuesta_validada = f.validar_RegEx(respuesta, "^[0-9]{1}$")
        if(respuesta_validada == False):
            continue
        elif(respuesta_validada=="1"):
            print("1 - Listar los personajes ordenados por altura\n")
            
            if(respuesta_validada != False):
                msg = f.mostrar(f.ordenar_por_altura(lista_personajes),"height")
            else: 
                print("Error")
                continue
        elif(respuesta_validada=="2"):
            print("2 - Mostrar el personaje mas alto de cada genero\n")
            
            if(respuesta_validada != False):
                lista_altura_ordenada = f.ordenar_por_altura(lista_personajes)
                f.mostrar_mas_alto_por_genero(lista_altura_ordenada)
            else: 
                print("Error")
                continue
        elif(respuesta_validada=="3"):
            print("3 - Ordenar los personajes por peso\n")
            if(respuesta_validada != False):
                msg = f.mostrar(f.ordenar_por_peso(lista_personajes),"mass")
            else: 
                print("Error")
                continue
        elif(respuesta_validada=="4"):
            print("4 - Armar un buscador de personajes\n")
        elif(respuesta_validada=="5"):
            print("5 - Exportar lista personajes a CSV\n")
            nombre_archivo = input("ingrese nombre del archivo > ")
            nombre_archivo_validado = f.validar_RegEx(nombre_archivo, "[a-z]+")
            if(nombre_archivo_validado != False ):
                f.export_csv(msg, nombre_archivo_validado)

        elif(respuesta_validada=="6"):
            break


starwars_app()

