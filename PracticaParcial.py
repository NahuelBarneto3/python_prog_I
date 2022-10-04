import json
import re
from tkinter.messagebox import NO
from xml.dom import registerDOMImplementation
'''
 {
            "nombre": "Howard the Duck",
            "identidad": "Howard (Last name unrevealed)",
            "altura": 79.35,
            "peso": 18.45,
            "fuerza": 2,
            "inteligencia": ""
        },
'''
def validar_RegEx(a_validar:str, patron_valicion):

    respuesta_validada = re.search(patron_valicion, a_validar, re.IGNORECASE)
    if( respuesta_validada != None):
        a_validar = a_validar.lower()
        a_validar = a_validar.replace(" ","")
        return a_validar
    else: return False


def import_json(url_archivo:str)-> list:
   
    with open(url_archivo) as archivo:
        data = json.load(archivo)

        return data["heroes"]
    
#lista_personajes = import_json(url_archivo)
# print(lista_personajes)
# print(type(lista_personajes))

def validar_respuesta(numero:str)-> bool|int:

    respuesta_validada = re.match("^[0-9]+$", numero)
    if( respuesta_validada != None):
        numero_int = int(numero)
        return numero_int
    else: return False    
#1) Listar los primeros N héroes. El valor de N será ingresado por el usuario  (Validar que no supere max. de lista)
'''
def listar_personajes(lista_recibida:list, valor_a_recorrer:int)->list:
    
    lista la cantidad de heroes elegidos por el usuario y los devuelve en lista
    RECIBE:
        -la lista a recorrer
        -Cantidad de heroes a recorrer (INT)

    DEVUELVE: Una Lista

    VALIDA:
        Que el valor recibido no supere len de lista
    
    
    lista_nueva = []
    

    if (type(lista_recibida) == list and len(lista_recibida) > 0 and valor_a_recorrer >0 and valor_a_recorrer <= len(lista_recibida)):
        i=0
        
        for heroe in lista_recibida:
            lista_nueva.append(heroe["nombre"])
            i += 1 
            if (i == valor_a_recorrer): break
    

    if(len(lista_nueva) > 0):
        return lista_nueva
    else: return False
'''
# 2) Ordenar y Listar héroes por altura. Preguntar al usuario si lo quiere ordenar de manera ascendente (‘asc’) o descendente (‘desc’)
def qsort_asc(lista_a_ordenar:list, key:str)->list:
    lista_recibida = lista_a_ordenar[:]
    lista_der = []
    lista_izq = []
    
    if(len(lista_a_ordenar) <= 1):
        return lista_a_ordenar
    else:
        pivot = lista_recibida[0]
        for elemento in lista_recibida[1:]:
            if (elemento[key] > pivot[key]):
                lista_der.append(elemento)
            else:
                lista_izq.append(elemento)

    lista_izq = qsort_asc(lista_izq, key)
    lista_izq.append(pivot)
    lista_der = qsort_asc(lista_der, key)

    return lista_izq + lista_der

# test = qsort_asc(lista_personajes, "altura")
# print (test)

def qsort_desc(lista_a_ordenar:list, key:str)->list:
    lista_recibida = lista_a_ordenar[:]
    lista_der = []
    lista_izq = []
    
    if(len(lista_a_ordenar) <= 1):
        return lista_a_ordenar
    else:
        pivot = lista_recibida[0]
        for elemento in lista_recibida[1:]:
            if (elemento[key] < pivot[key]):
                lista_der.append(elemento)
            else:
                lista_izq.append(elemento)
    lista_izq = qsort_desc(lista_izq, key)
    lista_izq.append(pivot)
    lista_der = qsort_desc(lista_der,key)

    return lista_izq + lista_der
# test = qsort_desc(lista_personajes, "altura")
# print (test)

