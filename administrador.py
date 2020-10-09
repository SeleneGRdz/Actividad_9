from particula import Particula

class Administrador:
    def __init__(self):
        self.__particulas = []

    def agregar_final(self, particula:Particula):
        self.__particulas.append(particula)

    def agregar_inicio(self, particula:Particula):
        self.__particulas.insert(0, particula)

    def mostrar(self):
        for particula in self.__particulas:
            print(particula)

L1 = Particula(id=1234, origen_x=45, origen_y=12,destino_x=32, destino_y=12, velocidad=203, red=1, green=0, blue=120)
administrador = Administrador()
administrador.agregar_final(L1)
administrador.mostrar()