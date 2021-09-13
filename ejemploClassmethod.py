class Persona:
    contador_persona = 0
    
    #contador +1 por cada persona con la clase method
    @classmethod
    def ContadorPersonas(cls):
        cls.contador_persona += 1
        return cls.contador_persona

    def __init__(self,nombre,edad):

        self._idPersona = Persona.ContadorPersonas()  #Llamamos a la clase methodo
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'Persona: {self._idPersona}, {self.nombre}, {self.edad}'

persona1 = Persona('juan', 23)
persona2 = Persona('carla', 30)
persona3 = Persona('alex', 33)
print(persona1, persona2, persona3)

#para recordad, este classmethod  solo se puede usar dentro de esta clse, no se puede
#llamar en otras clases.
