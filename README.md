# Python-Programacion Orientada a Objetos(POO)
voy a subir los ejercicios  y el codigo de programación orientada a objetos con  Python 

aqui dejo los conceptos basicos de POO

1. Clase
Definición: Es una plantilla que define los atributos (datos) y métodos (comportamientos) que tendrán los objetos creados a partir de ella.

Ejemplo: class Perro:

2. Objeto
Definición: Es una instancia concreta de una clase. Cada objeto tiene su propio estado.

Ejemplo: mi_perro = Perro("Rex", "Labrador", 4)

3. Atributos
Definición: Son las variables que pertenecen a un objeto. Describen el estado del objeto.

Ejemplo: self.nombre, self.edad

4. Métodos
Definición: Son funciones definidas dentro de una clase que definen el comportamiento de los objetos.

Ejemplo: def ladrar(self):

5. __init__ (Constructor)
Definición: Es un método especial que se ejecuta automáticamente cuando se crea un objeto. Se usa para inicializar atributos.

Ejemplo:

python
Copiar
Editar
def __init__(self, nombre):
    self.nombre = nombre
6. self
Definición: Es una referencia al propio objeto. Permite acceder a sus atributos y métodos dentro de la clase.

Importante: Siempre es el primer parámetro de los métodos de instancia.

7. Encapsulamiento
Definición: Esconder la información interna del objeto y controlar su acceso. Se protege el estado interno del objeto.

En Python: se usa _atributo o __atributo para indicar que no debería ser accedido directamente.

Ejemplo:

python
Copiar
Editar
class Persona:
    def __init__(self):
        self.__dni = "12345678"  # Atributo privado
8. Herencia
Definición: Permite crear una nueva clase que hereda atributos y métodos de otra clase.

Ejemplo:

python
Copiar
Editar
class Animal:
    def hablar(self):
        print("Hace un sonido")

class Gato(Animal):
    def hablar(self):
        print("Miau")
9. Polimorfismo
Definición: Permite que diferentes clases tengan métodos con el mismo nombre, pero comportamiento distinto.

Ejemplo:

python
Copiar
Editar
for animal in [Perro(), Gato()]:
    animal.hablar()  # Cada uno se comporta distinto
10. Abstracción
Definición: Consiste en ocultar los detalles complejos y mostrar solo lo esencial del objeto.

Ejemplo conceptual: Usar un método .enviar_mensaje() sin saber cómo internamente lo envía.

11. Métodos especiales o mágicos
Definición: Son métodos que empiezan y terminan con __, como __init__, __str__, __len__, etc. Sirven para personalizar el comportamiento de los objetos.

Ejemplo:

python
Copiar
Editar
def __str__(self):
    return f"Perro: {self.nombre}"
12. Composición
Definición: Es cuando una clase contiene objetos de otra clase. Es una relación "tiene un".

Ejemplo:

python
Copiar
Editar
class Motor:
    pass

class Auto:
    def __init__(self):
        self.motor = Motor()  # El auto tiene un motor
13. Instancia
Definición: Es un objeto específico de una clase.

Ejemplo: auto1 = Auto() ← auto1 es una instancia de la clase Auto.

14. Clase base y clase derivada
Clase base (superclase): Es la clase que hereda sus atributos y métodos.

Clase derivada (subclase): Es la clase que hereda de la base y puede modificar o extender su comportamiento.

15. Sobreescritura de métodos (override)
Definición: Es redefinir un método en una subclase que ya existía en la clase base.

Ejemplo:

python
Copiar
Editar
class Animal:
    def hablar(self):
        print("Sonido")

class Perro(Animal):
    def hablar(self):
        print("Guau")  # Sobrescribe
