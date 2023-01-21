class CreditCard:
    """A consumer credit card."""

    def __init__(self, customer, bank, acnt, limit):
        """Create a new Credit Card instance.
        The initial balance is zero.
        
        customer    the name of the customer(e.g., 'John Bowman')
        bank        the name of the bank(e.g., 'California Savings')
        acnt        the account identifier (e.g., '5391 0375 9387 5309')
        limit       credit limit (measure in dollars)
        """

        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        '''Return name of the customer.'''
        return self._customer

    def get_bank(self):
        '''Return the Bank's name.'''
        return self._bank

    def get_account(self):
        '''Return the card identifying number (typically stored as a string).'''
        return self._account

    def get_limit(self):
        '''Return current credit limit.'''
        return self._limit

    def get_balance(self):
        '''Return current balance.'''
        return self._balance

    def charge(self, price):
        '''Charge given price to the card, assuming sufficient credit limit.
        Return True if charge was processed; False if charge was denied.'''
        if price + self._balance > self._limit: #if charged would exceed limit
            return False
        else:
            self._balance += price              #cannot accept charge
            return True

    def make_payment(self, amount):
        '''Process customer payment that reduce balance.'''
        self._balance -= amount

class PredatoryCreditCard(CreditCard):
    '''An extensionto creditCard that compound interest and fees.'''

    OVERLIMIT_FEE = 5                           # This is a class-level member

    def __init__(self, customer, bank, acnt, limit, apr):
        '''Create a new predatorycredit card instance.
        The initial balance is zero.
        customer    the name of the custome(e.g., 'John Bowman')
        bank        the name of he bank (e.g., 'California Saving')
        acnt        the account identifier (e.g., '5391 0375 9387 5309')
        apr         annual percentage rate(e.g., 0.0825 for 8.25% APR)
        '''
        super().__init__(customer,bank, acnt, limit)    #call suoer constructor
        self._apr = apr
    
    def charge(self, price):
        '''Charge given price to the card, assuming sufficient credit limit.
        Return True if charge charge is processed.
        Return False and assess $5 fee if charge is denied.'''
        success = super().charge(price)         #call inherited method
        if not success:
            # self._balance += 5                  # assess penalty
            self._balance += PredatoryCreditCard.OVERLIMIT_FEE
        return success

    def process_month(self):
        '''Assess monthly intrest on outstanding balance.'''
        if self._balance > 0:
            '''If positive balance, convert APR to monthly multiplicative factor.'''
            monthly_factor = pow(1 + self._apr, 1/12)
            self._balance *= monthly_factor

if __name__ == "__main__":
    cardHolder = []

    while input() != '':
        name = input()
        bank = input()
        account = input()
        limit = float(input())
        apr = float(input())
        cardHolder.append(PredatoryCreditCard(name, bank, account, limit, apr))

    for i in range(len(cardHolder)):
        cardHolder[i].charge(float(input()))

    for i in range(len(cardHolder)):
        print('Customer =', cardHolder[i].get_customer())
        print('Bank =', cardHolder[i].get_bank())
        print('Account Number =', cardHolder[i].get_account())
        print('Limit =', cardHolder[i].get_limit())
        print('Balance =', cardHolder[i].get_balance())

        while cardHolder[i].get_balance() > 100:
            cardHolder[i].make_payment(100)

            print('New Balancce =',cardHolder[i].get_balance())
    for i in range(len(cardHolder)):
        cardHolder[i].process_month()
        print('Monthly intrest =',cardHolder[i].get_balance())