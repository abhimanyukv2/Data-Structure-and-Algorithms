# print -     A A A
#             B B B 
#             C C C 


n = int(input())
a = ord("A")
for i in range(n):
    for j in range(n):
        print(chr(a),end=' ')
    a = a + 1
    print()
    