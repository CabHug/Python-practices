dic = [
    {
        'name': 'Hugo',
        'age': 31,
        'salary': 5000000
    },
    {
        'name': 'Andres',
        'age': 31,
        'salary': 4500000
    },
    {
        'name': 'Laura',
        'age': 28,
        'salary': 4700000
    },
    {
        'name': 'Carlos',
        'age': 35,
        'salary': 5200000
    }
]


def process(input: list) -> list:
    select: list = []

    for i in input:
        if i['salary'] > 4500000:
            select.append(i['name'])

    return select

print(process(dic))

# anotaciones y validaciones en clases

class calculator:
    num1: float
    num2: float
    def __init__(self, num1:float, num2:float):
        # hago validacion de tipo con if e isinstance esto garantiza el buen fucninamiento de la clase
        if not isinstance(num1, float) and not isinstance(num2, float):
            # En este caso con la palabra reservada raise puede llamar a una excepcion de python para señalar el error
            # La palabra reservada raise se utiliza para eso, para disparar excepciones
            raise TypeError("El tipo de dato es incorrecto")
            #print("ERROR: !")
            # Cuando se utiliza raise ya no es necesario el return porque el raise detiene la ejecucion del bloque de codigo
            #return None
        self.num1=num1
        self.num2=num2
    
    def divide(self) -> float:
        if self.num2 == 0:
            print("ERROR: !")
            return None
        return self.num1/self.num2
    
    def multiply(self) -> float:
        return self.num1*self.num2
    
    def sum(self) -> float:
        return self.num1+self.num2
    
    def sus(self) -> float:
        return self.num1-self.num2
    


calc = calculator(10.0,4.0)

#ejemplo de uso
# en este caso se utiliza try and except para manejar la informacion adicional del erro

#calc2 = calculator(2,4)

#Con try and except you puedo personalizar mejor la excepcion que salta y captura desde la ejecucion del codigo
try:
    calc3 = calculator(4,6)
except TypeError as e:
    print(f"El numero ingresado debe ser flotante {e}")