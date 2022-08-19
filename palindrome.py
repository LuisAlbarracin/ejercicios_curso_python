def is_palindrome(nombre: str) -> bool:
    nombre = nombre.replace(" ", "").lower()
    return nombre == nombre[::-1]


def run():
    print(is_palindrome('sandra'))


if __name__ == '__main__':
    run()
