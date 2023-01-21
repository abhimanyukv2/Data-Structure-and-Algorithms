class Vectors:
    """Represent a vector in a multi-dimensional space."""

    def __init__(self, d):
        """Create d-dimensional vector of zeros."""
        self._coord = [0]*d

    def __len__(self):
        'return the dimension of the vector.'
        return len(self._coord)

    def __getitem__(self, j):
        '''Return jth coordinate of vector.'''
        return self._coord[j]

    def __setitem__(self, j, val):
        '''Set jth coordinate of vector to given value.'''
        self._coord[j] = val

    def __add__(self, other):
        '''Return sum of two vectors.'''
        if len(self) != len(other):         # relies on __len__ method
            raise ValueError('Dimension must agree')
        result = Vectors(len(self))         # start with vector of zero
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __eq__(self, other):
        '''Return True if vector has same coordinates as other.'''
        return self._coord == other._coord

    def __ne__(self, other):
        '''Return True if vector differ from other.'''
        return not self == other          # relay on existing  __eq__ definition

    def __str__(self):
        '''Produce string representation of vectors.'''
        return '<' + str(self._coord)[1:-1] + '>'   #adpt list representation

if __name__ == "__main__":
    d = int(input())
    v1 = Vectors(d)
    for i in range(d):
        value = int(input())
        v1.__setitem__(i, value)
    print(v1.__str__())
    v2 = Vectors(d)
    for i in range(d):
        value = int(input())
        v2.__setitem__(i, value)
    print(v2.__str__())
    result = Vectors.__add__(v1, v2)
    print(result)
    print(Vectors.__getitem__(result, 1))
    print(Vectors.__len__(result))
    print(Vectors.__eq__(v1, v2))
    print(Vectors.__ne__(v1, v2))