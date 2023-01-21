"""ThePredatoryCreditCard class of Section 2.4.1 provides a process_month
method that models the completion of a monthly cycle. Modify the class so
that once a customer has made ten calls to charge in the current month,
each additional call to that function results in an additional $1 surcharge."""


class CreditCard:
	"""A consumer credit card."""

	def __init__(self, customer, bank, acnt, limit, balance=0):
		"""Create a new Credit Card instance.
		The initial balance is zero.

		customer 	the name of the customer (e.g., 'John Bowman')
		bank		the name of the bank (e.g., 'California Saving')
		acnt 		the account identifier (e.g., '5391 0375 9389 5309')
		limit		credit limit (measure in dollars)
		"""

		self._customer = customer
		self._bank = bank
		self._account = acnt
		self._limit = limit
		self._balance = balance
		self._charge_count = 0

	def get_customer(self):
		"""Return the name of the customer."""
		return self._customer

	def get_bank(self):
		"""The return the name of the bank"""
		return self._bank

	def get_account(self):
		"""Return  the card identifying number (typically stored as a
		string)."""
		return self._account

	def get_limit(self):
		"""Return the current credit limit."""
		return self._limit

	def get_balance(self):
		"""Return the current balance"""
		return self._balance

	def charge(self, price):
		"""Charge given price to the card, assuming sufficient credit limit.
		Return True if charged was processed, False if charge wad denied."""

		if not isinstance(price, (int, float)):
			raise ValueError('Price must be a number.')

		if price + self._balance > self._limit:
			print(f'Credit card of {self._customer} account number '
				  f'{self._account} from {self._bank} denied. Accrued balance over limit.')
			return False
		else:
			self._balance += price
			self._charge_count += 1

			if self._charge_count > 10:
				self._balance += 1

			return True

	def make_payment(self, amount):
		"""Make payment to the given card, assuming amount is greater than 0."""

		if not isinstance(amount, (int, float)):
			raise ValueError('Payment must be a number')
		elif amount < 0:
			raise ValueError('Payment must be positive')

		"""Process customer payment that reduce the balance."""
		self._balance -= amount


class PredatoryCreditCard(CreditCard):
	"""An extension to CreditCard class that compound interest and fee."""

	OVERLIMIT_FEE = 5  # this is a class level member
	MAX_CHARGES = 10  # this is a class level member

	def __init__(self, customer, bank, acnt, limit, apr):
		"""Create a new Predatorycredit card instance.
		The initial balance is zero.
		customer		the name of the customer(e.g., 'John Bowman')
		bank			the name of the bank (e.g., 'California Savings')
		acnt			the account identifier (e.g., '5391 0375 9387 5309')
		apr				annual percentage rate (e.g., '0.0825 for 8.25% APR)
		"""
		super().__init__(customer, bank, acnt,
						 limit)  # call super() constructor
		self._apr = apr
		self._num_charge = 0

	def charge(self, price):
		"""Charge given price to the card, assuming sufficient credit limit.
		Return True if charged is processed.
		Return False and assess $5 fee if charge is denied."""

		success = super().charge(price)  # call inherited method

		if not success:
			self._balance += 5
		else:
			self._num_charge += 1
			if self._num_charge > self.MAX_CHARGES:
				self._balance += 1

		return success

	def process_month(self):
		"""Access monthly interest on outstanding balance."""

		if self._balance > 0:
			"""If positive balance, convert APR to monthly multiplicative 
			factor."""
			monthly_factor = pow(1 + self._apr, 1 / 12)
			self._balance *= monthly_factor
		"""Reset the counter at beginning of each month."""
		self._num_charge = 0


if __name__ == "__main__":
	cardHolder = []
	numCardHolder = 0

	while input() != "":
		customer = input()
		bank = input()
		account = input()
		limit = float(input())
		apr = float(input())
		cardHolder.append(PredatoryCreditCard(customer, bank, account, limit,
											  apr))
		numCardHolder += 1
	for i in range(numCardHolder):
		cardHolder[i].charge(float(input()))

	for i in range(numCardHolder):
		print(f'Customer = {cardHolder[i].get_customer()}')
		print(f'Bank = {cardHolder[i].get_bank()}')
		print(f'Account Numer = {cardHolder[i].get_account()}')
		print('Limit = {}'.format((cardHolder[i].get_limit())))
		print('Balance =', cardHolder[i].get_balance())

		while cardHolder[i].get_balance() > 100:
			cardHolder[i].make_payment(100)
			print('New balance =', cardHolder[i].get_balance())
		print()
	for i in range(numCardHolder):
		cardHolder[i].process_month()
		print('Monthly interest =', cardHolder[i].get_balance())