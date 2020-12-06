from pytest import fixture


@fixture(scope='class')
def list_numbers90():
    return [item for item in range(1, 91)]


@fixture(scope='class')
def list_numbers_used():
    return [item for item in range(21, 91)]


@fixture(scope='class')
def list_numbers10():
    return [2, 3, 0, 5, 0, 10, 56, 0, 19]
