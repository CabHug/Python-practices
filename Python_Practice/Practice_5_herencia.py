class vehiculo:
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.disponible = True

    def vender(self):
        if self.disponible:
            self.disponible = False
            print(f"El vehiculo {self.marca} {self.modelo} ha sido vendido por {self.precio}")
        else:
            print(f"El vehiculo {self.marca} {self.modelo} ya ha sido vendido")

    def get_disponibilidad(self):
        print(f"Estado del vehiculo {self.marca} es: {'Disponible' if self.disponible else 'No disponible'}")
        return self.disponible

    def get_precio(self):
        print(self.precio)
        return self.precio
    
    def arrancar(self):
        raise NotImplementedError("Metodo de subclase")
    
    def detener(self):
        raise NotImplementedError("Metodo de subclase")
    
class carro(vehiculo): #-> Sintaxis que me dice que hereda
    def arrancar(self):
        print("El auto ha arrancado.")

    def detener(self):
        print("El auto de ha detenido.")

class Bicicleta(vehiculo):
    def arrancar(self):
        print("Estamos pedaleando.")

    def detener(self):
        print("Frenando.")

#Una clase hija no necesariamente necesita un constructor, pero si puede tneerlo si necesita atributos propios
class Camion(vehiculo): #-> Sintaxis que me dice que hereda
    def arrancar(self):
        print("El auto ha arrancado.")

    def detener(self):
        print("El auto de ha detenido.")

class cliente:
    def __init__(self, name):
        self.name = name
        self.autos_comprados = []
    
    def comprar(self, vehiculo:vehiculo):# La notacion vehiculo:vehco define el parametro como un objeto de esa clase
        if vehiculo.disponible:
            vehiculo.vender()
            self.autos_comprados.append(vehiculo)

        else:
            print("Vehiculo no disponible")

    def consultar_vehiculo(self, vehiculo:vehiculo):
        vehiculo.get_disponibilidad()


class concesionario:
    def __init__(self):
        self.inventario = []

    def agregar_vehiculo(self, vehiculo:vehiculo):
        self.inventario.append(vehiculo)

    def mostrar(self):
        for i in self.inventario:
            print(i.marca)

#chreacion de vehiculos
mazda1 = carro("Mazda", "1995", 15000)
bici1 = Bicicleta("Roja","20210", 500)
camion1 = Camion("MGZ","2020", 500000)

print("Info Carro")
mazda1.get_disponibilidad()
mazda1.get_precio()
mazda1.arrancar()
mazda1.detener()
print("Info Bici")
bici1.get_disponibilidad()
print("Info Camion")
camion1.get_precio()

conc = concesionario()
conc.agregar_vehiculo(mazda1)
conc.agregar_vehiculo(bici1)
conc.agregar_vehiculo(camion1)

conc.mostrar()

hugo = cliente("Hugo")

hugo.consultar_vehiculo(mazda1)
hugo.comprar(mazda1)
hugo.consultar_vehiculo(mazda1)
