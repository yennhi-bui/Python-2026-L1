def get_divisors(n):
    out = []
    for i in range(1, n+1):
        if n % i == 0:
            out += [i]
    return out
print(get_divisors(100))