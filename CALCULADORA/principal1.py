from numero1 import Numero
from usuario1 import Usuario
from calculadora1 import Calculadora

nombre = input("ingrese el nombre del usuario: ")
obj_usuario = Usuario(nombre, "777777777")
obj_numero1 = Numero(8)
obj_numero2 = Numero(9)
obj_tipo_operacion = input("Ingrese el tipo de operación (suma, resta, multiplicacion, division): ")

obj_calculadora = Calculadora("2024-02-01")


if obj_tipo_operacion == "suma":
    obj_calculadora.calcular_suma(obj_numero1, obj_numero2,0)
    
elif obj_tipo_operacion == "resta":
    obj_calculadora.calcular_resta(obj_numero1, obj_numero2,0)
elif obj_tipo_operacion == "multiplicacion":
    obj_calculadora.calcular_multiplicacion(obj_numero1, obj_numero2,0)
elif obj_tipo_operacion == "division":
    obj_calculadora.calcular_division(obj_numero1, obj_numero2,0)
    
else:
    print("Tipo de operación no válida.")
    resultado = 0 
    
obj_calculadora.mostrar_info()