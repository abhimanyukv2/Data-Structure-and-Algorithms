'''Write a Python program that can “make change.” Your program should take two numbers as input, one that is a monetary amount charged and the other that is a monetary amount given. It should then return the number of each kind of bill and coin to give back as change for the difference between the amount given and the amount charged. The values assigned to the bills and coins can be based on the monetary system of any current or former government. Try to design your program so that it returns as few bills and coins as possible.'''

def makeChange(amountCharged, amountGiven):
    moneyType = (2000, 500, 200, 100, 50, 20, 10, 5, 2, 1)
    
    if amountCharged > amountGiven:
        return 'Need more money. Please!'
    
    elif amountCharged == amountGiven:
        return 'Exact money is given!'

    else:
        amountReturned = {}
        remainingAmount = amountGiven - amountCharged
        for money in moneyType:
            num = remainingAmount//money
            if remainingAmount > money:
                amountReturned[money] = num
                remainingAmount = remainingAmount - num*money
    
    return amountReturned

amountCharged = int(input())
amountGiven = int(input())
ans = makeChange(amountCharged, amountGiven)
print(ans)