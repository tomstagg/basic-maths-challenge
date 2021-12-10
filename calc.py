import random
from type import Question


def _add(x, y):
    return x + y


def _multiply(x, y):
    return x * y


def _add_digits(setup):
    return Question(random.randint(0, setup['maxNumber']), random.randint(0, setup['maxNumber']), '+')


def _multiply_digits(setup):
    return Question(random.randint(0, 12), random.choice(setup['timesTables']), 'X')


dispatcher = {'add': {'calc': _add, 'get_digits': _add_digits},
              'multiply': {'calc': _multiply, 'get_digits': _multiply_digits}}


def get_result(x, y, func):
    try:
        return dispatcher[func]['calc'](x, y)
    except:
        raise Exception('invalid function')


def get_digits(setup):
    challenge = setup['challenge']
    try:
        return dispatcher[challenge]['get_digits'](setup)
    except:
        raise Exception('invalid function')


if __name__ == '__main__':
    print(get_result(2, 3, 'add'))
    print(get_result(2, 3, 'multiply'))
    get_digits()
