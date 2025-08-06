class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre}")

# Crear objeto
p1 = Persona("Danny")
p1.saludar()
