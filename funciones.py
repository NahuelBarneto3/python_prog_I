
import json
import re
url_archivo = r"D:\UTN\Utn Ingreso\Prog\python_prog_I\Examen"
def import_json(url_archivo:str)->list:
    with open(url_archivo) as archivo:
        data = json.load(archivo)
        return data["results"]

lista_personajes = import_json(url_archivo)
print(lista_personajes)
#1 - Listar los personajes ordenados por altura
def qsort_altura(lista_a_ordenar:list, key="altura")->list:
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

    lista_izq = qsort_altura(lista_izq, key)
    lista_izq.append(pivot)
    lista_der = qsort_altura(lista_der, key)

    return lista_izq + lista_der
   
def ordenar_por_altura(lista_recibida:list)->list:


    retorno = False
    
    if(type(lista_recibida) == list and len(lista_recibida) > 0 ):
        copia_lista = lista_recibida.copy()
        lista_nueva = []
        altura_ordenada = qsort_altura(copia_lista)
        for i in range(len(altura_ordenada)):
            lista_nueva.append(altura_ordenada[i])
        return lista_nueva
    else: return retorno

#ordenar_por_altura()