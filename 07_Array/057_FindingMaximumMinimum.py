# finding maximum and minimum element of an array

# using function
def getMax(num):
    maxi = num[0]
    for i in range(1,len(num)):
        if num[i] > maxi:
            maxi = num[i]
    return maxi

def getMin(num):
    mini = num[0]
    for i in range(1,len(num)):
        if num[i] < mini:
            mini = num[i]
    return mini


size = int(input())
num = []
for i in range(size):
    num.append(input())

# using in-built function
minimum = min(num)
maximum = max(num)

print('minimum value of arr is',minimum)
print('maximim value of arr is',maximum)


print('maximum element of an array is',getMax(num))
print('minimum element of an array is',getMin(num))