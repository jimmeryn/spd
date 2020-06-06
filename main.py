from jackson_test import jackson_test
from schrage_test import schrage_test, schrageWithDivisions_test
from carlier_test import carlier_test
from witi_test import witi_test


def test(i):
    switcher = {
        1: jackson_test,
        2: schrage_test,
        3: schrageWithDivisions_test,
        4: carlier_test,
        5: witi_test
    }
    func = switcher.get(i, lambda: 'Invalid')
    return func()


if __name__ == '__main__':
    test(int(input("Choose algorithm to test:\n\
        1: jackson_test,\n\
        2: schrage_test,\n\
        3: schrageWithDivisions_test,\n\
        4: carlier_test,\n\
        5: witi_test\n")))
