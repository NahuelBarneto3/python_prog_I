from subprocess import IDLE_PRIORITY_CLASS
from data_stark import lista_personajes
import re

'''
 {
   "nombre": "Howard the Duck",
   "identidad": "Howard (Last name unrevealed)",
   "empresa": "Marvel Comics",
   "altura": "79.349999999999994",
   "peso": "18.449999999999999",
   "genero": "M",
   "color_ojos": "Brown",
   "color_pelo": "Yellow",
   "fuerza": "2",
   "inteligencia": "average"
 },
'''

 #1.1) Crear la función ‘extraer_iniciales’ que recibirá como parámetro:

def extraer_iniciales(nombre_heroe:str)->str:
    '''
    extrae iniciales de un nombre str

    recibe un strig como parametro

    si el string contiene "the" se omite si contiene guion pone espacio

    retorna N/A en caso de str vacio

    '''

    retorno = "N/A"

    if(len(nombre_heroe) > 0 ):
        if(nombre_heroe.count("the") > 0):
            nombre_heroe = nombre_heroe.replace("the ","")

        if(nombre_heroe.count("-")):
            nombre_heroe = nombre_heroe.replace("-"," ")

        lista1 = nombre_heroe.split(" ")

        inicial = "" #se pueden acumular strings wtf, para luego concatenarlos
        for palabra in lista1:
            inicial += palabra[0] + "."

        return inicial

#1.2) Crear la función ‘definir_iniciales_nombre’ la cual recibirá como parámetro:

def definir_iniciales_nombre(heroe:dict)->bool:

    '''
        recibe heroe: un diccionario con los datos del personaje
        deberá agregar una nueva clave al diccionario
        recibido como parámetro. La clave se deberá llamar ‘iniciales’ y su valor será el
        obtenido de llamar a la función ‘extraer_iniciales’

        valida que el tipo sea dic
        que contenga la clave "nombre"

        En caso de encontrar algún error retornar False, caso contrario retornar True

    '''

    retorno = False
    if(type(heroe) == type({})):
        for clave in heroe:
            if(clave.count("nombre") > 0):
                inicial = extraer_iniciales(heroe["nombre"])
                heroe["inicial"] = inicial
                retorno = True
                break



    return retorno

#1.3) Crear la función ‘agregar_iniciales_nombre’ la cual recibirá como parámetro:

def agregar_iniciales_nombre(lista_heroes:list)->bool:
    '''
        recibe lista_heroes: lista de personajes

        valida  Que lista_heroes sea del tipo lista
                Que la lista contenga al menos un elemento

        La función itera lista_heroes pasándole cada héroe a la función definir_iniciales_nombre.

        En caso que retorne False entonces detiene la
        iteración e informa por pantalla:
        ‘El origen de datos no contiene el formato correcto’

        La función deberá devolver True en caso de haber
        finalizado con éxito o False en caso de que haya ocurrido un error

    '''

    retorno = False

    i = 0
    if(type(lista_heroes) == type([]) and len(lista_heroes) > 0):
        for heroe in lista_heroes:
            definir_iniciales_nombre(lista_heroes[i])
            i += 1
        retorno = True

    if retorno == False:
        print("El origen de datos no contiene el formato correcto")
        return retorno
    else:
        return retorno

#1.4) Crear la función ‘stark_imprimir_nombres_con_iniciales’  la cual recibirá como parámetro:
def stark_imprimir_nombres_con_iniciales(lista_heroes:list):

    '''
    Recibe:
        lista_heroes: la lista de personajes

    Utiliza la función agregar_iniciales_nombre para añadirle las iniciales a los diccionarios
    contenidos en la lista_heroes

    Imprime la lista completa de los nombres de los personajes seguido de las iniciales encerradas
    entre paréntesis ()

    Valida:
        Que lista_heroes sea del tipo lista
        Que la lista contenga al menos un elemento

    FORMATO DE SALIDA: Delante de cada nombre '*'
        * Howard the Duck (H.D.)
        * Rocket Raccoon (R.R.)
    '''
    i = 0
    retorno = False
    if (type(lista_heroes) == type([]) and len(lista_heroes) > 0):

        for i in range(len(lista_heroes)):
            if (definir_iniciales_nombre(lista_heroes[i]) == True):
               print("* {0} ({1})".format(lista_heroes[i]["nombre"], lista_heroes[i]["inicial"]))


    return retorno


#2.1) Crear la función ‘generar_codigo_heroe’ la cual recibirá como parámetros

