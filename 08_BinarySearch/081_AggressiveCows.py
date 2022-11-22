'''Given an array of length N, where each elements denotes the
positions of a stall. Now you have N stalls and an integer K which denotes
the number of cows that are aggressive. To prevent the cows from hurting
each other, you need to assign the cows to the stalls, such that the
minium distance between any two of them is as large as possible.
Return the largest minimum distance.'''

def largestMinimumDistance(numberOfStall, numberOfAggressiveCows, positionOfStall):
    positionOfStall.sort()
    start = 0
    end = positionOfStall[-1]
    ans = -1

    while start <= end:
        mid = start + (end - start)//2

        if isPossible(numberOfStall, numberOfAggressiveCows, positionOfStall, mid):
            ans = mid
            start = mid + 1
        else:
            end = mid - 1
    
    return ans

def isPossible(numberOfStall, numberOfAggressiveCows, positionOfStall, mid):
    cowCount = 1
    lastPosition = positionOfStall[0]

    for i in range(len(positionOfStall)):
        if positionOfStall[i] - lastPosition >= mid:
            cowCount += 1
            
            if cowCount == numberOfAggressiveCows:
                return True
            lastPosition = positionOfStall[i]

    return False


if __name__ == "__main__":
    testCase = int(input())
    for _ in range(testCase):
        numberOfStall, numberOfAggressiveCows = map(int, input().split())
        positionOfStall = list(map(int,input().split()))

        ans = largestMinimumDistance(numberOfStall, numberOfAggressiveCows, positionOfStall)
        print(ans)
