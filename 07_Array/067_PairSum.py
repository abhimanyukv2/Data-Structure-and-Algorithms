'''You are give an integer array of size N and an integer S.
Your task is to return the list of all pairs of element
such that each sum of element of each pair equals S.'''

def pairSum(arr,n,s):
    arr.sort()
    pair = []
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            elif arr[i]+arr[j] == s:
                pair.append([arr[i],arr[j]])
    for i in pair:
        i.sort()
    printPair(pair)

def pairSum1(arr,n,s):
    ans = []
    for i in range(n-1):
        for j in range(i+1,n):
            if arr[i]+arr[j] == s:
                temp = []
                temp.append(min(arr[i],arr[j]))
                temp.append(max(arr[i],arr[j]))
                ans.append(temp)
    # temp.sort()
    ans.sort()
    printPair1(ans)

def printPair(pair):
    for i in range(len(pair)//2):
        print(*pair[i])
    
def printPair1(pair):
    for i in range(len(pair)//2):
        print(*pair[i])

if __name__ == "__main__":
    testCase = int(input())
    for _ in range(testCase):
        n = int(input())
        arr = list(map(int,input().split()))
        s = int(input())
        pairSum(arr,n,s)
        pairSum1(arr,n,s)