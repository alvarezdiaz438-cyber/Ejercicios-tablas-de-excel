class Carro :
    def __init__(self, tipo_carro,placa ,color):
        self.tipo_carro = tipo_carro
        self.placa = placa
        self.color = color

    def get_tipo_carro(self):
        return self.tipo_carro
    
    def set_tipo_carro(self, nuevo_tipo_carro):
        self.tipo_carro = nuevo_tipo_carro

    def get_placa(self):
        return self.placa
    
    def set_placa(self, nueva_placa):
        self.placa = nueva_placa

    def get_color(self):
        return self.color
    
    def set_color(self, nuevo_color):
        self.color = nuevo_color

    def imprimir_datos(self):
        print(f"Nombre carro:{self.tipo_carro}")
        print(f"placa carro:{self.placa}")
        print(f"color carro:{self.color}")
      
        