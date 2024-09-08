def isPwrOf2(n):
    if n <= 0: return False
    if n == 1: return True
    if n%2 == 0: return isPwrOf2(n/2)
    return False

print("It's a power of two: " + str(isPwrOf2(16)))
print("It's a power of two: " + str(isPwrOf2(32)))
print("It's a power of two: " + str(isPwrOf2(64)))
print("It's a power of two: " + str(isPwrOf2(256)))
print("It's a power of two: " + str(isPwrOf2(65536)))
print("It's a power of two: " + str(isPwrOf2(73291)))