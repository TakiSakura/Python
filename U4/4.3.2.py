numbers=list(range(1,6))
print(numbers)
#指定步长
even_numbers=list(range(2,11,2))
print(even_numbers)
#乘方运算
squares=[]
for value in range(1,11):
    square=value**2
    squares.append(square)
print(squares)
#让代码更简洁
for value in range(1,11):
    squares.append(value**2)
print(squares)