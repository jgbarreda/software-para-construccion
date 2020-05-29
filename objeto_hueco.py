''' En este ejemplo he creado una clase hueco, con un atributo 'tipo' que puedes definir como un string y un constructor 
con la medidas del hueco. Los métodos alfeizar y carpintería te dan las medidas de estos elementos en un string'''  

class Hueco:
        tipo=''
        def __init__(self, a, b):
                self.ancho = a
                self.alto = b

        def __str__(self):
                return 'Hueco tipo ' + self.tipo + ' de medidas ' + str(self.ancho) + ' x ' + str(self.alto)
                
        def alfeizar(self):
                alfeizar=self.ancho
                return 'La piedra de alfeizar mide ' + str(alfeizar) + ' metros'

        def carpinteria(self):
                carpinteria=float('{0:.4f}'.format(self.ancho*self.alto))
                return 'la carpinteria mide ' + str(carpinteria) + ' m2.'
                
        
def mide_hueco(a,b):
             v1=Hueco(a,b)
             alf=v1.alfeizar()
             carp=v1.carpinteria()
             return alf + ' y ' + carp
             
             
if __name__ == "__main__":
    print(mide_hueco(0.8, 1.4))