def generar_codigo_heroe(id_heroe:int, genero_heroe:str)-> str:

    '''
    RECIBE:
        id_heroe: un entero que representa el identificador del héroe.
        genero_heroe: un string que representa el género del héroe ( puede tomar los valores "M",  "F" o "NB")

    La función deberá generar un string
    FORMATO:
        GENERO-000…000ID

    Es decir, el género recibido por parámetro seguido de un "-" (guión) y por último el identificador recibido.
    Todos los códigos generados deben tener como máximo 10 caracteres (contando todos los caracteres, inclusive el guión).
    Se deberá completar con ceros para que todos queden del mismo largo

    '''

    if(type(id_heroe) == type(0) and (genero_heroe == "F" or genero_heroe == "NB" or genero_heroe == "M")):

        id_heroe = str(id_heroe)
        id_heroe_final =  "{0}-{1}".format(genero_heroe,id_heroe.zfill(10))

    return id_heroe_final



#2.2) Crear la función ‘agregar_codigo_heroe’ la cual recibirá como parámetro:
def agregar_codigo_heroe(heroe:dict,id_heroe:int)->bool:

    '''
        RECIBE:
            heroe: un diccionario con los datos del personaje
            id_heroe: un entero que representa el identificador del héroe.

        Agrega una nueva clave llamada "codigo_heroe" al diccionario "heroe" recibido como parámetro
        y le asigna como valor un código utilizando la función "generar_codigo_heroe"

        VALIDA:
            Que el diccionario recibido como parámetro no se encuentre vacío.
            Que el código recibido mediante generar_codigo_heroe tenga exactamente 10 caracteres

        La función deberá retornar True o False en caso de encontrarse o no un error

    '''

    retorno = False

    if(len(heroe) > 0):
        heroe["id_heroe"] = generar_codigo_heroe(id_heroe, heroe["genero"])
        retorno = True

    return retorno




#2.3) Crear la función ‘stark_generar_codigos_heroes’  la cual recibirá como parámetro:

def stark_generar_codigos_heroes(lista_heroes:list):
    '''
    RECIBE:
        lista_heroes: la lista de personajes

    VALIDA:
        La lista contenga al menos un elemento
        Todos los elementos de la lista sean del tipo diccionario
        Todos los elementos contengan la clave "genero"

    La función itera la lista de personajes y agrega el código a cada uno de los personajes.

    Imprime por pantalla con el siguiente formato

    FORMATO:
        Se asignaron ## códigos

        * El código del primer héroe es:    M-00000001
        * El código del del último héroe es: 	M-00001224
    '''

    retorno = False
    contador_heroes = 0
    lista_id_heroe = []

    if(len(lista_heroes) > 0):
        for i in range(len(lista_heroes)):
            if(type(lista_heroes[i]) == type({}) and "genero" in lista_heroes[i]):
                agregar_codigo_heroe(lista_heroes[i],i+1)
                contador_heroes += 1

        print("Se le asignaron {0} codigos \n\
            *El codigo del primer heroe es:     {1}\n\
            *El codigo del ultimo heroe es:     {2}\n\
            ".format(contador_heroes, lista_heroes[0]["id_heroe"],lista_heroes[len(lista_heroes)-1]["id_heroe"]))



#3.1) Crear la función ‘sanitizar_entero’ la cual recibirá como parámetro:

def sanitizar_entero(numero_str:str)-> int:
    '''
    RECIBE:
        numero_str: un string que representa un posible número entero

    Analiza el string recibido y determina si es un número entero positivo.
    La función debe devolver distintos valores según el problema encontrado:

    RETORNAR:
        Si contiene carácteres no numéricos retornar -1
        Si el número es negativo se deberá retornar un -2
        Si ocurren otros errores que no permiten convertirlo a entero entonces se deberá retornar -3

    Quita los espacios en blanco de atras y adelante del string en caso que los tuviese

    En caso que se verifique que el texto contenido en el string es un número entero positivo,
    lo retorna convertido en entero

    '''
    #Con expresiones regulares

    numero_str_2 = re.findall("[a-z]",numero_str)

    if(len(numero_str_2) == 0):
        numero_str_2 = re.findall("[.]", numero_str)
        if(len(numero_str_2) == 0):
            numero_str = int(numero_str)
            if(type(numero_str) == type(1)):
                if(numero_str > -1 ):
                    return numero_str
                else: return -2
        else: return -3
    else: 
        return -1


    # numero_str = numero_str.strip()

    # if(numero_str.isalnum() == True):
    #     return -1

    # numero_str = int(numero_str)

    # if(numero_str < 0 ):
    #     return -2

    # if()




test = sanitizar_entero("3.152")
print(test)
#stark_generar_codigos_heroes(lista_personajes)
#test = agregar_codigo_heroe(lista_personajes[0],291000)
#print(test)
#generar_codigo_heroe(6544,"F")
#stark_imprimir_nombres_con_iniciales(lista_personajes)



# lista_vacia = []
# true_false = agregar_iniciales_nombre(lista_personajes)
# print(true_false)


# true_false = definir_iniciales_nombre(lista_personajes[0])
# print(true_false)


# iniciales = extraer_iniciales("Thor")
# print(iniciales)