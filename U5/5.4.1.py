requested_toppings = ['mushrooms','green peppers','extra cheese']
for requested_topping in requested_toppings:
    print("Adding"+requested_topping+".")
print("\nFinished making your pizza!")
#然而，如果比萨店的青椒用完了，该如何处理呢？为妥善地处理这种情况，可在for循环中包含一条if语句：
requested_toppings = ['mushrooms','green peppers','extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry,we are out of green peppers right now")
    else:
        print("Adding "+requested_topping+".")
print("\nFinished making your pizza!")