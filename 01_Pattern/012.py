# print - A B C
#         A B C
#         A B C

n = int(input())
for i in range(n):
    a = ord('A')
    for j in range(n):
        print(chr(a),end=' ')
        a = a + 1
    print()