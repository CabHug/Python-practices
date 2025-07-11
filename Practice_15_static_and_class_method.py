class Order():
    global_discount = 10

    def __init__(self, monto):
        self.monto = monto
        
    @classmethod
    def set_monto(cls, n_monto):
        cls.monto = n_monto

    @classmethod
    def get_monto(cls):
        return cls.monto
    
    @classmethod
    def set_global_discount(cls, n_discount):
        cls.global_discount = n_discount

    @classmethod
    def get_global_discount(cls):
        return cls.global_discount
    
    @staticmethod
    def calculate(num1, num2):
        return num1+num2
    

# Las bondades de usar staticmethod y classmethos es la capacidad de interactuan con los metodos sin necesidad de
# crear una instancia de la clase

#-> staticmethod me permite interactias con los atributos de la clase que no tienen relacionado los parametros self o cls
# y tener su resultado

#-> staticmethod me permite llamar a un metodo pero sin cencesidad de crear una instancia de clase, este metodo no tiene relacionado un self o cls
# es decir no afecta directamente a la clase

Order.set_monto(12)
print(Order.get_monto())

print(Order.calculate(5,2))



