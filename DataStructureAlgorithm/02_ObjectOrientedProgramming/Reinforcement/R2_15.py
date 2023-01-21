'''The Vector class of Section 2.3.3 provides a constructor that takes an integer d, and produces a d-dimensional vector with all coordinates equal to 0. Another convenient form for creating a new vector would be to send the constructor a parameter that is some iterable type representing a sequence of numbers, and to create a vector with dimension equal to the length of that sequence and coordinates equal to the sequence values. For example, Vector([4, 7, 5]) would produce a three-dimensional vector with coordinates <4, 7, 5>. Modify the constructor so that either of these forms is acceptable; that is, if a single integer is sent, it produces a vector of that dimension with all zeros, but if a sequence of numbers is provided, it produces a vector with coordinates based on that sequence.'''

class Vector:
    '''Represent a vector in a multidimensional space.'''

    def __init__(self, d):
        '''Create d-dimensional vector of zeros.'''
        if isinstance(d, int):
            self._coords = [0]*d
        elif isinstance(d, (list, tuple)):
            self._coords = [0]*len(d)
            for i in range(len(d)):
                self._coords[i] = d[i]
        else:
            raise ValueError('Dimension should be an integer or a list')

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

    def __mul__(self, other):
        '''Return multiplication of a scaler or a vector'''
        if isinstance(other, (int, float)):
            result = Vector(len(self))
            for j in range(len(self)):
                result[j] = self[j] * other
        elif len(self) == len(other):
            result = Vector(len(self))
            for j in range(len(self)):
                result[j] = self[j] * other[j]
        else:
            raise ValueError('Muliplicand should be a scaler or a vector with the same direction as multiplier')
        return result

    def __rmul__(self, other):
        '''Return multiplication of a vector or a scaler'''
        if isinstance(other, (int, float)):
            result = Vector(len(self))
            for j in range(len(self)):
                result[j] = self[j] * other
        elif len(self) == len(other):
            result = Vector(len(self))
            for j in range(len(self)):
                result[j] = self[j] * other[j]
        else:
            raise ValueError('Multiplicand should be a vector or a scaler with the same dimenson as multiplier')
        return result

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
        return '<' + str(self._coords)[1:-1] + '>'      #adapt list 
        
    def __repr__(self):
        '''Return string representation for repr().'''
        return 'Vector({})'.format(self._coords)

    def __iter__(self):
        '''Generate an iteration of the vector's elements.'''
        return self._coords.__iter__()

    def __contains__(self, item):
        '''Return True if item is found in the vector.'''
        return item in self._coords
    
    def __bool__(self):
        '''Return True if any of the coordinates is nonzero.'''
        for i in self._coords:
            if i != 0:
                return True
        return False

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

        print('dot product of vector x and y is', x * y)
        print('dot product of vector z and x is', z * x)

        multi = float(input('Multiply by: '))
        print('Vector multiplication by {} is {}'.format(multi, multi*x))