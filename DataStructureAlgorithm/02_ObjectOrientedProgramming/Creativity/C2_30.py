"""At the close of Section 2.4.1, we suggest a model in which
the CreditCard class supports a nonpublic method, _set_balance(b), that could be
used by subclasses to affect a change to the balance, without directly
accessing the _balance data member. Implement such a model, revising both
theCreditCard and PredatoryCreditCard classes accordingly."""


class CreditCard:
	def __init__(self, customer, bank, acnt, limit, balance=0):
		"""
		Create a new Credit Card instance.
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
		"""Return the name of the bank."""
		return self._bank

	def get_account(self):
		"""Return the card identifying number (typically a str)."""
		return self._account

	def get_limit(self):
		"""Return the current credit limit."""
		return self._limit

	def get_balance(self):
		"""Return the current balance."""
		return self._balance

	def charge(self, price):
		"""Charge given price to the card, assuming sufficient credit limit.
		Return True if charge was processed, False if charge was denied"""

		if not isinstance(price, (int, float)):
			raise ValueError('Price must be a number.')
		if price + self._balance > self._limit:
			print(f'Credit card of {self._customer}, account number '
				  f'{self._account} from {self._bank} is denied. Accrued '
				  f'balance over limit.')
			return False
		else:
			self._balance += price
			self._charge_count += 1
			if self._charge_count > 10:
				self._balance += 1  # $1 surcharge for all calls after 10
			# charges
			return True

	def make_payment(self, amount):
		"""Make a payment to the given credit card."""

		if not isinstance(amount, (int, float)):
			raise ValueError('Payment must be a number.')
		elif amount < 0:
			raise ValueError('Payment must be positive')

		"""Process customer payment that reduce the balance."""
		self._balance -= amount


class PredatoryCreditCard(CreditCard):
	"""An extension to CreditCard that calculate compound interest and fees."""

	def __init__(self, customer, bank, acnt, limit, apr):
		"""Create a new Predatory credit class instance."""

		super().__init__(customer, bank, acnt, limit)  # call super contractor
		self._apr = apr
		self._cycle = 0
		self._min_pay = 0
		self._late_fee = False
		self._override_limit = False

	def _set_balance(self, b):
		"""This could be used by subclasses to affect a change to the
		balance, without directly accessing the _balance data member."""

		self._balance = b

	def charge(self, price):
		"""Charge given price to the card, assuming sufficient credit limit.
		Return True if charge was processed.
		Return False and access $5 fee if charge is denied."""

		success = super().charge(price)  # call inherited method
		if not success:
			self._balance += 5  # cases penalty
		return success

	def get_balance(self):
		return round(self._balance, 2)

	def process_month(self):
		"""Access monthly interest on outstanding balance"""
		fee = 10
		if self._late_fee:
			success = self.charge(fee)

		self._cycle += 1
		prev_month = self._balance
		self._min_pay = round(0.4 * prev_month, 2)

		if self._balance > 0:
			if self._balance >= self._limit:
				self._override_limit = True
			monthly_factor = pow(1 + self._apr, 1 / 12)
			self._set_balance(self._balance * monthly_factor)

	def make_payment(self, amount):
		"""Make a payment to the given credit card."""
		super().make_payment(amount)

		if self._min_pay > 0:
			self._late_fee = True
			self._min_pay -= amount
			if self._min_pay >= 0:
				self._late_fee = False

		else:
			self._late_fee = False

	@property
	def get_apr(self):
		return str(100 * self._apr) + '%'
