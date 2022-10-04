# print -     A B C
#             B C D
#             C D E

n = int(input())
for i in range(1,n+1):
    a = ord('A') + i - 1
    for j in range(n):
        print(chr(a),end=' ')
        a = a + 1
    print()

