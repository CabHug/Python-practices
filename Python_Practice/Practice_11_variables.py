dic = [{
    'name': 'Hugo',
    'age': 31,
    'salary': 5000000
    },
    {
    'name': 'Andres',
    'age': 31,
    'salary': 4500000    
    }
    ]

def evaluate(dic):
    selec = []
    def process():
        nonlocal dic, selec
        
        for i in dic:
            if i['salary'] > 3500000:
                selec.append(i['name'])
    
    process()
    print(selec)

evaluate(dic)
