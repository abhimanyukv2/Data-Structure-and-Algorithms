def factors1(n):
    result = []
    for k in range(1,n+1):
        if n%k == 0:
            result.append(k)
    return result

def factors2(n):
    for k in range(1,n+1):
        if n%k == 0:
            yield k

def factors3(n):
    k = 1
    while k*k < n:
        if n%k == 0:
            yield k
            yield n//k
        k += 1
    if k*k == n:
        yield k