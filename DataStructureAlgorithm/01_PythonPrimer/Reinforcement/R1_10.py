'''What parameters should be sent to the range constructor, to produce a
range with values 8, 6, 4, 2, 0, −2, −4, −6, −8?'''

'''Parameter of the range is range(8,-10,-2)'''

def rangeConstructor(lst):
    start = lst[0]
    steps = lst[1] - lst[0]
    end = lst[-1] + steps
    return start, end, steps

lst = list(map(int, input().split()))
ans = rangeConstructor(lst)
print(ans)