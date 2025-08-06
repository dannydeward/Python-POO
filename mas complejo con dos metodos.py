class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre}")

    def responder_saludo(self, cantidad_personas):
        print(f"\nMucho gusto a todos, yo soy {self.nombre}. Me saludaron {cantidad_personas} personas.")
        

# Lista de nombres de personas que saludan
nombres = ["Ana", "Luis", "Sofía", "Carlos"]

# Crear lista de objetos Persona
personas = [Persona(nombre) for nombre in nombres]

# Cada persona saluda
for persona in personas:
    persona.saludar()

# Juan también es un objeto Persona
juan = Persona("Juan")

# Juan responde a todos los que saludaron
juan.responder_saludo(len(personas))
