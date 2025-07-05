"""
Implementar un sistema de gestion de pedidos utilizando collection y enumerations
llevar un registro de los productos que tenemos (defaultdict)
llevar una enumeracion para tener el estado de la orden (enum)
"""

from collections import defaultdict
from enum import Enum
from collections import deque

class OrderStatus(Enum):
    BASE = 0
    PENDING = 1
    SHIPPED = 2
    DELIVERED = 3

class Shop:
    inventary: list
    def __init__(self, inventary: list):
        self.inventary = inventary


    def Get_Inventary(self) -> defaultdict:
        # creo el defaultdict
        invent = defaultdict(int)
        if not isinstance(self.inventary, list) or not all(isinstance(item, str) for item in self.inventary):
            raise TypeError("El inventario no es una lista o no tiene elementos correctos")
        # hago el conteo del inventario
        for item in self.inventary:
            invent[item] += 1
        return invent

    def set_inventary(self, shop: list[str]) -> list:
        if not isinstance(shop, list) or not all(isinstance(item, str) for item in shop):
            raise TypeError("El inventario no es una lista o no tiene elementos correctos")
        invent = deque(self.inventary)
        for item in shop:
            try:
                invent.remove(item)
            except ValueError as e:
                return [False, e]
        self.inventary = list(invent)
        return [True, 'Compa exitosa!']

    def Add_Inventary(self, Nitems: list[str]) -> list:
        if not isinstance(Nitems, list) or not all(isinstance(item, str) for item in Nitems):
            raise TypeError("El nuevo set no es una lista o no tiene elementos correctos")
        invent = deque(self.inventary)
        for item in Nitems:
            invent.appendleft(item)
        self.inventary = list(invent)
        return [True, 'Inventario cambiado']


class Customer:
    shop: Shop
    order_status: OrderStatus

    def __init__(self, shop: Shop, orderS: OrderStatus):
        self.shop = shop
        self.order_status = orderS

    def Shoping(self, products: list[str]):
        if not self.shop.set_inventary(products)[0]:
            print(self.shop.set_inventary(products)[1])
        self.order_status = OrderStatus.PENDING

    def Get_status(self):
        print(self.order_status)

    def Set_status(self):
        if not self.order_status >= 0 and not self.order_status <= 3:
            print('Error! la orden ya fue entregada')
        self.order_status += 1
        print("Orden status cambiado!")


# creo el mercado
invetario = ["Vaso1","Vaso1","Vaso1","Vaso2","Vaso2","Vaso3","Vaso3","Vaso3"]
botRec = Shop(invetario)

#Consultar inventario
print(botRec.Get_Inventary())

# Agregar productos
botRec.Add_Inventary(["Vaso1","Vaso1","Vaso1"])
#Consultar inventario
print(botRec.Get_Inventary())

#defino un cliente
Hugo = Customer(botRec, OrderStatus.BASE)

Hugo.Shoping(["Vaso1"])
Hugo.Shoping(["Vaso1","Vaso2"])

Hugo.Get_status

#Consultar inventario
print(botRec.Get_Inventary())


    
