def param_registro(action):
    def decorador(function):
        def wrapper(self, n_saldo):
            self._register(action)
            function(self, n_saldo)
        return wrapper
    return decorador

class bank:
    nombre: str
    saldo: float
    _n_cuenta: int
    __trans: list
    def __init__(self, name: str):
        self.nombre = name
        self.saldo = 0
        self._n_cuenta = 0
        self.__trans = []

    @param_registro('set saldo')
    def _set_saldo(self, n_saldo: float) -> str:
        try:
            if isinstance(n_saldo, float):
                self.saldo += n_saldo
                return "Cuenta actualizada con exito!"
            else:
                raise TypeError("Error tipo de dato incorrecto!")
        except TypeError as e:
            print(e)
    
    def get_saldo(self):
        print(self.saldo)

    def _register(self, action: str):
        self.__trans.append(action)

    def get_trans(self):
        print(self.__trans)


Hugo_acc = bank('Hugo')
print(Hugo_acc._set_saldo(12.0))
Hugo_acc.get_trans()
print(Hugo_acc._set_saldo(12.0))
Hugo_acc.get_trans()
Hugo_acc.get_saldo()



