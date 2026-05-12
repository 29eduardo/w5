import grpc
import calculadora_pb2
import calculadora_pb2_grpc


cliente = grpc.insecure_channel('localhost:5000')

stub = calculadora_pb2_grpc.CalculadoraStub(cliente)
 
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
op= input("Ingresa la operación (+, -, *, /): ").strip()

respuesta = calculadora_pb2.Operacion(a=num1, b=num2)

if op == "+":
    resultado = stub.sumar(respuesta)
elif op == "-":
    resultado = stub.restar(respuesta)
elif op == "*":
    resultado = stub.multiplicar(respuesta)
elif op == "/":
    resultado = stub.dividir(respuesta)
else:
    print("Operación no válida.")
    exit()

print(f"Resultado: {resultado}")




"""
r1 = stub.sumar(
    calculadora_pb2.Operacion(a=10,b=5)
)
r2 = stub.restar(calculadora_pb2.Operacion(a=12,b=2))
r3 = stub.multiplicar(calculadora_pb2.Operacion(a=11,b=2))
r4 = stub.dividir(calculadora_pb2.Operacion(a=2,b=2))


print("La Suma es: ",r1)
print("La Resta es: ",r2)
print("La Multiplicacion es: ",r3)
print("La Division es: ",r4)
"""