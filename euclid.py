a = 24342
b = 2523

def euclid(a, b):
    return (b if (a % b == 0) else euclid(b, a % b))

print(euclid(a, b))