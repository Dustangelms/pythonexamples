def generator1():
    yield 1
    yield 2
    yield 3


print('==')
for i in generator1():
    print(i)


def generator2(stop):
    ls = [ 1, 2, 3 ]
    for l in ls:
        if l == stop:
            return
        yield l


print('==')
for i in generator2(None):
    print(i)
print('==')
for i in generator2(3):
    print(i)