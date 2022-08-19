"""
    Función que recibe como
    parámetro otra función, le
    añade cosas, y retorna una
    función diferente.
"""


def decorador(func):
    def envoltura():
        print('Esto se añade a mi función original')
        func()

    return envoltura


def saludo():
    print('Hola!')


saludo()
# Output
# > Hola!

saludo = decorador(saludo)
saludo()
# Output
# > Esto se añade a mi función original
# > Hola!
