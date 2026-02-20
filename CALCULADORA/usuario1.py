
class Usuario:
    def __init__(self, nombre,cedula):
        self.nombre = nombre
        self.cedula = cedula
        
    def get_cedula(self):
        return self.cedula
    
    def set_cedula(self,cedula_nueva):
        self.cedula = cedula_nueva
        
    def imrimir_datos(self):
        print(f"Nombre cliente:{self.nombre}")
        print(f"cedula cliente:{self.cedula}")
        
        
    