"""Modify thePredatoryCreditCard class from Section 2.4.1 so that a customer
is assigned a minimum monthly payment,  as a percentage of the balance,
and so that a late fee is assessed if the customer does not subsequently pay
that minimum amount before the next monthly cycle."""


class CreditCard:
	"""A consumer credit card."""

	def __init__(self, customer, bank, acnt, limit, balance=0):
		"""Create a new Credit Card instance.
		The initial balance is zero.

		customer	the name of the customer (e.g., 'John Bowman')
		bank		the name of the bank (e.g., 'California saving')
		acnt		the account identifier (e.g., '5391 0375 9389 5309')
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
		"""Return the name of the bank"""
		return self._bank

	def get_account(self):
		"""Return the card identifying number (typically stores as a string.)"""
		return self._account

	def get_limit(self):
		"""Return the current credit limit."""
		return self._limit

	def get_balance(self):
		"""Return current balance."""
		return self._balance

	def charge(self, price):
		"""Charge given price to the card, assuming sufficient credit limit.
		Return True if charge was processed, False if charge was denied."""

		if not isinstance(price, (int, float)):
			raise ValueError('Price must be a number')

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
		"""Make a payment to the given credit card."""

		if not isinstance(amount, (int, float)):
			raise ValueError('Amount must be a number.')
		elif amount < 0:
			raise ValueError('Payment must be positive.')

		"""Process customer payment that reduce the balance."""
		self._balance -= amount


class PredatoryCreditCard(CreditCard):
	"""An extension to CreditCard class that calculate compound intrest and
	fee."""

	"""This is a class level member"""
	OVERLIMIT_FEE = 5
	MAX_CHARGES = 10
	MINIMUM_PCT = 0.1
	LATE_FEE = 10

	def __init__(self, customer, bank, acnt, limit, apr):
		"""Create a new PredatoryCreditClass instance.
		the initial balance is zero.
		customer	the name of the customer (e.g., 'John Bowman')
		bank		the name of the bank (e.g., 'California Savings')
		acnt		the account identifier (e.g., '5391 0375 9387 5309')
		apr			annual percentage rate (e.g., '0.0825for 8.25% APR')
		"""

		super().__init__(self, customer, bank, acnt, limit)  # call super
		# constructor
		self._apr = apr
		self._num_charge = 0
		self._minimum_payment = 0

	def charge(self, price):
		"""Charge given price to the card, assuming sufficient credit limit.
		Return True if charge is process.
		Return False and access $5 if charged is denied."""

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
			"""If Positive balance, convert APR to monthly multiplicative 
			factor."""
			monthly_factor = pow(1 + self._apr, 1 / 12)
			self._balance *= monthly_factor

			self._minimum_payment = self._balance * self.MINIMUM_PCT

		if self._minimum_payment > 0:
			self._balance = self.LATE_FEE

		"""Reset the counter at beginning of each month."""
		self._num_charge = 0

	def make_payment(self, amount):
		"""Make a payment to the given credit card."""

		if super().make_payment(amount):
			self._minimum_payment = max(0, self._minimum_payment - amount)
