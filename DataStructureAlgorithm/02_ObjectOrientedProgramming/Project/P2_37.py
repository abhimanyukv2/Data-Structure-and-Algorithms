"""Write a simulator, as in the previous project, but add a Boolean gender
field and a floating-point strength field to each animal, using an Animal
class as a base class. If two animals of the same type try to collide,
then they only create a new instance of that type of animal if they
are of differ-ent genders. Otherwise, if two animals of the same type and
gender try to collide, then only the one of larger strength survives."""

import random


class RiverEcosystem:
	"""Creating a RiverEcosystem class which will contain bears and fish"""

	class Bear:
		"""Creating a Bear class."""

		def __init__(self, location):
			"""Create a new Bear instance."""
			self._location = location
			self._strength = random.uniform(0, 1)
			self._gender = True if random.randint(0, 1) > 0.5 else False

	class Fish:
		"""Creating a Fish class."""

		def __init__(self, location):
			"""Create a new Fish instance."""
			self._location = location
			self._strength = random.uniform(0, 1)
			self._gender = True if random.randint(0, 1) > 0.5 else False

	def __init__(self, size=100, num_bears=3, num_fish=10):
		"""Create a new RiverEcosystem instance.
		size 		the size of the river
		num_bears 	the number of bears in the river
		num_fish 	the number of fish in the river
		"""
		self._river = [None] * size
		self._num_bears = num_bears
		self._num_fish = num_fish
		self._time = 0
		self._populate()

	def __repr__(self):
		"""Return the string representation of a RiverEcosystem object."""
		output_string = []
		for i in range(len(self._river)):
			if self._river[i] is None:
				output_string.append(' ')
			elif isinstance(self._river[i], self.Bear):
				output_string.append('B')
			elif isinstance(self._river[i], self.Fish):
				output_string.append('F')

		return ''.join(output_string)

	def _populate(self):
		"""Populate the river with bears and fish."""
		while self._num_bears:
			location = random.randint(0, len(self._river) - 1)
			if self._river[location] is None:
				self._river[location] = self.Bear(location)
				self._num_bears -= 1

		while self._num_fish:
			location = random.randint(0, len(self._river) - 1)
			if self._river[location] is None:
				self._river[location] = self.Fish(location)
				self._num_fish -= 1

	def _move(self):
		"""Move all the animals in the river."""
		for i in range(len(self._river)):
			if self._river[i] is not None:
				self._river[i]._location = (self._river[i]._location + 1) % len(
					self._river)

	def _eat(self):
		"""Have all the bears eat the fish."""
		for i in range(len(self._river)):
			if isinstance(self._river[i], self.Bear):
				if isinstance(self._river[self._river[i]._location], self.Fish):
					if self._river[self._river[i]._location
					]._strength < self._river[i]._strength:
						self._river[self._river[i]._location] = None


if __name__ == '__main__':
	river = RiverEcosystem()
	print(river)
	river._move()
	print(river)
	river._eat()
	print(river)
