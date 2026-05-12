import xmlrpc.client

servidor = xmlrpc.client.ServerProxy("http://localhost:8000/")

print("=== Conversor de Temperatura  ===")
print("1. Convertir Celsius a Fahrenheit")
print("2. Convertir Fahrenheit a Celsius")

opcion = input("Seleccione una opción (1 o 2): ")


valor = float(input("Ingrese la temperatura a convertir: "))

if opcion == "1":
    
    resultado = servidor.celsius_a_fahrenheit(valor)
    print(f"\n>> {valor}°C equivalen a {resultado:.2f}°F")
    
elif opcion == "2":
    
    resultado = servidor.fahrenheit_a_celsius(valor)
    print(f"\n>> {valor}°F equivalen a {resultado:.2f}°C")
    
else:
    print("Opción no válida.")



