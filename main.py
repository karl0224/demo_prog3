def restar(x, y):
    return x - y

def multiplicacion(x, y):
    return x * y

def division(x, y):
    if y == 0:
        return 0
    else:
        return x / y

def potenciacion(x, y):
    return x ** y

multiplica = multiplicacion(5, 7)
print(multiplica)

resultado = restar(7, 5)
print("CAMBIO",+str(resultado))