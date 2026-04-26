def karatsuba(x, y):
    if x < 10 or y < 10: return x*y
    n = max(len(str(x)), len(str(y)))//2
    a, b = divmod(x, 10**n)
    c, d = divmod(y, 10**n)
    ac, bd = karatsuba(a,c), karatsuba(b,d)
    abcd = karatsuba(a+b, c+d) - ac - bd
    return ac*10**(2*n) + abcd*10**n + bd

print(karatsuba(1234, 5678))
