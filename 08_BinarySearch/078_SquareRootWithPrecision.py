def morePrecision(n,precision,ans):
    increment = 0.1
    for i in range(0, precision):
        while (ans * ans <= n):
            ans += increment
 
        ans = ans - increment
        increment = increment / 10
    return ans

def sqrtN(n,precision):
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
    # return ans
    # print(ans)
    pricise = morePrecision(n,precision,ans)
    return pricise
        

if __name__ == "__main__":
    testcase = int(input())
    for _ in range(testcase):
        n = int(input())
        precision = int(input())
        ans = sqrtN(n,precision)
        print(ans)
