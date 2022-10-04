import re
import json

url_archivo = r"D:\UTN\Utn Ingreso\Prog\python_prog_I\data_stark.json"

def cargar_archivo(url_archivo:str)->list:
    with open(url_archivo) as archivo:
        data = json.load(archivo)

        return data["heroes"]
    
lista_personajes = cargar_archivo(url_archivo)


def imprimir_dato(string:str):

    if(type(string) == type('')):
        print(string)
    else:
        print("error no es un string")

#Crear la funcion 'stark_menu_principal_desafio_5


def imprimir_menu_desafio_5():
        menu = ("\n\
        A -  \n\
        B - \n\
        C -  \n\
        D - \n\
        E - \n\
        F - \n\
        G - \n\
        H - \n\
        I - \n\
        J - \n\
        K - \n\
        L - \n\
        M - \n\
        N - \n\
        O - \n\
        Z - Salir\n \n ")
        
        imprimir_dato(menu)


def stark_menu_principal_desafio_5():
    imprimir_menu_desafio_5()

    respuesta = input("Respuesta > ")


    letra_validada = re.search("[a-oA-OzZ]", respuesta)

    if(letra_validada == None):
        letra_validada = -1
        return letra_validada
    else: return respuesta
  
    
#Crear la función 'stark_marvel_app_5'

def stark_marvel_app_5(lista_heroes: list):
   

    while (True):
        respuesta = stark_menu_principal_desafio_5()
        if(respuesta != -1):
            respuesta.lower()
        else:
            print("error opcion incorrecta")
            continue

        if (respuesta == "a"):
            print(respuesta)
        elif(respuesta == "b"):
            print(respuesta) 
        elif(respuesta == "c"):
            print(respuesta)
        elif(respuesta == "d"):
            print(respuesta)
        elif(respuesta == "e"):
            print(respuesta) 
        elif(respuesta == "f"):
            print(respuesta)
        elif(respuesta == "g"):
            print(respuesta)
        elif(respuesta == "h"):
            print(respuesta)
        elif(respuesta == "i"):
            print(respuesta)
        elif(respuesta == "j"):
            print(respuesta)
        elif(respuesta == "k"):
            print(respuesta)
        elif(respuesta == "l"):
            print(respuesta)
        elif(respuesta == "m"):
            print(respuesta)
        elif(respuesta == "n"):
            print(respuesta)
        elif(respuesta == "o"):
            print(respuesta)
        elif(respuesta == "z"):
            break

#Crear la función 'leer_archivo' 

def leer_archivo(archivo:str):
    with open(archivo, "r") as archivo:
        data = json.load(archivo)

    print("a")
    return data

#Crear la función 'guardar_archivo'

def guardar_archivo(nombre_tipo_archivo:str,cont_a_guardar:str)->bool:
    
    with open(nombre_tipo_archivo, "w+") as archivo:
        archivo.writelines(cont_a_guardar)
        print("el archivo" + nombre_tipo_archivo + "se creo correctamente")
    
    return
    

test = guardar_archivo("archivo_nuevo.csv", "hola que tal/n como andas")
print(test)
# test = leer_archivo(url_archivo)
# print(test)

#stark_marvel_app_5(lista_personajes)

# test = stark_menu_principal_desafio_5()
# print(test)

#imprimir_menu_desafio_5()