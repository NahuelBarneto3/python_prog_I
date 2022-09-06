from data_stark import lista_personajes
'''
lista_heroes =
[
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
]
'''


#print(lista_personajes)

for heroes in lista_personajes:
    print("Heroe: {0} Altura: {1} ".format(heroes["nombre"], heroes["altura"]))
