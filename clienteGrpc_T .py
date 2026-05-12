import grpc
import temperatura_pb2
import temperatura_pb2_grpc


#Crea un canal de comunicacion con el servidor
#cliente = grpc.insecure_channel('172.31.115.158:5000')
cliente = grpc.insecure_channel('localhost:5000')

#Crea el stub. llamar funciones remotas como 
stub = temperatura_pb2_grpc.ConversorTemperaturaStub(
    cliente)

print("─" * 40)
print("  CONVERSOR DE TEMPERATURA")
print("─" * 40)
print("  1. Celsius     →  Fahrenheit")
print("  2. Fahrenheit  →  Celsius")
print("─" * 40)

opcion = input("  Elige una opción (1/2): ").strip()

valor = float(input("  Ingresa la temperatura: "))

if opcion == "1":
    solicitud = temperatura_pb2.SolicitudTemperatura(valor=valor)
    respuesta = stub.CelsiusAFahrenheit(solicitud)
    print("  Resultado:", respuesta.descripcion)

elif opcion == "2":
    solicitud = temperatura_pb2.SolicitudTemperatura(valor=valor)
    respuesta = stub.FahrenheitACelsius(solicitud)
    print("  Resultado:", respuesta.descripcion)

else:
    print("  Opción no válida.")

cliente.close()