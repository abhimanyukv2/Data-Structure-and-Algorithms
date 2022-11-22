'''Given an arry/list of length N, where the arry/list represent the
boards and each element of the given array/list represent the length
of each boards. Consider that each unit of a boards takes 1 unit of
time to paint.
You are supposed to return the area of the minimum time to get this
job done of painting all the N boards under a constraint that any
painter will only paint the continuous of boards.'''


def largestMinDistance(arr, numberOfBoards, numberOfPainters):
    totalNumberOfBoards = sum(arr)
    start = 0 
    end = totalNumberOfBoards
    ans = -1

    while start <= end:
        mid = start + (end - start)//2

        if isPossible(arr, numberOfBoards, numberOfPainters, mid):
            ans = mid
            end = mid - 1
        else:
            start = mid + 1
    return ans

def isPossible(arr, numberOfBoards, numberOfPainters, mid):
    PaintersCount = 1
    boardSum = 0

    for i in range(numberOfBoards):
        if boardSum + arr[i] <= mid:
            boardSum += arr[i]
        else:
            PaintersCount += 1
            if PaintersCount > numberOfPainters or arr[i]> mid:
                return False
            
            boardSum = arr[i]
    return True


if __name__ == "__main__":
    testCase = int(input())
    for _ in range(testCase):
        numberOfBoards, numberOfPainters = map(int,input().split())
        arr = list(map(int,input().split()))

        ans = largestMinDistance(arr, numberOfBoards, numberOfPainters)
        print(ans)