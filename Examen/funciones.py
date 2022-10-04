
import json
import re
url_archivo = r"D:\UTN\Utn Ingreso\Prog\python_prog_I\Examen\data.json"
def cargar_json(url_archivo:str)->list:
    with open(url_archivo) as archivo:
        data = json.load(archivo)
        return data["results"]

        '''
        	{
			"name": "Luke Skywalker",
			"height": "172",
			"mass": "77",
			"gender": "male"
		},
        
        '''
def validar_RegEx(a_validar:str, patron_valicion)-> bool|int:

    respuesta_validada = re.search(patron_valicion, a_validar, re.IGNORECASE)
    if( respuesta_validada != None):
        a_validar = a_validar.lower()
        a_validar = a_validar.replace(" ","")
        return a_validar
    else: return False

lista_personajes = cargar_json(url_archivo)
#print(lista_personajes)
#1 - Listar los personajes ordenados por altura
def qsort_caracteristicas(lista_a_ordenar:list, key="height")->list:
    lista_recibida = lista_a_ordenar[:]
    lista_der = []
    lista_izq = []
    
    if(len(lista_a_ordenar) <= 1):
        return lista_a_ordenar
    else:
        pivot = lista_recibida[0]
        for elemento in lista_recibida[1:]:
            elemento[key] = int(elemento[key])
            pivot[key] = int(pivot[key])
            if (elemento[key] > pivot[key]):
                
                lista_der.append(elemento)
            else:
                lista_izq.append(elemento)

    lista_izq = qsort_caracteristicas(lista_izq, key)
    lista_izq.append(pivot)
    lista_der = qsort_caracteristicas(lista_der, key)

    return lista_izq + lista_der
   
def ordenar_por_altura(lista_recibida:list)->list:

    
    if(type(lista_recibida) == list and len(lista_recibida) > 0 ):
        copia_lista = lista_recibida.copy()
        lista_nueva = []
        altura_ordenada = qsort_caracteristicas(copia_lista)
        for i in range(len(altura_ordenada)):
            lista_nueva.append(altura_ordenada[i])
        return lista_nueva
    else: return False

# lista_ordenada = ordenar_por_altura(lista_personajes)
# print(lista_ordenada)

#2 - Mostrar el personaje mas alto de cada genero
def mostrar_mas_alto_por_genero(lista_recibida:list):

    
    
    if(type(lista_recibida) == list and len(lista_recibida) > 0 ):
        
        for i in range(len(lista_recibida)):
            if(lista_recibida[i]["gender"] == "male"):
                print_mas_alto_male = lista_recibida[i]["name"]
                if(len(lista_recibida) == 1): break
            elif(lista_recibida[i]["gender"] == "female"):
                print_mas_alto_female= lista_recibida[i]["name"]
                if(len(lista_recibida) == 1): break
            elif(lista_recibida[i]["gender"] == "n/a"):
                print_mas_alto_na = lista_recibida[i]["name"]
                if(len(lista_recibida) == 1): break 
        print("El mas alto Male es: {0}\nLa mas alta Female es: {1}\nEl mas alto sin genero es: {2}".format(print_mas_alto_male,print_mas_alto_female,print_mas_alto_na))
    else:return False
#mostrar_mas_alto_por_genero(lista_ordenada)

#3 - Ordenar los personajes por peso
def ordenar_por_peso(lista_recibida:list)->list:

    if(type(lista_recibida) == list and len(lista_recibida) > 0 ):
        copia_lista = lista_recibida.copy()
        lista_nueva = []
        altura_ordenada = qsort_caracteristicas(copia_lista,"mass")
        for i in range(len(altura_ordenada)):
            lista_nueva.append(altura_ordenada[i])
        return lista_nueva
    else: return False
         

'''
        	{
			"name": "Luke Skywalker",
			"height": "172",
			"mass": "77",
			"gender": "male"
		},
        
        '''
#5 - Exportar lista personajes a CSV
def mostrar(lista_recibida:list, key:str):
    mensaje = "" 
    for personaje in lista_recibida:
        mensaje += "{0}, {1}\n".format(personaje['name'],personaje[key])
    return mensaje

def export_csv(mensaje:str, nombre_archivo:str):
    nombre_final = nombre_archivo + ".csv"
    with open(nombre_final, "w") as archivo:
        archivo.write(mensaje)
# test = ordenar_por_peso(lista_personajes)   
# print(test)