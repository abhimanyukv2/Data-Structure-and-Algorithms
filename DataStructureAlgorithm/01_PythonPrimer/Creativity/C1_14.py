'''Write a short Python function that takes a sequence of integer values and determines if there is a distinct pair of numbers in the sequence whose product is odd.'''

def pairProductOdd(sequence):
    for i in range(len(sequence)-1):
        if (sequence[i]*sequence[i+1])%2 == 1:
            return 'sequence[{}] and sequence[{}] product is odd'.format(i,i+1)

    return 'No distinct pair of number in the sequence whose product is odd.'

sequence = list(map(int,input().split()))
ans = pairProductOdd(sequence)
print(ans)