
def remove_duplicates(some_list):
    my_list = list(set(some_list))
    return my_list


def run():
    random_list = [1, 1, 2, 2, 4]
    print(remove_duplicates(random_list))


if __name__ == '__main__':
    run()