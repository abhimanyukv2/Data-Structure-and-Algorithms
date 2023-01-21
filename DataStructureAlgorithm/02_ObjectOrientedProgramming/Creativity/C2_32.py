"""Write a Python class that extends the Progression class so that each value
in the progression is the square root of the previous value. (Note that you
can no longer represent each value with an integer.) Your constructor should
accept an optional parameter specifying the start value, using 65,536 as a
default."""


class Progression:
	"""Iterator producing a generic progression.
	Default iterator produces the whole numbers 0, 1, 2, ..."""

	def __init__(self, start=0):
		"""Initialize the current to the first value of the progression."""
		self._current = start

	def _advance(self):
		"""Update self._current to a new value. This should be overriden by
		the subclass to customize progression. By convention, if current is
		None this designates the end of a finite progression."""
		self._current += 1

	def __next__(self):
		"""Return the next element or raise StopIteration error."""

		if self._current is None:  # our convention to end our progression
			raise StopIteration

		answer = self._current
		self._advance()  # advance to prepare for next time

		return answer  # return the answer

	def __iter__(self):
		"""By convention an iterator must return itself as an iterator."""
		return self

	def print_progression(self, n):
		"""Print the next n value of the progression."""
		print(' '.join(str(next(self)) for _ in range(n)))


class SQRTProgression(Progression):
	"""Iterator produce an square root progression."""

	def __init__(self, start=65536):
		"""Create a new square root progression.
		start		the fist term of the progression (default 65536).
		"""
		super().__init__(start)  # initialize the base class

	def _advance(self):
		"""Update the current value to the square root of the previous value."""
		self._current = self._current ** 0.5

	def __getitem__(self, item):
		"""Return the value at the index item"""
		return self._current ** (1/(2**item))


if __name__ == "__main__":
	print('Default square root progression is ')
	SQRTProgression().print_progression(10)

	while input() != '':
		start = int(input('Start number: '))
		sqrt = SQRTProgression(start)
		n = int(input('How many progression do you want: '))
		for i in range(n):
			print(f'{i+1} = {sqrt[i]}')