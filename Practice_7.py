import csv

#Leer como un diccionario
"""
with open('products.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(row)
"""
# Mostrar la informacion por columnas
"""
with open('products.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(f"producto {row['name']}, precio {row['price']}")
"""
# Añadir informacion a el docuemnto
"""
new_product = {
    'name': 'Wireless Charger',
    'price': 75,
    'quantity': 100,
    'brand': 'Master',
    'category': 'Accessories',
    'entry_date':'2024-06-30'
}

with open('products.csv', mode='a', newline='') as file:
    #file.write('\n')
    csv_writer = csv.DictWriter(file, fieldnames=new_product.keys())
    csv_writer.writerow(new_product)
"""

#Nueva columna
file_path = 'products.csv'
new_file = 'new_products.csv'

with open(file_path, mode='r') as file:
    csv_reader = csv.DictReader(file)
    # Obtener informacion de las columnas
    fieldNames = csv_reader.fieldnames + ['total_value'] + ['luxury']

    with open(new_file, mode='w', newline='') as updatedFile:
        csv_writer = csv.DictWriter(updatedFile, fieldnames=fieldNames)
        csv_writer.writeheader() # Metodo que escribe los encabezados

        for row in csv_reader:
            row['total_value'] = float(row['price']) * int(row['quantity'])
            if row['total_value'] >= 5000:
                row['luxury'] = 'True'
            else:
                row['luxury'] = 'False'
            csv_writer.writerow(row)