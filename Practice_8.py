import json

with open('data.json', mode='r') as file:
    products = json.load(file)

#mostrar el contenido
for product in products:
    print(product)