motorcycles=['honda','yamaha','suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)
#2.使用pop()删除元素
motorcycles=['honda','yamaha','suzuki']
print(motorcycles)
popped_motorcycle=motorcycles.pop()#pop()会修改列表的元素
print(motorcycles)
print(popped_motorcycle)
#根据值删除元素
motorcycles=['honda','yamaha','suzuki','ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)
#remove也可继续使用
motorcycles=['honda','yamaha','suzuki','ducati']
print(motorcycles)
too_expensive='ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA "+too_expensive.title()+" is too expensive for me.")
