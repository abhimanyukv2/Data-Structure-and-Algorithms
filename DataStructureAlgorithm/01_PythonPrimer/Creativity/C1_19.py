'''Demonstrate how to use Python’s list comprehension syntax to produce the list [ a , b , c , ..., z ], but without having to type all 26 such characters literally.'''

def comprihension(start, end):
    return [chr(x) for x in range(ord(start),ord(end)+1)]

start = input()
end = input()
print(comprihension(start, end))