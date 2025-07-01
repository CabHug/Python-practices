import json

#LEctura de una JSON file
"""
#Lectura del archivo
with open('data.json', mode='r') as file:
    products = json.load(file)

#mostrar el contenido
for product in products:
    #print(product)
    print(f"Producto {product['name']}, precio {product['price']}")
"""

#Escrituta de un JSON file
register = {
        "name": "Wireless Charger",
        "price": 20,
        "quantity": 100,
        "brand": "ChargeMaster",
        "category": "Accessories",
        "entry_date": "2024-07-01"
    }

with open('data.json', mode='r') as file:
    json_file = json.load(file)

json_file.append(register)

with open('data.json', mode='w') as writeFile:
    json.dump(json_file, writeFile, indent=4)