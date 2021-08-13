def f(x):
    return x + f(x - 1)
print(f(100))