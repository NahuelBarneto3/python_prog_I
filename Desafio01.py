from importlib.resources import is_resource
from itertools import count
from typing import Counter
from data_stark import lista_personajes


'''
for heroe in lista_personajes:
    print(heroe["nombre"],heroe["altura"])


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
 }
'''

#A) Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M
def mostrar_por_genero_M():
    
    for personaje in lista_personajes:
        if(personaje["genero"] == "M"):
            print("Nombre: {0} ".format(personaje["nombre"]))
            
#B) Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F
def mostrar_por_genero_F():
    
    for personaje in lista_personajes:
        if(personaje["genero"] == "F"):
            print("Nombre: {0} ".format(personaje["nombre"]))


def primer_masculino():

    for personaje in lista_personajes:
        if(personaje["genero"] == "M"):   
            return personaje


def primer_femenino():

    for personaje in lista_personajes:
        if(personaje["genero"] == "F"):   
            return personaje

#C) Recorrer la lista y determinar cuál es el superhéroe más alto de género M
def mostrar_mas_alto_M():
    masculino_alto = primer_masculino()
    
    for personaje in lista_personajes:
        personaje["altura"] = float(personaje["altura"])
        
        if (personaje["altura"] > masculino_alto["altura"]):
            masculino_alto = personaje




    print("el personaje masculino mas alto es : {0} Y su altura es de : {1}".format(masculino_alto["nombre"], masculino_alto["altura"]))


#D) Recorrer la lista y determinar cuál es el superhéroe más alto de género F 

def mostrar_mas_alto_F():
    femenino_alto = primer_femenino()
    femenino_alto["altura"] = float(femenino_alto["altura"])


    for personaje in lista_personajes:
        personaje["altura"] = float(personaje["altura"])
    
        if ((personaje["altura"] > femenino_alto["altura"]) and personaje["genero"] == "F"):
            femenino_alto = personaje

    print("el personaje femenino mas alto es : {0} Y su altura es de : {1}".format(femenino_alto["nombre"], femenino_alto["altura"]))

# E) Recorrer la lista y determinar cuál es el superhéroe más bajo  de género M 
def mostrar_mas_bajo_M():
    masculino_bajo = primer_masculino()
    
    for personaje in lista_personajes:
        personaje["altura"] = float(personaje["altura"])

        if (personaje["altura"] < masculino_bajo["altura"]):
            masculino_bajo = personaje
            
    print("el personaje masculino mas bajo es : {0} Y su altura es de : {1}".format(masculino_bajo["nombre"], masculino_bajo["altura"]))

# F) Recorrer la lista y determinar cuál es el superhéroe más bajo  de género F 
def mostrar_mas_bajo_F():
    femenino_bajo = primer_femenino()
    femenino_bajo["altura"] = float(femenino_bajo["altura"])
    
    for personaje in lista_personajes:
        personaje["altura"] = float(personaje["altura"])
        
        if ((personaje["altura"] < femenino_bajo["altura"]) and personaje["genero"] == "F"):
            femenino_bajo = personaje

    print("el personaje femenino mas bajo es : {0} Y su altura es de : {1}".format(femenino_bajo["nombre"], femenino_bajo["altura"]))

# G) Recorrer la lista y determinar la altura promedio de los  superhéroes de género M
def altura_promedio_M():
    acumulador_altura_f = 0
    contador_m = 0

    for personaje in lista_personajes:
        personaje["altura"] = float(personaje["altura"])
        if(personaje["genero"] == "M"):
            acumulador_altura_f += personaje["altura"]
            contador_m += 1

    print("el promedio de altura de los masculinos es: {0} metros".format(acumulador_altura_f/contador_m))

#H) Recorrer la lista y determinar la altura promedio de los  superhéroes de género F
def altura_promedio_F():
    acumulador_altura_f = 0
    contador_m = 0
    for personaje in lista_personajes:
        personaje["altura"] = float(personaje["altura"])
        if(personaje["genero"] == "F"):
            acumulador_altura_f += personaje["altura"]
            contador_m += 1

    print("el promedio de altura de las heroinas es: {0} metros".format(acumulador_altura_f/contador_m))

#I) Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F)
def listado_completo():
    print()

#J) Determinar cuántos superhéroes tienen cada tipo de color de ojos.

def cantidad_personajes_por_color_ojos():
    cantidad_personajes_por_color_ojos = {}


    for personaje in lista_personajes:
        cantidad_personajes_por_color_ojos[personaje["color_ojos"]] = 0

    for personaje in lista_personajes:
        cantidad_personajes_por_color_ojos[personaje["color_ojos"]] += 1

    for tipo in cantidad_personajes_por_color_ojos:
        print("existen {0} personajes con color de ojo {1}".format(cantidad_personajes_por_color_ojos[tipo],tipo ))


#K) Determinar cuántos superhéroes tienen cada tipo de color de pelo.
def cantidad_personajes_por_color_pelo():
    cantidad_personajes_por_color_pelo = {}


    for personaje in lista_personajes:
        cantidad_personajes_por_color_pelo[personaje["color_pelo"]] = 0

    for personaje in lista_personajes:
        cantidad_personajes_por_color_pelo[personaje["color_pelo"]] += 1
    
    for tipo in cantidad_personajes_por_color_pelo:
        print("existen {0} personajes con color de pelo {1}".format(cantidad_personajes_por_color_pelo[tipo],tipo ))

#L)Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’). 
def cuantos_por_tipo_de_inteligencia():
    tipo_inteligencia = {}

    for personaje in lista_personajes:
        tipo_inteligencia[personaje["inteligencia"]] = 0

    for personaje in lista_personajes:
        tipo_inteligencia[personaje["inteligencia"]] += 1
    
    for tipo in tipo_inteligencia:
        print("existen {0} personajes de inteligencia {1}".format(tipo_inteligencia[tipo],tipo ))

#K) Listar todos los superhéroes agrupados por color de ojos.
def listar_color_ojos():
    
    dict_color_ojos = {}
    #lista_color_ojos = {"marron": ["hulk", "thor", "batman"]}

    for personajes in lista_personajes:
        personajes["color_ojos"] = personajes["color_ojos"].lower() 
        dict_color_ojos[personajes["color_ojos"]] = []
        
    for personajes in lista_personajes:
        for color in dict_color_ojos:
            if (personajes["color_ojos"] == color):
                dict_color_ojos[color].append(personajes["nombre"])

    for color in dict_color_ojos:
        print("Color: {0}".format(color))
        for nombre_pj in dict_color_ojos[color]:
            print("\t {0}".format(nombre_pj))



    # for personaje in lista_personajes:
    #     for color in lista_color_ojos:
    #         if personaje["color_ojos"] == color:
    #             lista_color_ojos[color] = personaje["nombre"]
    
    
    #print(lista_color_ojos)





#mostrar_por_genero_M()
#mostrar_por_genero_F()
#mostrar_mas_alto_M()
#mostrar_mas_alto_F()
#mostrar_mas_bajo_M()
#mostrar_mas_bajo_F()
#altura_promedio_M()
#altura_promedio_F()
#cantidad_personajes_por_color_ojos()
#cantidad_personajes_por_color_pelo()
#cuantos_por_tipo_de_inteligencia()
listar_color_ojos()
# #while True:
        
#     respuesta = input("Elija una de las siguientes opciones: \n 1 para obtener heroes Masculinos")
#     if(respuesta == "1"):
