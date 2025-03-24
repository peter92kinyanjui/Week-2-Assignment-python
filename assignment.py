my_list = [10,20,30,40]
my_list[1]=15
list1 = [50,60,70]
my_list.extend(list1)
del(my_list[-1])
my_list.sort()
print(f'The index of value 30 in my_list is : {my_list.index(30)}')

