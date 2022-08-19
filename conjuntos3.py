my_set = {1, 2, 3}
print(my_set)

# Añadir un elemento
my_set.add(4)
print(my_set)

# Añadir multiples
my_set.update([4, 5, 8])
print(my_set)

# Añadir multiples
my_set.update((1, 2, 9), {6, 10})
print(my_set)

# Borrar un elemento existente
my_set.discard(1)
print(my_set)

# Borrar un elemento existente
my_set.remove(2)
print(my_set)

# Borrar un elemento inexistente
my_set.discard(10)
print(my_set)

# Borrar un elemento inexistente
my_set.remove(12)
print(my_set)

# Borrar un elemento aleatorio
my_set.pop()
print(my_set)

# Limpiar el set
my_set.clear()
print(my_set)
