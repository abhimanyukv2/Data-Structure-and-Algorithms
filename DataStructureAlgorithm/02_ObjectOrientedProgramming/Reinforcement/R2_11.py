'''In Section 2.3.3, we note that our Vector class supports a syntax such as v = u + [5, 3, 10, −2, 1], in which the sum of a vector and list returns a new vector. However, the syntax v = [5, 3, 10, −2, 1] + u is illegal. Explain how the Vector class definition can be revised so that this syntax generates a new vector.'''

class Vector:
    '''Represent a vector in a multidimensional space.'''

    def __init__(self, d):
        '''Create d-dimensional vector of zeros.'''
        self._coords = [0]*d

    def __len__(self):
        '''Return the dimension of the vector.'''
        return len(self._coords)

    def __getitem__(self, j):
        '''Return jth coordinate of vector.'''
        return self._coords[j]

    def __setitem__(self, j, val):
        '''Set jth coordinate of vector to given value.'''
        self._coords[j] = val

    def __add__(self, other):
        '''Return sum of two vectors.'''
        if len(self) != len(other):         # relies on __len__ method
            raise ValueError('dimenssions must agree')

        result = Vector(len(self))          # start with vector of zeros

        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __radd__(self, other):
        '''To ensure that other + vector will work, i.e., other is left side'''
        return self + other

    def __sub__(self, other):
        '''Return Difference of two vectors.'''
        if len(self) != len(other):         # relies on __len__ method
            raise ValueError('dimension of value must agree')
        
        result = Vector(len(self))          # start with vector of zeros

        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result

    def __rsub__(self, other):
        '''To ensure that other - vector will work. i.e., other on left side.'''
        return self - other

    def __neg__(self):
        '''Return vectors whose coordinates are all the negated values of the
        respective coordinates of v.'''
        result = Vector(len(self)) + self
        for i in range(len(self)):
            result[i] *= -1
        return result

    def __eq__(self, other):
        '''Return True if vector has same coordinates as other.'''
        return self._coords == other._coords

    def __ne__(self, other):
        '''Return True if vector differs from other.'''
        return not self == other            # rely on existing eq defination

    def __str__(self):
        '''Producing string representation of vector.'''
        return '<' + str(self._coords)[1:-1] + '>'      #adapt list representation

if __name__ == "__main__":
    while input() != '':
        d = int(input('How many dimension of vector du you have? '))
        x = Vector(d)

        for i in range(d):
            x.__setitem__(i, float(input()))
        print('vector x =', x.__str__())

        y = Vector(d)
        for i in range(d):
            y.__setitem__(i, float(input()))
        print('vector y =', y.__str__())

        z = Vector(d)
        for i in range(d):
            z.__setitem__(i, float(input()))
        print('vector z =', z.__str__())

        print('legal vector x + y', x + y)
        print('illegal vector z + x', z + x)

        print('legal vector x + [1, 2, 3] =', x + [1, 2, 3])

        print('illegal vetor [1, 2, 3] + x =', [1, 2, 3] + x)