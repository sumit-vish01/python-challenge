import datetime
birthday = datetime.date(1959, 7, 15)
print(birthday.day)
print(birthday.month)
print(birthday.year)


def add(a , b):
    result = a + b
    print(f'Adding {a} and {b} gives {result}')
    return result

import pdb
def divide(a, b):
    pdb.set_trace()
    return a / b

print(divide(10, 2))

def divide(a, b):
    result = a / b
    return result

print(divide(10, 2))
print(divide(15, 3))