class Numero:
    def __init__(self,numero):
        self.numero = numero
    
    def get_numero(self):
        return self.numero
    
    def set_numero(self,numero_nuevo):
        self.numero = numero_nuevo
        
    def impriir_numero(self):
        print(f"Numero: {self.numero}")