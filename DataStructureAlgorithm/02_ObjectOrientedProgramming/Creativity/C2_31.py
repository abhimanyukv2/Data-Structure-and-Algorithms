"""Write a Python class that extends the Progression class so that each value in
the progression is the absolute value of the difference between the previous
two values. You should include a constructor that accepts a pair of numbers
as the first two values, using 2 and 200 as the defaults."""


class Progression:
	"""Iterator producing a generic progression.
	Default iterator produces the whole numbers 0, 1, 2, ..."""

	def __init__(self, start=0):
		"""Initialize the current to the first value of the progression."""
		self._current = start

	def _advance(self):
		"""Update self._current to a new value. This should be overridden by
		the subclass to customize progression. By convention, if current is
		set to None, this designates the end of a finite progression."""
		self._current += 1

	def __next__(self):
		"""Return the next element, or raise StopIteration error."""
		if self._current is None:  # our convention to end a progression
			raise StopIteration
		else:
			answer = self._current
			self._advance()  # advance to prepare for the next time
			return answer  # return the answer

	def __iter__(self):
		"""By convention, an iterator must return itself as an iterator."""
		return self  # so we return ourselves

	def print_progression(self, n):
		"""Print next n values of the progression."""
		print(' '.join(str(next(self)) for _ in range(n)))


class AbsoluteProgression(Progression):
	"""Iterator produce an absolute progression."""

	def __init__(self, first=2, second=200):
		"""Create a new absolute progression.
		first   the fist term of the progression (default 2)
		second  the second term of the progression (default 200)
		"""
		super().__init__(first)  # initialize base class
		self._prev = second + first  # initialize the previous term

	def _advance(self):
		"""Update the current value by taking the absolute value of the sum
		of previous two terms."""
		self._prev, self._current = self._current, abs(self._prev - self._current)


if __name__ == "__main__":
	AbsoluteProgression().print_progression(10)