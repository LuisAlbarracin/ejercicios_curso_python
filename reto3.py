"""
    Modifica el iterador que acabamos de
    crear, pero que en lugar de devolver los
    inifitos números de la Sucesión de
    Fibonacci solo devuelva los números
    hasta un máximo. Una vez que esto pase,
    eleva el error StopIteration
"""

import time


class FiboIter:

    def __init__(self, maximo=10):
        self.max = maximo

    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self

    def __next__(self):
        if self.counter < self.max:
            if self.counter == 0:
                self.counter += 1
                return self.n1
            elif self.counter == 1:
                self.counter += 1
                return self.n2
            else:
                self.aux = self.n1 + self.n2
                self.n1, self.n2 = self.n2, self.aux
                self.counter += 1
                return self.aux
        else:
            raise StopIteration

if __name__ == "__main__":
    fibonacci = FiboIter()
    for element in fibonacci:
        print(element)
        time.sleep(1)
