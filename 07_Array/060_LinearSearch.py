# Linear search

def search(arr,key):
    for i in arr:
        if i == key:
            return True
    return False

arr = [5,7,-2,10,22,-2,8,5,22,1]
print('Enter the element to search for ',end='')
key = int(input())

found = search(arr,key)
if found:
    print('key is present')
else:
    print('key is absent')
