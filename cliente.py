# Importa la herramienta para crear el cliente XML-RPC.
import xmlrpc.client
#Crea una conexión con el servidor XML-RPC.
cliente  = xmlrpc.client.ServerProxy("http://localhost:8000/")
print("===  Calculadora  ===")
a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))
op= input("Ingresa la operación (+, -, *, /): ").strip()

if op == "+":
    resultado = cliente.sumar(a, b)
elif op == "-":
    resultado = cliente.restar(a, b)
elif op == "*":
    resultado = cliente.multiplicar(a, b)
elif op == "/":
    resultado = cliente.dividir(a, b)
else:
    print("Operación no válida.")
    exit()

print(f"Resultado: {resultado}")


# Llamar a las funciones
"""
suma = cliente.sumar(4,9)
print ("La suma es: ",suma)
resta = cliente.restar(6,3)
print ("La resta es: ",resta)
multiplicacion = cliente.multiplicar(6,9)
print("La multiplicacion es: ",multiplicacion)
division  = cliente.dividir(8,7)
print("La division es: ",division)
"""