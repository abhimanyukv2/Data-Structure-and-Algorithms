"""Write a Python program to simulate an ecosystem containing two types of
creatures, bears and fish. The ecosystem consists of a river, which is
modeled as a relatively large list. Each element of the list should be a Bear
object, a Fish object, or None. In each time step, based on a random process,
each animal either attempts to move into an adjacent list location or stay
where it is. If two animals of the same type are about to collide in the same
cell, then they stay where they are, but they create a new instance of that
type of animal, which is placed in a random empty (i.e., previously None)
location in the list.  If a bear and a fish collide, however, then the fish
dies (i.e., it disappears)."""

import random


class RiverEcosystem:
	"""Creating a RiverEcosystem class which will contain bears and fish
	object."""

	class Bear:
		"""Creating a Bear class."""

		def __init__(self, location):
			"""Create a new Bear instance."""
			self._location = location

		def __str__(self):
			"""Return the string representation of a Bear object."""
			return 'B'

	class Fish:
		"""Creating a Fish class."""

		def __init__(self, location):
			"""Create a new Fish instance."""
			self._location = location

		def __str__(self):
			"""Return the string representation of a Fish object."""
			return 'F'

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

	def _move(self, animal):
		"""Move the animal to a random empty location in the river."""
		locations = [i for i in range(len(self._river)) if
					 self._river[i] is None]
		if locations:
			new_location = random.choice(locations)
			self._river[animal._location] = None
			self._river[new_location] = animal
			animal._location = new_location

	def _collision(self, animal1, animal2):
		"""Handle the collision between two animals."""
		if isinstance(animal1, self.Bear) and isinstance(animal2, self.Bear):
			self._bear_collision(animal1, animal2)
		elif isinstance(animal1, self.Fish) and isinstance(animal2, self.Fish):
			self._fish_collision(animal1, animal2)
		elif isinstance(animal1, self.Bear) and isinstance(animal2, self.Fish):
			self._bear_fish_collision(animal1, animal2)
		elif isinstance(animal1, self.Fish) and isinstance(animal2, self.Bear):
			self._bear_fish_collision(animal2, animal1)

	def _bear_collision(self, bear1, bear2):
		"""Handle the collision between two bears."""
		self._move(bear1)
		self._move(bear2)
		self._add_bear()

	def _fish_collision(self, fish1, fish2):
		"""Handle the collision between two fish."""
		self._move(fish1)
		self._move(fish2)
		self._add_fish()

	def _bear_fish_collision(self, bear, fish):
		"""Handle the collision between a bear and a fish."""
		self._move(bear)
		self._river[fish._location] = None

	def _add_bear(self):
		"""Add a new bear to the river."""
		location = random.randint(0, len(self._river) - 1)
		if self._river[location] is None:
			self._river[location] = self.Bear(location)
			self._num_bears += 1

	def _add_fish(self):
		"""Add a new fish to the river."""
		location = random.randint(0, len(self._river) - 1)
		if self._river[location] is None:
			self._river[location] = self.Fish(location)
			self._num_fish += 1

	@property
	def river(self):
		return self._river


if __name__ == '__main__':
	river = RiverEcosystem()
	print(river)
	river._collision(river._river[0], river.river[1])
	print(river)