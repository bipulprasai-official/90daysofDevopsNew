# Question: Given a list my_list = [1, 2, 3, 4, 5], 
# write the code to create a new list containing elements from index 1 to 3 (inclusive).

# Below is for Slicing in Python
my_list = [1, 2, 3, 4, 5]
newList = my_list[0:4]
newListNegative = my_list[:-2] #opposite way of slicing or from back
# print(newListNegative)

# below is for append in python
my_list.append(6)
# print(my_list)

# inserting in python
my_list.insert(6,2.6)
# print(my_list)

# removing in python
my_list.remove(3)
# print(my_list)

# removing in python
my_list.pop(5)
# print(my_list)

# length in python

lengthofstring = len(my_list)
print(my_list)
print(lengthofstring)