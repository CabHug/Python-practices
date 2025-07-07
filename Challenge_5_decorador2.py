def check_cred(cargo, boss_id):
    def decorador(function):
        def wrapper(self, emp_id):
            boss = next((emp for emp in self.employees if emp['id'] == boss_id), None)
            if boss:
                print(boss)
                if boss['cargo'] == cargo:
                    function(self, emp_id)
                else:
                    print(f"El encargado {boss['nombre']} no tiene los permisos")
            else:    
                print("El encargado no fue encontrado")
        return wrapper
    return decorador

class business:
    employees: list
    def __init__(self, employees: list):
        self.employees = employees

    @check_cred('ops', 1)
    def remove_employee(self, emp_id):
        for i, item in enumerate(self.employees):
            if item['id'] == emp_id:
                print(f"El empleado {item['nombre']} fue eliminado.")
                del self.employees[i]
                return None
            
        print(f"No se encontro el empleado con id: {emp_id}")
                


empleados = [
    {'id': 1, 'nombre': 'Ana Martínez', 'cargo': 'ops', 'salario': 4500},
    {'id': 2, 'nombre': 'Carlos Gómez', 'cargo': 'Analista de Datos', 'salario': 4200},
    {'id': 3, 'nombre': 'Lucía Torres', 'cargo': 'Diseñadora UX/UI', 'salario': 4000},
    {'id': 4, 'nombre': 'Miguel Rojas', 'cargo': 'Administrador de Sistemas', 'salario': 4700},
    {'id': 5, 'nombre': 'Sofía Ramírez', 'cargo': 'Gerente de Proyecto', 'salario': 6000}
]


AMM = business(empleados)

AMM.remove_employee(3)
AMM.remove_employee(3)

print(AMM.employees)