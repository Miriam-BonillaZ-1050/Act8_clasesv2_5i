class informacion:
    def mi_lista(self):
        lista_nomperros=["bobby","dollar","fanny"]
        for x in lista_nomperros:
            print(x)

    def mi_tupla(self):
        tupla_nomperros=("pato","quesadilla","gansito")
        for x in tupla_nomperros:
            print(x)

    def mi_conjunto(self):
        conjunto_nomperros={"max","queso","pablito"}
        for x in conjunto_nomperros:
            print(x)

    def mi_diccionario(self):
        dicc_nomperros = {
        "Perro 1:" : "dani",
        "Perro 2:" : "princesa",
        "Perro 3:" : "beom"}
        for x,y in dicc_nomperros.items():
            print(x,y)  

# Creando el objeto
datos=informacion()
print("Listado de nombres de perros:")
datos.mi_lista()
print("")

print("Listado de nombres de gatos:")
datos.mi_tupla()
print("")

print("Listado de nombres de pericos:")
datos.mi_conjunto()
print("")

print("Listado de nombres de perritos:")
datos.mi_diccionario()
