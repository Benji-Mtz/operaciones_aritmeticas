import operator

ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.floordiv,
}
def plus(val):
    return [val, '+']

def minus(val):
    return [val, '-']

def times(val):
    return [val, '*']

def divided_by(val):
    return [val, '/']


def zero(func = None):
    default_value = 0
    if func == None:
        return default_value
    
    value = func[0]
    symbol = func[1]
    if symbol == '/' and value == 0:
        print("No se puede dividir por cero")
    else:
        operacion = ops[symbol](default_value,value)
        print(operacion)
    
def one(func = None): 
    default_value = 1
    if func == None:
        return default_value
    
    value = func[0]
    symbol = func[1]
    if symbol == '/' and value == 0:
        print("No se puede dividir por cero")
    else:
        operacion = ops[symbol](default_value,value)
        print(operacion)

def two(func = None):
    default_value = 2
    if func == None:
        return default_value
    
    value = func[0]
    symbol = func[1]
    if symbol == '/' and value == 0:
        print("No se puede dividir por cero")
    else:
        operacion = ops[symbol](default_value,value)
        print(operacion)
    
def three(func = None):
    default_value = 3
    if func == None:
        return default_value
    
    value = func[0]
    symbol = func[1]
    if symbol == '/' and value == 0:
        print("No se puede dividir por cero")
    else:
        operacion = ops[symbol](default_value,value)
        print(operacion)
    
def four(func = None):
    default_value = 4
    if func == None:
        return default_value
    
    value = func[0]
    symbol = func[1]
    if symbol == '/' and value == 0:
        print("No se puede dividir por cero")
    else:
        operacion = ops[symbol](default_value,value)
        print(operacion)
    
def five(func = None):
    default_value = 5
    if func == None:
        return default_value
    
    value = func[0]
    symbol = func[1]
    if symbol == '/' and value == 0:
        print("No se puede dividir por cero")
    else:
        operacion = ops[symbol](default_value,value)
        print(operacion)
    
def six(func = None):
    default_value = 6
    if func == None:
        return default_value
    
    value = func[0]
    symbol = func[1]
    if symbol == '/' and value == 0:
        print("No se puede dividir por cero")
    else:
        operacion = ops[symbol](default_value,value)
        print(operacion)
    
def seven(func = None):
    default_value = 7
    if func == None:
        return default_value
    
    value = func[0]
    symbol = func[1]
    if symbol == '/' and value == 0:
        print("No se puede dividir por cero")
    else:
        operacion = ops[symbol](default_value,value)
        print(operacion)
    
def eight(func = None):
    default_value = 8
    if func == None:
        return default_value
    
    value = func[0]
    symbol = func[1]
    if symbol == '/' and value == 0:
        print("No se puede dividir por cero")
    else:
        operacion = ops[symbol](default_value,value)
        print(operacion)
    
def nine(func = None):
    default_value = 9
    if func == None:
        return default_value
    
    value = func[0]
    symbol = func[1]
    
    if symbol == '/' and value == 0:
        print("No se puede dividir por cero")
    else:
        operacion = ops[symbol](default_value,value)
        print(operacion)

four(times(five())) # imprime 20
one(plus(eight())) # imprime 9
seven(minus(three())) # imprime 4
nine(divided_by(three())) # imprime 3

nine(divided_by(zero())) # Exception
eight(divided_by(zero())) # Exception
seven(divided_by(zero())) # Exception
six(divided_by(zero())) # Exception
five(divided_by(zero())) # Exception
four(divided_by(zero())) # Exception
three(divided_by(zero())) # Exception
two(divided_by(zero())) # Exception
one(divided_by(zero())) # Exception
zero(divided_by(zero())) # Exception