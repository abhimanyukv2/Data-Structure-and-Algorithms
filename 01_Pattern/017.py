# print -     A
#             B C
#             D E F
#             G H I J

n = int(input())
a = ord('A')
for i in range(n):
    for j in range(i+1):
        print(chr(a),end=' ')
        a = a + 1
    print()
