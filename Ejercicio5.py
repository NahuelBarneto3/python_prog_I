
habilidades = [
    {
        "Nombre": "Vision-X",
        "Poder": 64
    },
    {
        "Nombre": "Vuelo",
        "Poder": 32
    },
    {
        "Nombre": "Inteligencia",
        "Poder": 256
    },
    {
        "Nombre": "Metamorfosis",
        "Poder": 1024
    },
    {
        "Nombre": "Super Velocidad",
        "Poder": 128
    },
    {
        "Nombre": "Magia",
        "Poder": 512
    }
]
dic_habilidades = {}
habilidades_utn = []

for ablt in habilidades:
    hab_utn = []
    
    for dato in ablt:
        hab_utn.append(ablt[dato])
    
    hab_utn_tupla = tuple(hab_utn)
    habilidades_utn.append(hab_utn_tupla)
    dic_habilidades["Habilidades_utn"] = habilidades_utn
        


print(habilidades_utn)