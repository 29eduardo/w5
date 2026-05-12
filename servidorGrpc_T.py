import grpc
from concurrent import futures #Importa herramientas para trabajar  con varios hilos

import temperatura_pb2
import temperatura_pb2_grpc


class ConversorTemperaturaServidor(
    temperatura_pb2_grpc.ConversorTemperaturaServicer
):
    def CelsiusAFahrenheit(self,request,context):
        celsius = request.valor
        fahrenheit = (celsius* 9/ 5) + 32


        print(f"  {celsius}°C → {fahrenheit:.2f}°F")

        return temperatura_pb2.ResultadoTemperatura(
            resultado=fahrenheit,
            descripcion=f"{celsius}°C equivale a {fahrenheit:.2f}°F"
        )
    
    def FahrenheitACelsius(self,request,context):
        fahrenheit= request.valor
        celsius= (fahrenheit - 32 ) * 5 / 9
        print(f" {fahrenheit}°F → {celsius:.2f}°C") 
        
        return temperatura_pb2.ResultadoTemperatura(
            resultado = celsius,
            descripcion = f"{fahrenheit}°F equivale a {celsius:.2f}°C"
       
        )
   
    
#Crea el servidor gRPC. max_workers=10 significa que puede atender hasta 10 tareas en paralelo
servidor = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

#Registra tu clase CalculadoraServidor dentro del servidor gRPC. pero no sabe que funciones ofrecer.
temperatura_pb2_grpc.add_ConversorTemperaturaServicer_to_server(
    ConversorTemperaturaServidor(),
    servidor
)
#Abre el puerto 50051 para recibir conexiones.
#[::] significa que acepta conexiones desde caulquier direccion dispnible
servidor.add_insecure_port('[::]:5000')

servidor.start()

print("Servidor gRPC. ejecutandose...")

#Mantiene el servidor encendido esperando peticiones
servidor.wait_for_termination()