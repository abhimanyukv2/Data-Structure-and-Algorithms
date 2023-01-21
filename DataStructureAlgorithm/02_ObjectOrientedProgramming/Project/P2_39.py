"""Develop  an  inheritance  hierarchy  based  upon  a Polygon class  that
abstract  methods area() and perimeter( ).   Implement  classes Triangle,
Quadrilateral,Pentagon,Hexagon,and Octagon that  extend  this  baseclass,
with the obvious meanings for the area() and perimeter() methods.Also implement
classes,IsoscelesTriangle,EquilateralTriangle,Rectangle,and Square, that have
the appropriate  inheritance relationships.  Finally, write a simple program
that allows users to create polygons of the various types and input their
geometric dimensions, and the program the n outputs  their  area  and
perimeter.   For extra  effort,  allow  users  to  input polygons by
specifying their vertex coordinates and be able to test if two such polygons
are similar."""


class Polygon:
	"""Creating a Polygon class."""

	def __init__(self, *sides):
		"""Create a new polygon."""
		self._sides = sides

	def __str__(self):
		"""Return the polygon."""
		return f'{self.__class__.__name__}({", ".join(str(side) for side in self._sides)})'

	def __repr__(self):
		"""Return the polygon."""
		return f'{self.__class__.__name__}({", ".join(str(side) for side in self._sides)})'

	def area(self):
		"""Return the area of the polygon."""
		raise NotImplementedError

	def perimeter(self):
		"""Return the perimeter of the polygon."""
		raise NotImplementedError


class Triangle(Polygon):
	"""Creating a Triangle class."""

	def __init__(self, side1, side2, side3):
		"""Create a new triangle."""
		super().__init__(side1, side2, side3)

	def area(self):
		"""Return the area of the triangle."""
		s = self.perimeter() / 2
		return (s * (s - self._sides[0]) * (s - self._sides[1]) * (s - self._sides[2])) ** 0.5

	def perimeter(self):
		"""Return the perimeter of the triangle."""
		return sum(self._sides)


class Quadrilateral(Polygon):
	"""Creating a Quadrilateral class."""

	def __init__(self, side1, side2, side3, side4):
		"""Create a new quadrilateral."""
		super().__init__(side1, side2, side3, side4)

	def area(self):
		"""Return the area of the quadrilateral."""
		raise NotImplementedError

	def perimeter(self):
		"""Return the perimeter of the quadrilateral."""
		return sum(self._sides)


class Pentagon(Polygon):
	"""Creating a Pentagon class."""

	def __init__(self, side1, side2, side3, side4, side5):
		"""Create a new pentagon."""
		super().__init__(side1, side2, side3, side4, side5)

	def area(self):
		"""Return the area of the pentagon."""
		raise NotImplementedError

	def perimeter(self):
		"""Return the perimeter of the pentagon."""
		return sum(self._sides)


class Hexagon(Polygon):
	"""Creating a Hexagon class."""

	def __init__(self, side1, side2, side3, side4, side5, side6):
		"""Create a new hexagon."""
		super().__init__(side1, side2, side3, side4, side5, side6)

	def area(self):
		"""Return the area of the hexagon."""
		raise NotImplementedError

	def perimeter(self):
		"""Return the perimeter of the hexagon."""
		return sum(self._sides)


class Octagon(Polygon):
	"""Creating a Octagon class."""

	def __init__(self, side1, side2, side3, side4, side5, side6, side7, side8):
		"""Create a new octagon."""
		super().__init__(side1, side2, side3, side4, side5, side6, side7, side8)

	def area(self):
		"""Return the area of the octagon."""
		raise NotImplementedError

	def perimeter(self):
		"""Return the perimeter of the octagon."""
		return sum(self._sides)


class IsoscelesTriangle(Triangle):
	"""Creating a IsoscelesTriangle class."""

	def __init__(self, side1, side2, side3):
		"""Create a new isosceles triangle."""
		super().__init__(side1, side2, side3)

	def area(self):
		"""Return the area of the isosceles triangle."""
		raise NotImplementedError

	def perimeter(self):
		"""Return the perimeter of the isosceles triangle."""
		return sum(self._sides)


class EquilateralTriangle(Triangle):
	"""Creating a EquilateralTriangle class."""

	def __init__(self, side1, side2, side3):
		"""Create a new equilateral triangle."""
		super().__init__(side1, side2, side3)

	def area(self):
		"""Return the area of the equilateral triangle."""
		raise NotImplementedError

	def perimeter(self):
		"""Return the perimeter of the equilateral triangle."""
		return sum(self._sides)


class Rectangle(Quadrilateral):
	"""Creating a Rectangle class."""

	def __init__(self, side1, side2, side3, side4):
		"""Create a new rectangle."""
		super().__init__(side1, side2, side3, side4)

	def area(self):
		"""Return the area of the rectangle."""
		raise NotImplementedError

	def perimeter(self):
		"""Return the perimeter of the rectangle."""
		return sum(self._sides)


class Square(Quadrilateral):
	"""Creating a Square class."""

	def __init__(self, side1, side2, side3, side4):
		"""Create a new square."""
		super().__init__(side1, side2, side3, side4)

	def area(self):
		"""Return the area of the square."""
		raise NotImplementedError

	def perimeter(self):
		"""Return the perimeter of the square."""
		return sum(self._sides)


class Parallelogram(Quadrilateral):
	"""Creating a Parallelogram class."""

	def __init__(self, side1, side2, side3, side4):
		"""Create a new parallelogram."""
		super().__init__(side1, side2, side3, side4)

	def area(self):
		"""Return the area of the parallelogram."""
		raise NotImplementedError

	def perimeter(self):
		"""Return the perimeter of the parallelogram."""
		return sum(self._sides)


class Rhombus(Quadrilateral):
	"""Creating a Rhombus class."""

	def __init__(self, side1, side2, side3, side4):
		"""Create a new rhombus."""
		super().__init__(side1, side2, side3, side4)

	def area(self):
		"""Return the area of the rhombus."""
		raise NotImplementedError

	def perimeter(self):
		"""Return the perimeter of the rhombus."""
		return sum(self._sides)


class Trapezoid(Quadrilateral):
	"""Creating a Trapezoid class."""

	def __init__(self, side1, side2, side3, side4):
		"""Create a new trapezoid."""
		super().__init__(side1, side2, side3, side4)

	def area(self):
		"""Return the area of the trapezoid."""
		raise NotImplementedError

	def perimeter(self):
		"""Return the perimeter of the trapezoid."""
		return sum(self._sides)


class Kite(Quadrilateral):
	"""Creating a Kite class."""

	def __init__(self, side1, side2, side3, side4):
		"""Create a new kite."""
		super().__init__(side1, side2, side3, side4)

	def area(self):
		"""Return the area of the kite."""
		raise NotImplementedError

	def perimeter(self):
		"""Return the perimeter of the kite."""
		return sum(self._sides)


if __name__ == "__main__":
	# Test your code here
	pass
