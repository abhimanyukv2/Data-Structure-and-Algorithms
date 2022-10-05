'''You are given  an array/list consisting of N integers.
Your task is to find all the distinct triplets present in the array
which adds up to a given number K.
An array is said to have a triplet {arr[i],arr[j],arr[k]} with sum = K
If there exists three indices i, j and k such that 
i != j, j != k, k != j and arr[i]+arr[j]+arr[k] = K'''

def tripletSum(arr,n,K):
    arr.sort()
    triplet = []
    for i in range(n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                summ = arr[i]+arr[j]+arr[k]
                if summ == K:
                    temp = []
                    temp.append(arr[i])
                    temp.append(arr[j])
                    temp.append(arr[k])
#                     temp.sort()
#                     if temp not in triplet:
                    triplet.append(temp)
    triplet1 = [list(x) for x in set(tuple(t) for t in triplet)]
    return triplet1

def findTriplet(arr,n,K):
    arr.sort()
    triplet = []
    for i in range(n-2):
        if i==0 or i>0 and arr[i] != arr[i-1]:
            low = i + 1
            high = n - 1
            while low<high:
                if arr[low]+arr[high]+arr[i] == K:
                    temp = []
                    temp.append(arr[low])
                    temp.append(arr[high])
                    temp.append(arr[i])
                    triplet.append(temp)
                    while low<high and arr[low] == arr[low+1]:
                        low = low + 1
                    while low<high and arr[high] == arr[high-1]:
                        high = high - 1
                    high = high - 1
                    low = low + 1
                elif arr[low]+arr[high]+arr[i]<K:
                    low = low + 1
                else:
                    high = high - 1
    return triplet


if __name__ == "__main__":
    testCase = int(input())
    for _ in range( testCase):
        n = int(input())
        arr = list(map(int,input().split()))
        k = int(input())

        ans = tripletSum(arr,n,k)
        print(ans)