import sys
#Configuration data for store
dataConfig = {
    'name' : "Hugo's Store"
}
#Stock
stock = {
    'Snacks' : {
        'Chips Lays' : 2.2,
        'Snickers' : 3
        },
    'Drinks' : {
        'Coca-cola' : 3.2,
        'Pepsi' : 4
        },
    'Candies' : {
        'M&ms' : 2.3,
        'Snickers' : 4.1}
}
#Products
products = []

def readList(list):
  for key in list:
    print(f"{key}")
  print(f"Exit")

def cleanTxT(txt):
  return txt.lower().capitalize()

def listVal(item, list):
  if item not in list:
    print("Invalid option")
    sys.exit(1)

print(f"Welcome to {dataConfig['name']}")


flag_1 = True

while flag_1 == True:
  print("Please know our stock, choose one: ")
  readList(list(stock.keys()))

  in_1 = input("-> ")

  #Validation
  if cleanTxT(in_1) == "Exit":
    flag_1 = False

  if cleanTxT(in_1) not in list(stock.keys()):
    print("Invalid option")
    continue

  print(f"You have chosen: {cleanTxT(in_1)}")

  print(
"""
Please choose an option:
1. Choose a product.
2. Exit
""")
  in_2 = input("-> ")
  if in_2 == "1":
    print("Please choose a product:")
    readList(list(stock[cleanTxT(in_1)].keys()))
    in_3 = input("-> ")
    listVal(cleanTxT(in_3), list(stock[cleanTxT(in_1)].keys()))

    print(f"You have chosen: {cleanTxT(in_3)}")
    print("Please tipe the quantity of the product: ")
    in_4 = input("-> ")
    try:
      int(in_4)
    except:
      print("Invalid option")
      continue

    products.append({
      "name" : cleanTxT(in_3),
      "price" : stock[cleanTxT(in_1)][cleanTxT(in_3)],
      "quantity" : float(in_4)
    })



  else:
    flag_1 = False

print("Factura:")
print("Name - Quantity - Price")
value = 0
for product in products:
  value += product['price'] * product['quantity']
  print(f"{product['name']} - {product['quantity']} - {product['price']}")

print(f"Total: {value}")