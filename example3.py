a = 0
print(b)


def b():
    print(a)
    c = 1
    d()


print(b)


def d():
    print(c)


print(a)
b()
e = d
f = 2
e()
f()
