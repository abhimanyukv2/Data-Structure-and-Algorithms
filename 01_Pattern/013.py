# print -     A B C
#             D E F
#             G H I

            

n = int(input())
a = ord('A')
for i in range(n):
    for i in range(n):
        print(chr(a),end=' ')
        a = a + 1
    print()