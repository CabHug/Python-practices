import numpy as np

# Paso 1: Crear arrays con datos de ventas mensuales
meses = np.array(['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
                  'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'])
ventas_A = np.array([150, 200, 250, 300, 220, 210, 180, 190, 230, 240, 280, 300])
ventas_B = np.array([180, 210, 230, 250, 270, 260, 240, 250, 270, 290, 310, 330])
ventas_C = np.array([200, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400, 420])

# Paso 2: Estadistica basica
def statistic_analysis(product, array):
    print(f"--> Statistic analysis for {product} <--")
    print(f"{product} median sales: {array.mean()}")
    print(f"{product} total sales: {array.sum()}")
    
input = [['Product_A',ventas_A], ['Product_B',ventas_B], ['Product_C',ventas_C]]
for p, v in input:
    statistic_analysis(p, v)

# Paso 3: Manipulacion y analisis de datos
sales_matrix = np.vstack((ventas_A, ventas_B, ventas_C))
invert_SM = sales_matrix.T
#print("Sales Matrix:\n",sales_matrix)
#print("Invert sales Matrix:\n",invert_SM)

total_sales = np.array([f.sum() for f in invert_SM], dtype=int)
total_sales_nonth = np.vstack((meses, total_sales))
#print(total_sales_nonth)
print("""
----------o----------
Total sales per month
""")
for m, t in total_sales_nonth.T:
    print(f"Total sales on {m}: {t}")


print("""
----------o----------
Max and Min sales month
""")

max = np.argmax(total_sales)
print(f"Max sales on month {total_sales_nonth[0,max]} is: {total_sales_nonth[1,max]}")

min = np.argmin(total_sales)
print(f"Max sales on month {total_sales_nonth[0,min]} is: {total_sales_nonth[1,min]}")

