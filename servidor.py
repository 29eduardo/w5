#Importa la herramienta para crear el servidor XMLRPC
from xmlrpc.server import SimpleXMLRPCServer

#Definir las funciones
def sumar (a,b):
    return a+b

def restar (a,b):
    return a-b

def multiplicar (a,b):
    return a*b

def dividir (a,b):
   if b != 0:
       return a/b
   else:
       print("Error")
       return None

#Crear el servidor  
servidor = SimpleXMLRPCServer(("localhost", 8000))

#Publicar las funciones para poder ser llamadas

servidor.register_function(sumar, "sumar")
servidor.register_function(restar, "restar")
servidor.register_function(multiplicar, "multiplicar")
servidor.register_function(dividir, "dividir")

servidor.serve_forever()
