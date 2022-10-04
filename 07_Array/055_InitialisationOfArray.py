# Initialisation of array in python

# in python array can be impliment using list and
# you can stre any type of data in list
# size of the list can be automatically calulate by pyhton 
# we do not have to declare the size of list

# method - 1 -using loop
# In python we can initialize an array with any type of element
arr1 = []
number1 = int(input())
value1 = int(input())
arr1 = [value1 for i in range(number1)]
print(arr1)

# method - 2 - Direct Method
value2 = input()
number2 = int(input())
arr2 = [value2]*number2
print(arr2)

# Accessing an element in the array
second = [5,7,11]
print("value at index 2",second[2])

# printing the array
for i in second:
    print(i)
n=3
for i in range(3):
    print(second[i])