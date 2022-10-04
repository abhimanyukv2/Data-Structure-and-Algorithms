# Switch case is not in-buit function of python
# for implimentation of switch case in python
# we use function and dictionary

def numbers_to_strings(argument):
    switcher = {
        0: "zero",
        1: "one",
        2: "two",
    }
    return switcher.get(argument, "It is a default Case")
 
argument=0
print (numbers_to_strings(argument))
print(numbers_to_strings(4))


# there is no need to use break and continue statement because
# in dictionary it re return only key value.