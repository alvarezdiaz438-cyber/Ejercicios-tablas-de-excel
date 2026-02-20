from usuario1 import Usuario
from carro1 import Carro
from estacionamiento import Estacionamiento


nombre = input("ingrese nombre del cliente: ")
cedula = int(input("ingrese cedula del cliente: "))
tipo_cliente = input("ingrese tipo de cliente: ") 
obj_cliente = Usuario(nombre, cedula, tipo_cliente) 

# Registro de Carro
placa = input("ingrese placa del carro: ")
marca = input("ingrese la marca del carro: ")
color = input("ingrese color del carro: ")
obj_carro = Carro(placa, marca, color)


obj_estacionamiento = Estacionamiento()

puesto = int(input("ingrese el numero de puesto: "))
obj_estacionamiento.set_puesto(puesto) 
obj_estacionamiento.registrar_entrada(obj_cliente, obj_carro) 
obj_estacionamiento.guardar()

obj_estacionamiento.mostrar_info()

registrar_salida_input = input("¿Desea ingresar la salida de un carro? [si/no] ")

if registrar_salida_input.lower() == "si":
    placa_salida = input("ingrese la placa del carro para dar salida: ")
    obj_estacionamiento.registrar_salida(placa_salida)
    obj_estacionamiento.guardar()

obj_estacionamiento.mostrar_info()
