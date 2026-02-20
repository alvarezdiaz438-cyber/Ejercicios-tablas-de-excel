
class Usuario:
    def __init__(self, nombre,cedula,tipo_usuario):
        self.nombre = nombre
        self.cedula = cedula
        self.tipo_usuario = tipo_usuario
        
    def get_cedula(self):
        return self.cedula
    
    def set_cedula(self,cedula_nueva):
        self.cedula = cedula_nueva

    def get_tipo_usuario(self):
        return self.tipo_usuario
    
    def set_tipo_usuario(self,tipo_usuario_nuevo):
        self.tipo_usuario = tipo_usuario_nuevo
        
    def imprimir_datos(self):
        print(f"Nombre cliente:{self.nombre}")
        print(f"cedula cliente:{self.cedula}")
        print(f"tipo usuario cliente:{self.tipo_usuario}")
        
    