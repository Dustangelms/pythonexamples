def fibo_generator():
    a, b = 0, 1
    yield 0
    yield 1
    while True:
        a = a + b
        yield a
        b = a + b
        yield b


fibo_lowest_exclusive_bound = int(input('Введите число:'))
for fibo in fibo_generator():
    if fibo > fibo_lowest_exclusive_bound:
        print('Минимальное число Фибоначчи, превышающее ' + str(fibo_lowest_exclusive_bound) + ', равняется ' + str(fibo) + '.')
        break
