def factorial(n):
    if n > 1:
        return n * factorial(n-1)
    elif n == 1 or n == 0:
        return 1
    elif n < 0:
        return "wrong number"
print(factorial(5))
print(factorial(4))
print(factorial(-1))