def ordenar_por_altura(lista_recibida:list, forma:str)->list:
    '''
        Devuelve una lista ordenada de manera ascendente o descendente segun indique el usuario segun altura

        RECIBE:
            -Una Lista
            -La forma (asc o desc)
        
        DEVUELVE: Una lista

        VALIDA: Que asc o desc este bien escrito
    
    '''
    retorno = False
    validar_forma = re.search("asc|desc",forma, re.IGNORECASE)
       
    if(type(lista_recibida) == list and len(lista_recibida) > 0 and validar_forma != None):
        copia_lista = lista_recibida.copy()
        lista_nueva = []
        if (re.search("asc",forma,re.IGNORECASE) != None):
            altura_asc = qsort_asc(copia_lista, "altura")
            for i in range(len(altura_asc)):
                #dic_heroes = {} 

                # dic_heroes["nombre"] = altura_asc[i]["nombre"]
                # dic_heroes["altura"] = altura_asc[i]["altura"]
                lista_nueva.append(altura_asc[i])
            return lista_nueva
        elif(re.search("desc",forma,re.IGNORECASE) != None):
            altura_desc = qsort_desc(copia_lista, "altura")
            for i in range(len(altura_desc)):
                #dic_heroes = {} 

                # dic_heroes["nombre"] = altura_desc[i]["nombre"]
                # dic_heroes["altura"] = altura_desc[i]["altura"]
                lista_nueva.append(altura_desc[i])
            return lista_nueva
    else: return retorno

  
# test = ordenar_por_altura(lista_personajes, "desc")
# print ("orde test" ,test)
#3)Ordenar y Listar héroes por fuerza. Preguntar al usuario si lo quiere ordenar de manera ascendente (‘asc’) o descendente (‘desc’)
def listar_por_fuerza(lista_recibida:list,forma:str)->list:
    '''
        Devuelve una lista ordenada de manera ascendente o descendente segun indique el usuario segun fuerza

        RECIBE:
            -Una Lista
            -La forma (asc o desc)
        
        DEVUELVE: Una lista

        VALIDA: Que asc o desc este bien escrito
    
    '''
    retorno = False
    validar_forma = re.search("asc|desc",forma, re.IGNORECASE)
    
    
    if(type(lista_recibida) == list and len(lista_recibida) > 0 and validar_forma != None):
        copia_lista = lista_recibida.copy()
        lista_nueva = []
        if (re.search("asc",forma,re.IGNORECASE) != None):
            fuerza_asc = qsort_asc(copia_lista, "fuerza")
            for i in range(len(fuerza_asc)):
                #dic_heroes = {} 

                # dic_heroes["nombre"] = fuerza_asc[i]["nombre"]
                # dic_heroes["fuerza"ascfuerza_asc = fuerza_asc[i]["fuerza"ascfuerza_asc
                lista_nueva.append(fuerza_asc[i])
            return lista_nueva
        elif(re.search("desc",forma,re.IGNORECASE) != None):
            fuerza_desc = qsort_desc(copia_lista, "fuerza")
            for i in range(len(fuerza_desc)):
                #dic_heroes = {} 

                # dic_heroes["nombre"] = fuerza_desc[i]["nombre"]
                # dic_heroes["fuerza"] = fuerza_desc[i]["fuerza"]
                lista_nueva.append(fuerza_desc[i])
            return lista_nueva
    else: return retorno

# test = listar_por_fuerza(lista_personajes, "asc")
# print(test)

#4) Calcular promedio de cualquier key numérica, filtrar los que cumplan con la condición de superar o no el promedio 
# (preguntar al usuario la condición: ‘menor’ o ‘mayor’) se deberá listar en consola aquellos que cumplan con ser mayores o menores 
# según corresponda.


