def sumar (*arg):
    sumar = arg[0]
    for value in arg[1:]:
        sumar += value
    return sumar

def restar (*arg):
    restar = arg[0]
    for value in arg[1:]:
        restar -= value
    return restar

def multiplicar (*arg):
    multiplicar = arg[0]
    for value in arg[1:]:
        multiplicar *= value
    return multiplicar

def dividir (n1, n2):
    return n1 / n2
