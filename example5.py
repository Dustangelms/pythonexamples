a = 1
b = 2
if a < b: print('1: This is fine')
else: print('1: This is not fine')

print('2: This is fine' if a < b else '2: This is not fine')

if a == b:
    print('Case 1')
elif a + 1 == b:
    print('Case 2')
else:
    print('Case whatever')

if None: print('3: This is fine')
else: print('3: This is not fine')

if 0: print('4: This is fine')
else: print('4: This is not fine')


def cycle(i):
    for a in range(0, i):
        print(a)
        if a % 2 == 0:
            print('is even')
    else:
        print(42)


cycle(3)
cycle(0)

array = [0, 1, 2]
array_iterator = iter(array)
print(next(array_iterator))
print(next(array_iterator))
print(next(array_iterator))
print(next(array_iterator))

while True:
    a = input('Say quit to quit:')
    if a == 'quit':
        break
else:
    print('Didn\'t happen')


def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    return a / b


switch = {
    '+': addition,
    '-': subtraction,
    '*': multiplication,
    '/': division
}
operation = input('Operation:').split(' ')
print('Result = ' + switch[operation[1]](int(operation[0]), int(operation[2])))

switch = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b
}
operation = input('Operation:').split(' ')
print('Result = ' + switch[operation[1]](int(operation[0]), int(operation[2])))
