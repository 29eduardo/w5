import grpc
from concurrent import futures

import calculadora_pb2
import calculadora_pb2_grpc

class CalculadorServidor(
    calculadora_pb2_grpc.CalculadoraServicer
):
    def sumar (self, request,context):
        resultado = request.a + request.b

        return calculadora_pb2.Resultado(
            resultado = resultado
        )
    
    def restar(self, request,context):
        resultado = request.a - request.b
        return calculadora_pb2.Resultado(resultado=resultado)

    def multiplicar(self, request,context):
        resultado = request.a * request.b
        return calculadora_pb2.Resultado(resultado=resultado)

    def dividir(self, request,context):
    #
        if request.b == 0:
            return calculadora_pb2.Resultado(resultado=0)
        
        resultado = request.a // request.b
        return calculadora_pb2.Resultado(resultado=resultado)
    

servidor = grpc.server(futures.ThreadPoolExecutor(max_workers = 10))

calculadora_pb2_grpc.add_CalculadoraServicer_to_server(
    CalculadorServidor(),
    servidor
)


servidor.add_insecure_port('[::]: 5000')
servidor.start()
print("Servidor GRPC ejecutandose...")
servidor.wait_for_termination()