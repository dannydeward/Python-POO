class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre}")


# Lista de nombres
nombres = ["Ana", "Luis", "Sofía", "Carlos"]

# Crear una lista de objetos Persona
personas = [Persona(nombre) for nombre in nombres]

# Cada persona saluda
for persona in personas:
    persona.saludar()
