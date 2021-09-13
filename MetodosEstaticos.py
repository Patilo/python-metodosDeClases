class MiClase:

    VariableClase = 'variable clase'

    def __init__(self, variableInstancia):
        self.variableInstancia = variableInstancia

    #creamos con el decorador un metodo estatico
    #no pueden acceder a las variables de instancia, solo la clase
    #no se accede a self ya q se relaciona con objetos y no atributos
    #podemos acceder a la variable de clase solo x la clase padre
    @staticmethod
    def metodo_estatico():
        print(MiClase.VariableClase)
    #luego se manda a llamar
    #MiClase.metodo_estatico()

    @classmethod
    #recibe los metodos de clase directos, pero no los self, estos pueden ser
    #llamados con cls ejemplo cls.nombre

    def metodoClase(cls):
        print(cls.VariableClase)
    def metodo_instancia(self):
        self.metodo_estatico()
        self.metodoClase()
        print(self.VariableClase)
        print(self.variableInstancia)

MiClase.metodoClase()
miobjeto1 = MiClase('Valor Variable Instancia')
miobjeto1.metodoClase()
miobjeto1.metodo_instancia()





