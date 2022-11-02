'''Yiu are given a positive integer N.
Your task is to find and return its square root.
Is N is not a perfect square, then return floor value of sqrt(N).'''

def sqrtN(n):
    start = 0
    end = n
    ans = 0

    while start <= end:
        mid = start + (end - start)//2
        square = mid*mid
        # print(mid)
        if square == n:
            return mid
        elif square < n:
            ans = mid
            start = mid + 1
        elif square < n:
            start = mid + 1
        elif square > n:
            end = mid - 1
    return ans

if __name__ == "__main__":
    testCase = int(input())
    for _ in range(testCase):
        N = int(input())
        ans = sqrtN(N)
        print(ans)