def square(x):
    return x**2


print(square(5))

result = (lambda x: x**2)(7)
print(result)

result1 = (lambda x, y: x + y)(2, 3)
print(result1)

a = 5
b = 10
c = 30
result2 = (lambda a, b, c: a + b + c)(a, b, c)
print(result2)
