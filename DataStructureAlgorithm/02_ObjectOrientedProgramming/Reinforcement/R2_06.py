'''If the parameter to the make payment method of the CreditCard class were a negative number, that would have the effect of raising the balance on the account. Revise the implementation so that it raises a ValueError if a negative value is sent.'''


'''Use the techniques of Section 1.7 to revise the charge and make payment methods of the CreditCard class to ensure that the caller sends a number as a parameter'''


class CreditCard:

    def __init__(self, customer, bank, acnt, limit):
        '''Create a new Credit card instance. The initial balance is 0
        customer    the name of the customer(e.g., 'John Bowman')
        bank        the name of the bank (e.g., 'California Savings')
        acnt        the account identifier (e.g., '5391 0375 9387 5309')
        limit       credit limit (measured in dollars)'''

        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0
        self._charge_count = 0

    def get_customer(self):
        '''Return the name of the customer'''
        return self._customer

    def get_bank(self):
        '''Return the name of the bank's'''
        return self._bank

    def get_account(self):
        '''Return the card identifying number (typically store as a string)'''
        return self._account

    def get_limit(self):
        '''return the current credit limit'''
        return self._limit

    def get_balance(self):
        '''Return the current balance'''
        return self._balance

    def charge(self, price):
        '''Charge given price to the card, assumming suffient credit limit.
        Return True if charged was processed, False if charge was denied.'''

        if not isinstance(price, (float, int)):
            raise ValueError('price must be a number.')

        if price < 0:
            raise ValueError('Price must be a positive number')
        
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            self._charge_count += 1

            if self._charge_count > 10:
                self._balance += 1      # surcharge for al calls after 10 charges
            return True

    def make_payment(self, amount):
        if not isinstance(amount, (int, float)):
            raise ValueError('Payment must be a number')
        elif amount < 0:
            raise ValueError('Payment must be positive')
        '''process customer payment that reduce the balance'''
        self._balance -= amount

if __name__ == "__main__":
    wallet = []

    while input() != '':
        customer = input()
        bank = input()
        acnt = input()
        limit = int(input())
        wallet.append(CreditCard(customer, bank, acnt, limit))

        if input('Want to make charge? ').lower() == 'y':
            wallet[-1].charge(float(input()))
        
        print(wallet[-1].get_balance())

        if input('Want to make payment? ').lower() == 'y':
            wallet[-1].make_payment(float(input()))
            
        print(wallet[-1].get_balance())