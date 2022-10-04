# Scope of the array

def update(arr):
    print('Inside the function')
    # updating the array first element
    arr[0] = 120 
    for i in arr:
        print(i,end=' ')
    print('Going back to the main function')

arr = [1,2,3]
update(arr)

# printing the array
for i in arr:
    print(i,end=' ')
