from xmlrpc.server import SimpleXMLRPCServer

def c_a_f(celsius):
    return (celsius * 9/5) + 32

def f_a_c(fahrenheit):
    return (fahrenheit - 32) * 5/9

server = SimpleXMLRPCServer(("localhost", 8000))
print("Servidor XML-RPC iniciado en puerto 8000...")
server.register_function(c_a_f, "celsius_a_fahrenheit")
server.register_function(f_a_c, "fahrenheit_a_celsius")
server.serve_forever()