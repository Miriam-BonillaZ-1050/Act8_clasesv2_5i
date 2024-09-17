print("Clases version 2 el constructor")
class perro:
# Funcion Constructor
    def __init__(self,color,edad):
        self.color=color
        self.edad=edad
# Funciones creadas por el usuario
    def muerde(self):
        print("Chale el perro me mordio")
    def chatperro(mensaje):
        print(f"Chat perro {mensaje}")    
    def chatperra(mensajepe):
        print(f"Chat perro {mensajepe}")
    def datos(self):
        print(f"Color {self.color} edad {self.edad}")
# Crear el objeto
chihuas=perro("Negro",2)     
# Llamadas a funciones
chihuas.datos()
chihuas.muerde()
chihuas.chatperro("Hola canina")
chihuas.chatperra("Hola bobby")
chihuas.chatperro("Quieres ser mi guaoguao?")
chihuas.chatperra("uuuuff....")