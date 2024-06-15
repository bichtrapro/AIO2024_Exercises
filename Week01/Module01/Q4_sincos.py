import math
#sin
def approx_sin(x, n):
    result = 0
    for i in range(n):
        coeff = (-1) ** i
        num = x ** (2 * i + 1)
        denom = math.factorial(2 * i + 1)
        term = coeff * (num / denom)
        result += term
    return result
#cos 
def approx_cos(x, n):
    result = 0
    for i in range(n):
        coeff = (-1) ** i
        num = x ** (2 * i)
        denom = math.factorial(2 * i)
        term = coeff * (num / denom)
        result += term
    return result

#sinh
def approx_sinh(x, n):
    result = 0
    for i in range(n):
        num = x ** (2 * i + 1)
        denom = math.factorial(2 * i + 1)
        term = (num / denom)
        result += term
    return result

#cosh
def approx_cosh(x, n):
    result = 0
    for i in range(n):
        num = x ** (2 * i)
        denom = math.factorial(2 * i)
        term = (num / denom)
        result += term
    return result

print(approx_sin(x=3.14,n=10))
print(approx_cos(x=3.14,n=10))
print(approx_sinh(x=3.14,n=10))
print(approx_cosh(x=3.14,n=10))
