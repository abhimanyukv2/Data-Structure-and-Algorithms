'''Write a Python program that repeatedly reads lines from standard input
until an EOFError is raised, and then outputs those lines in reverse order
(a user can indicate end of input by typing ctrl-D).
'''

def eofRaised():
    readLines = []
    while True:
        try:
            x = input()
            if x == "":
                raise EOFError
            readLines.append(x)
        except EOFError:
            print('End of File Error')
            return reversed(readLines)

ans = eofRaised()
print(list(ans))