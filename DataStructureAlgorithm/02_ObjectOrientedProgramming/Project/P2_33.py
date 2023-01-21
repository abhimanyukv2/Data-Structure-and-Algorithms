"""Write a Python program that inputs a polynomial in standard algebraic
notation and outputs the first derivative of that polynomial."""


class Polynomial:
	"""Creating a Polynomial expression by tacking standard algebraic
	notation."""

	def __init__(self, expression):
		"""Create a new polynomial expression."""
		self._expression = expression
		self._polynomial = self._create_polynomial()

	def _create_polynomial(self):
		"""Create a polynomial expression."""
		polynomial = {}
		terms = self._expression.split(' ')
		for term in terms:
			coefficient, exponent = term.split('x')
			polynomial[int(exponent)] = int(coefficient)
		return polynomial

	def __str__(self):
		"""Return the polynomial expression."""
		return self._expression

	def __repr__(self):
		"""Return the polynomial expression."""
		return self._expression

	def __add__(self, other):
		"""Add two polynomial expressions."""
		polynomial = {}
		for exponent, coefficient in self._polynomial.items():
			polynomial[exponent] = coefficient
		for exponent, coefficient in other._polynomial.items():
			if exponent in polynomial:
				polynomial[exponent] += coefficient
			else:
				polynomial[exponent] = coefficient
		return Polynomial(' '.join(f'{coefficient}x{exponent}' for exponent, coefficient in polynomial.items()))

	def __sub__(self, other):
		"""Subtract two polynomial expressions."""
		polynomial = {}
		for exponent, coefficient in self._polynomial.items():
			polynomial[exponent] = coefficient
		for exponent, coefficient in other._polynomial.items():
			if exponent in polynomial:
				polynomial[exponent] -= coefficient
			else:
				polynomial[exponent] = -coefficient
		return Polynomial(' '.join(f'{coefficient}x{exponent}' for exponent, coefficient in polynomial.items()))

	def __mul__(self, other):
		"""Multiply two polynomial expressions."""
		polynomial = {}
		for exponent1, coefficient1 in self._polynomial.items():
			for exponent2, coefficient2 in other._polynomial.items():
				exponent = exponent1 + exponent2
				coefficient = coefficient1 * coefficient2
				if exponent in polynomial:
					polynomial[exponent] += coefficient
				else:
					polynomial[exponent] = coefficient
		return Polynomial(' '.join(f'{coefficient}x{exponent}' for exponent, coefficient in polynomial.items()))

	def __truediv__(self, other):
		"""Divide two polynomial expressions."""
		polynomial = {}
		for exponent1, coefficient1 in self._polynomial.items():
			for exponent2, coefficient2 in other._polynomial.items():
				exponent = exponent1 - exponent2
				coefficient = coefficient1 / coefficient2
				if exponent in polynomial:
					polynomial[exponent] += coefficient
				else:
					polynomial[exponent] = coefficient
		return Polynomial(' '.join(f'{coefficient}x{exponent}' for exponent, coefficient in polynomial.items()))

	def __pow__(self, other):
		"""Raise a polynomial expression to a power."""
		polynomial = {}
		for exponent1, coefficient1 in self._polynomial.items():
			for exponent2, coefficient2 in other._polynomial.items():
				exponent = exponent1 * exponent2
				coefficient = coefficient1 ** coefficient2
				if exponent in polynomial:
					polynomial[exponent] += coefficient
				else:
					polynomial[exponent] = coefficient
		return Polynomial(' '.join(f'{coefficient}x{exponent}' for exponent, coefficient in polynomial.items()))

	def derivative(self):
		"""Return the first derivative of a polynomial expression."""
		polynomial = {}
		for exponent, coefficient in self._polynomial.items():
			if exponent > 0:
				polynomial[exponent - 1] = coefficient * exponent
		return Polynomial(' '.join(f'{coefficient}x{exponent}' for exponent, coefficient in polynomial.items()))


if __name__ == "__main__":
	# Get the polynomial expression from the user
	expression = input('Enter a polynomial expression: ')
	polynomial = Polynomial(expression)
	print(f'The first derivative of {polynomial} is {polynomial.derivative()}.')

	"""example:
	Enter a polynomial expression: 3x2 2x 1
	The first derivative of 3x2 2x 1 is 6x 2x.
	"""
