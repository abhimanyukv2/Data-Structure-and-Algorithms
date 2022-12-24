'''Write a short Python program that takes two arrays a and b of length n storing int values, and returns the dot product of a and b. That is, it returns an array c of length n such that c[i] = a[i] ·b[i], 
for i = 0, . . . , n −1.'''

def dotProduct(vectorA, vectorB, n):
    vectorC = []
    for i in range(n):
        vectorC.append(vectorA[i]*vectorB[i])
    return vectorC

n = int(input())
vectorA = list(map(int, input().split()))
vectorB = list(map(int, input().split()))
ans = dotProduct(vectorA, vectorB, n)
print(ans)