def calcular_promedio_key_numerica(lista_recibida:list, key:str, forma:str)->list:
    '''
    Calcula el promedio de cualquier key numérica , filtra y lista los datos segun menor o mayor al promedio
    
    DEVUELVE: Una lista con los valores filtrados por mayor o menor

    VALIDA: 
        -Que la key sea numerica
        -Que la forma sea "mayor" o "menor"
    '''
    retorno = False
    validar_forma = re.search("mayor|menor", forma,re.IGNORECASE)
    validar_key = re.search("fuerza|altura|peso", key)
    acumulador_key = 0
    # print(validar_forma)
    # print(validar_key)
    if(type(lista_recibida) == list and len(lista_recibida) > 0 and validar_forma != None and validar_key != None):
        for heroe in lista_recibida:
            acumulador_key += heroe[key]
            
        promedio_key = acumulador_key / len(lista_recibida)
        if(re.search("mayor", forma,re.IGNORECASE)):
            lista_nueva = []
            
            for i in range(len(lista_recibida)):
                if (lista_recibida[i][key] > promedio_key):
    
                    lista_nueva.append(lista_recibida[i])
        elif(re.search("menor", forma,re.IGNORECASE)):
            lista_nueva = []     
            for i in range(len(lista_recibida)):
                
                if (lista_recibida[i][key] < promedio_key):
                    lista_nueva.append(lista_recibida[i])
                    # dic_heroes["nombre"] = lista_recibida[i]["nombre"]
                    # dic_heroes[key] = lista_recibida[i][key]
                    # lista_nueva.append(dic_heroes)  
                    
        return lista_nueva
    else: return retorno
    
# test = calcular_promedio_key_numerica(lista_personajes, "altura", "menor")
# print(test)

#5) Buscar héroes por inteligencia [good, average, high] y listar en consola los que cumplan dicha búsqueda.
def buscar_por_inteligencia(lista_recibida:list, tipo:str)->str:
    '''
    Busca héroes por inteligencia [good, average, high] y lista en consola los que cumplan dicha búsqueda.
    
    VALIDA: Que el tipo sea [good, average, high] con RegEx

    DEVUELVE: Lista impresa con los que cumplen con dicho requisito
    '''

    retorno = False
    validar_tipo = re.search("good|average|high", tipo, re.IGNORECASE)
    if(type(lista_recibida) == list and len(lista_recibida) > 0 and validar_tipo != None):
        lista_nueva = []
        for i in range(len(lista_recibida)):
            if (lista_recibida[i]["inteligencia"] == tipo):
                lista_nueva.append(lista_recibida[i])
        return lista_nueva
    else: return retorno

# test = buscar_por_inteligencia(lista_personajes, "good")
# print(test)

# 6) Exportar a CSV la lista de héroes ordenada según opción elegida anteriormente [1-4]
def fun_mostrar(lista_recibida:list, key="altura"): 
    mensaje = ""
   
    for heroe in lista_recibida:
        mensaje += "{0}, {1}, {2} {3}\n".format(heroe["nombre"],heroe["identidad"],key, heroe[key])
    return mensaje
      
def fun_mostrar_cantidad_especifica(lista_recibida:list):
    mensaje = ""
   
    for heroe in lista_recibida:
        mensaje += "{0}, {1}, {2}, {3}, {4}, {5}\n".format(heroe["nombre"],heroe["identidad"],heroe["altura"]
        ,heroe["peso"],heroe["fuerza"],heroe["inteligencia"])
    return mensaje
        
def exportar_CSV(mensaje:str,nombre_archivo:str):
    '''Exportar a CSV la lista de héroes ordenada según opción elegida anteriormente [1-4]'''
    
    nombre_final = nombre_archivo + ".csv"
    with open(nombre_final, "w+") as archivo:
        archivo.write(mensaje)





def imprimir_menu():
    menu = '''

    1-Listar los primeros N héroes.

    2-Ordenar y Listar héroes por altura.

    3-Ordenar y Listar héroes por fuerza. 

    4-Calcular promedio de cualquier key numérica

    5-Buscar héroes por inteligencia [good, average, high] 

    6-Exportar a CSV la lista de héroes ordenada según opción elegida [1-4]

    '''
    print(menu)
# lista_test = []

# test = listar_personajes(lista_personajes, 10)

# print(test)