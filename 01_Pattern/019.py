# print -     D
#             C D
#             B C D
#             A B C D


n = int(input())
for i in range(1,n+1):
    a = ord('A') + n - i 
    for j in range(i):
        print(chr(a),end=' ')
        a = a + 1
    print()
