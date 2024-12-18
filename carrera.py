from Personaje_clase import Personaje

def main():
    personaje1 = Personaje(
        input("Nombre del personaje 1: "),
        float(input("Altura: ")),
        float(input("Velocidad: ")),
        float(input("Resistencia: ")),
        float(input("Fuerza: "))
    )

    personaje2 = Personaje(
        input("Nombre del personaje 2: "),
        float(input("Altura: ")),
        float(input("Velocidad: ")),
        float(input("Resistencia: ")),
        float(input("Fuerza: "))
    )
    
    
    print("\nInformación inicial:")
    personaje1.mostrar_info()
    print()
    personaje2.mostrar_info()

    personaje1.atacar(personaje2)
    personaje2.atacar(personaje1)  # Esta línea hace que el personaje2 ataque

    print("\nInformación después del ataque:")
    personaje1.mostrar_info()
    print()
    personaje2.mostrar_info()

if __name__ == "__main__":
    main()
