a = True
a = False
a = not a

a = 0
a = 1 + 1
a = a + 1
a += 1
a = (1 - 2 + 3) * 4 // 5
a /= 6
a = int(a)
del a

a = 0.0
a = 1.4 + 1
a = a + 1
a += 1.6
a = (1 - 2 + 3) * 4 // 5
a = float(a)
a /= 6
del a

a = 0b10
a = 1 << 1 # 01 << 1 -> 010
a = -1 << 1 # 11 << 1 -> 110
a = 3 >> 1 # 011 >> 1 -> 01
a = -3 >> 1 # 101 >> 1 -> 10
a = 3 & 5 # 0011 & 0101 -> 0001
a = -3 & 5 # 1101 & 0101 -> 0101
a = 3 | 5 # 0011 & 0101 -> 0111
a = -3 | 5 # 1101 & 0101 -> 1101
a = 3 ^ 5 # 0011 ^ 0101 -> 0110
a = -3 ^ 5 # 1101 ^ 0101 -> 1000
a = ~1
a = ~-2
a = -2 & 255
a = 123455678901234567890
a >>= 1
a <<= 1
del a

a = 'c'
a = "c"
a = 'c\'d'
a = "c\'d"
a = "c'd"
a = 'c"d'
a = 'c' + 'd'
a *= 2
b = 'c' in a
b = "cd" in a
a, b = 'c', 'd'
del a, b

a = [ 1, 2 ]
b = a[0]
a[1] = 3.0
b = a[1]
a.append([ 4, 5 ])
a[1] = None
del a, b

a, *b = 1, 2, 3
del a, b

a = { 1, 2 }
a.add(2)
a.add('2')
a.remove(2)
a.add({ 3, 4 })
a.add(frozenset({ 3, 4 }))
b = { 1, 3 }
b &= a
b.add('3')
b |= a
del a, b

a = { 1: 2 }
b = a[0]
b = a.get(0)
a[1] = '2'
b = a[1]
del a[1]
del a, b