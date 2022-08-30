flag = 0
edad_heroe_fuerza_joven = 0
edad_heroe_viejo = 0
contador_fuerza_magia = 0
contador_heroinas = 0 
acumulador_edad_heroinas = 0
contador_heroes = 0
acumulador_edad_heroes_fuerza = 0

while(True):

    nombre_heroe = input("ingrese su nombre de heroe o heroina")
    while(True):
        edad = input("ingrese su edad (mayor a 18 anos)")
        edad =int(edad)
        if(edad < 18): continue
        else: break
    
    while(True):
        sexo = input("Ingrese su sexo ('m' , 'f' o 'nb')")
        if(sexo != "m" and sexo != "f" and sexo != "nb"): continue
        else: break
    
    while(True):
        habilidad = input("Ingrese su habilidad (fuerza , magia o inteligencia)")
        if(habilidad != "fuerza" and habilidad != "magia" and habilidad != "inteligencia"):continue
        else: break

    if((flag == 0 or edad_heroe_fuerza_joven > edad) and habilidad == "fuerza"):
        edad_heroe_fuerza_joven = edad
        nombre_mas_joven = nombre_heroe

    if(flag == 0 or edad_heroe_viejo < edad):
        edad_heroe_viejo = edad
        nombre_heroe_viejo = nombre_heroe

    if((habilidad == "fuerza" or habilidad == "magia") and sexo == "f"):
        contador_fuerza_magia += 1
        if(habilidad == "fuerza" and sexo == "m"):
            contador_heroes += 1 
            acumulador_edad_heroes_fuerza += 1

    if(sexo == "f"):
        contador_heroinas += 1
        acumulador_edad_heroinas += edad
    
    respuesta = input("Quiere seguir ingresando heroes?")
    
    if(respuesta != "no"): continue
    else: break

print ("el heroe | heroina de fuerza mas joven es: " + nombre_mas_joven)
print("el heroe | heroina de mayor mas viejo es: " + nombre_heroe_viejo)
print("la cantidad de heroinas que tienen habilidades de fuerza o magia son: "+ contador_fuerza_magia)

promedio_edad_heroinas = acumulador_edad_heroinas / contador_heroinas
promedio_edad_heroes_fuerza = acumulador_edad_heroes_fuerza / contador_heroes

print("el promedio de edad entre las heroinas es de: " + str(promedio_edad_heroinas))
print("El promedio de edad entre Heroes de fuerza: " + str(promedio_edad_heroes_fuerza))