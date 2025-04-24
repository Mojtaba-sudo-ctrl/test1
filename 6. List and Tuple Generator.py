numbers_list = []
numbers_tuple = ()
numbers = input("please enter the numbers seperated with comma without space: ")
numbers_list = numbers.split(',')
numbers_tuple = tuple(numbers_list)
print(numbers_list)
print(numbers_tuple)