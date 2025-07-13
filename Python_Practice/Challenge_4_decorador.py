def log_employee_action(func):
    def wrapper(self):
        result = func(self)
        with open('log.txt', mode='a') as file:
            file.writelines(result)
    return wrapper

class employee:
    info: dict
    def __init__(self, info: dict):
        self.info = info
        
    @log_employee_action
    def greet(self):
        print(f"Hi every one, my name is {self.info['name']}")
        return f"{self.info['name']} has greeted \n"
    
    @log_employee_action
    def dimiss(self):
        print("Bye every one")
        return f"{self.info['name']} has dimissied \n"
Hugo = employee({
    'name': 'Hugo'
})

Hugo.greet()
Hugo.dimiss()
