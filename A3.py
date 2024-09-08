def isPwrOf4(n):
    if n <= 0: return False
    if n == 1: return True
    if n%4 == 0: return isPwrOf4(n/4)
    return False

print("It's a power of four: " + isPwrOf4(16))
print("It's a power of four: " + isPwrOf4(32))
print("It's a power of four: " + isPwrOf4(64))
print("It's a power of four: " + isPwrOf4(256))
print("It's a power of four: " + isPwrOf4(65536))
print("It's a power of four: " + isPwrOf4(73291))