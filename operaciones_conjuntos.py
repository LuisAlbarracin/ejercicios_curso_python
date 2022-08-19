my_set1 = {3, 4, 5}
my_set2 = {5, 6, 7}

# union
my_set3 = my_set1 | my_set2
print(my_set3)

# Interseccion
my_set3 = my_set1 & my_set2
print(my_set3)

# Diferencia
my_set3 = my_set1 - my_set2
print(my_set3)

# Diferencia
my_set3 = my_set2 - my_set1
print(my_set3)

# Diferencia simetrica contrario a la interseccion
my_set3 = my_set1 ^ my_set2
print(my_set3)

my_set1.union(my_set2)
my_set1.symmetric_difference(my_set2)
my_set1.difference(my_set2)
my_set1.intersection(my_set2)
