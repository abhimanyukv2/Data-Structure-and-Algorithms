'''What parameters should be sent to the range constructor, to produce a
range with values 50, 60, 70, 80?'''

'''Parameter of the range is range(50,90,10)'''

def rangeConstructor(lst):
    start = lst[0]
    steps = lst[1] - lst[0]
    end = lst[-1] + steps
    return start, end, steps

lst = list(map(int, input().split()))
ans = rangeConstructor(lst)
print(ans)