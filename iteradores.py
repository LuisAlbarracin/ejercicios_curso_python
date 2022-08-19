"""
    Una estructura de datos para
    guardar datos infinitos
"""

my_list = [1, 2, 3, 4, 5]
my_iter = iter(my_list)
# Iterando un iterador
print(my_iter)
# Cuando no quedan datos, la excepción StopIteration es elevada

while True:
    try:
        element = next(my_iter)
        print(element)
    except StopIteration:
        break

for element in my_list:
    print(element)
