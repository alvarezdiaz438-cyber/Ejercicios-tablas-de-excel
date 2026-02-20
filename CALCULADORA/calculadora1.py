class Calculadora:
    
    def __init__(self,fecha_uso):
        self.tipo_operacion = ""
        self.resultado = ""
        self.fecha_uso = fecha_uso
        self.tabla = ""
    
    
    
    def calcular_suma(self,num1,num2,result_suma):
        result_suma = num1.get_numero()+num2.get_numero()
        print(f"El resultado de la suma es: {result_suma}")
        return result_suma
    
    def calcular_resta(self,num1,num2,result_resta):
        result_resta = num1.get_numero()-num2.get_numero()
        print(f"El resultado de la resta es: {result_resta}")
        return result_resta
    
    def calcular_multiplicacion(self,num1,num2,resultado_multiplicacion):
        resultado_multiplicacion = num1.get_numero()*num2.get_numero()
        print(f"El resultado de la multiplicación es: {resultado_multiplicacion}")
        return resultado_multiplicacion
    
    def calcular_division(self,num1,num2,resultado_division):
        resultado_division = num1.get_numero()/num2.get_numero()
        print(f"El resultado de la división es: {resultado_division}")
        return resultado_division
      
               
    def get_fecha(self):
        return self.fecha  
        
    def guardar_info_tabla(self, tabla):
        self.tabla = tabla  
        
    def mostrar_tabla(self):    
        print(f"Tabla: {self.tabla}")
        
        
        
    def mostrar_info(self):
        print(f"fecha de la calculadora: {self.fecha_uso}")
    
        
        

        
    


        
    