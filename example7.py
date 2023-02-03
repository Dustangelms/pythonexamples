def foo(a, b, c = 3, *d, e, **f):
    print(a)
    print(b + c)
    try:
        print(len(d), d[0], d[1])
    except Exception:
        pass
    print(e)
    try:
        print(f['main'])
    except Exception:
        pass


foo(1, 2, e = 5)
foo(1, 2, 3.0, 4, 4.1, e = 5, main = 6)