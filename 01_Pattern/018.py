# print - A 
        # B C
        # C D E 
        # D E F G


n = int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        a = ord('A') + i + j - 2
        print(chr(a),end=' ')
    print()