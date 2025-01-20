def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def gcd(a , b):
    while b:
        a, b = b, a%b
    return a
a = 48
b = 18
print(f"The LCM of {a} and {b} is: {lcm(a, b)}")
