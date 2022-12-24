'''Give an example of a Python code fragment that attempts to write an element to a list based on an index that may be out of bounds. If that index is out of bounds, the program should catch the exception that results, and print the following error message:
“Don’t try buffer overflow attacks in Python!”'''


def overflowAttact(data,n):
    index = 0
    while True:
        value = input()
        try:
            data[index] = value
            index += 1
            if index == n:
                raise IndexError
        except IndexError:
            print("Don't try buffer overflow attacks in python")
            break

n = int(input())
data = [0 for i in range(n)]
overflowAttact(data,n)