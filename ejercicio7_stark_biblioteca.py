from calendar import c
from pickle import FALSE
from sys import float_repr_style
from data_stark import lista_personajes
'''
{
    "nombre": "Groot",
    "identidad": "Groot",
    "empresa": "Marvel Comics",
    "altura": "701.12",
    "peso": "4.8200000000000003",
    "genero": "M",
    "color_ojos": "Yellow",
    "color_pelo": "",
    "fuerza": "85",
    "inteligencia": "good"
  },
'''
#0)Crear la función 'stark_normalizar_datos' la cual recibirá por parámetro la lista de héroes. La función deberá:

def star_normalizar_datos(lista:list, clave:str) ->dict:
    '''
    recorro la listas y convierto al tipo de dato correcto el valor de las claves, teniendo en cuneta que sea numerica

    recibe como parametro las Lista a recorrer y la clave 

    Retorna un mensaje si algun dato fue normalizdo o error.
    
    '''
    
    retorno = print("Error. Lista vacia") 
    if (type(lista) == type([]) and len(lista) > 0 and type(clave) == type("")):
        
        for elemento in lista_personajes:
            if(type(elemento[clave]) == type("")):
                if(clave == "altura"):
                   elemento["altura"] = float(elemento["altura"])
                   print("alo")
                elif(clave == "peso"):
                    elemento["peso"] = float(elemento["peso"])
                elif(clave == "fuerza" ):
                   elemento["fuerza"] = int(elemento["fuerza"])
    
        retorno = print("Datos normalizados")
    
    return retorno


#Crear la función 'obtener_nombre' la cual recibirá por parámetro un diccionario el cual representara a un 
# héroe y devolverá un string el cual contenga su nombre formateado de la siguiente manera: 


def obtener_nombre(dictionary:dict) ->str:
    '''
    Recibe por parametro un diccionario que represente a un heroe y devuelve el nombre del heroe con un formato:
        Formato:
        Nombre: Howard the Duck
    
    '''
    retorno = False

    if(type(dictionary) == type({}) and len(dictionary) > 0):
        print("Nombre: {0}".format(dictionary["nombre"]))
        retorno = True
       
    return retorno


#Crear la función 'imprimir_dato' la cual recibirá por parámetro un string y 
# deberá imprimirlo en la consola. La función no tendrá retorno.

def imprimir_dato(dato:str):
    '''
    imprime el dato que le pasas literalmente
    '''
    print(dato)

#Crear la función 'stark_imprimir_nombres_heroes' la cual recibirá por parámetro la lista de héroes y 
# deberá imprimirla en la consola. 
# Reutilizar las funciones hechas en los puntos 1.1 y 1.2. Validar que la lista no esté vacía 
def stark_imprimir_nombres_heroes(lista:list):

    '''
    recibe la lista e imprime en consola solo los nombres de la lista
    tambien valida(por si es necesario despues)

    '''
    retorno = False
    if(type(lista) == type([]) and len(lista) > 0):
        for heroes in lista:
            imprimir_dato(heroes["nombre"])
            retorno = True
    
    return retorno

#Crear la función 'obtener_nombre_y_dato' la misma recibirá por parámetro un diccionario el
#  cual representara a un héroe y una key (string) la cual representará el dato que se desea obtener. 

def obtener_nombre_y_dato(dictionary:dict, key:str)-> str:
    '''
    recibe el diccionario, que representara al heroe y tambien una key para imprimir el dato del heroe necesitado


    El string resultante debe estar formateado de la siguiente manera: (suponiendo que la key es fuerza)
    Nombre: Venom | fuerza: 500
    
    '''

    star_normalizar_datos(lista_personajes)




#star_normalizar_datos(lista_personajes, "peso")
#obtener_nombre(lista_personajes[5])
#imprimir_dato("alo")
#stark_imprimir_nombres_heroes(lista_personajes)



#print(lista_personajes)