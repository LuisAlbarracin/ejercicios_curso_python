def main():
    a = 1

    def nested():
        print(a)

    return nested


my_func = main()
my_func()

del main
my_func()

# Reglas para encontrar un closure
# - Debemos tener una nested function
# - La nested function debe referenciar un valor de un scope superior
# - La funcion que envuelva a la nested function debe retornarla tambien