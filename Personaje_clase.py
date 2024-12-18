class Personaje:
    def __init__(self, nombre, altura, velocidad, resistencia, fuerza):
        self.nombre = nombre
        self.altura = altura
        self.velocidad = velocidad
        self.resistencia = resistencia
        self.fuerza = fuerza
        self.vida = 10  # Atributo que indica la vida del personaje
        self.estado = True  # Atributo que indica si el personaje está vivo o no

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Altura: {self.altura}")
        print(f"Velocidad: {self.velocidad}")
        print(f"Resistencia: {self.resistencia}")
        print(f"Fuerza: {self.fuerza}")
        print(f"Vida: {self.vida}")

    def atacar(self, otro_personaje):
        daño = self.fuerza - otro_personaje.resistencia
        if daño > 0:
            otro_personaje.vida -= daño
            if otro_personaje.vida <= 0:
                otro_personaje.estado = False
                print(f"{otro_personaje.nombre} ha sido derrotado!")
        else:
            print(f"{self.nombre} no ha podido atacar a {otro_personaje.nombre}!")