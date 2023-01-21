"""In Section 2.3.5, we note that our version of the Range class has implicit
support for iteration, due to its explicit support of both len and getitem .
The class also receives implicit support of the Boolean test, “k in r” for
Range r. This test is evaluated based on a forward iteration through the
range, as evidenced by the relative quickness of the test 2 in Range(
10000000) versus 9999999 in Range(10000000). Provide a more efficient
implementation of the __contains__ method to determine whether a particular
value lies within a given range. The running time of your method should be
independent of the length of the range."""


class Range:
	"""A class that mimic's the built-in range class."""

	def __init__(self, start, stop=None, step=1):
		"""Initialize a Range instance.
		Semantic is similar to built-in range class"""
		if step == 0:
			raise ValueError('step cannot be 0')

		if stop is None:  # special case of range(n)
			start, stop = 0, start  # should be treated as if range(0, n)

		# Calculate the effective length once
		self._length = max(0, (stop - start + step - 1) // step)

		# need knowledge of stat and step (but not stop) to support __getitem__
		self._start = start
		self._step = step

	def __len__(self):
		"""Return number of entries in the range"""
		return self._length

	def __getitem__(self, item):
		"""Return entry at index item (using standard interpretation if
		negative)."""
		if item < 0:
			item += len(self)  # attempt to convert negative index

		if not 0 <= item < self._length:
			raise IndexError('Index out of range')

		return self._start + item * self._step

	def __contains__(self, item):
		"""That will be in the sequences if (item - start)%step == 0"""
		_factor, _reminder = divmod(item - self._start, self._step)

		if _reminder == 0:  # It is the part of the  infinite range in either direction
			# Now we just need to check if it's within the defined range
			if len(self) > _factor >= 0:
				return True
			else:
				return False
		else:
			return False


if __name__ == "__main__":
	r = Range(10000000)
	print('2 in range(r)', 2 in r)
	print('999999 in range(r)', 9999999 in r)
