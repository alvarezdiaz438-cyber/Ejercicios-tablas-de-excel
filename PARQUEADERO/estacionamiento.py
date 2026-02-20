from usuario1 import Usuario
from carro1 import Carro

class Estacionamiento:
    def __init__(self):
        self.puesto = "libre"
        self.fecha_entrada = None
        self.h_entrada = None
        self.h_salida = None
        self.estado = "Libre"
        self.cliente = None
        self.carro = None
        self.txt_tabla = ""
        
    def get_puesto(self):
        return self.puesto
    
    def get_fecha_entrada(self):
        return self.fecha_entrada
    
    def get_h_entrada(self):
        return self.h_entrada  
    
    def get_h_salida(self):
        return self.h_salida
    
    def get_estado(self):
        return self.estado
    
    def set_puesto(self, nuevo_puesto):
        self.puesto =  nuevo_puesto    
    def set_estado(self, nueva_estado):
        self.estado = nueva_estado
        
        
    
    def registrar_Entrada(self, cliente, carro):
        self.cliente = cliente
        self.carro = carro
        hora = ("10:42")
        self.fecha_entrada = ("22-04-2025")
        self.h_entrada = hora
        self.estado = "Ocupado"
        
    def registrar_salida(self, placa_buscar):
        if self.estado == "Ocupado" and self.carro.get_placa() == placa_buscar:
            
            hora = ("12:00")
            self.h_salida = hora
            self.estado = "libre"
        
    def guardar(self):
        self.txt_tabla += f"\nPuesto: {self.puesto} ||Estado: {self.estado}  || Fecha Entrada: {self.fecha_entrada} || Hora Entrada: {self.h_entrada} || Hora Salida: {self.h_salida}"
    
    def mostrar_info(self):
        print (self.txt_tabla)