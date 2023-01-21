'''Exercise R-2.12 uses the __mul__ method to support multiplying a Vector by a number, while Exercise R-2.14 uses the __mul__ method to support computing a dot product of two vectors. Give a single implementation of Vector. __mul__ that uses run-time type checking to support both syntaxes u*v and u*k, where u and v designate vector instances and k represents a number.'''

class Vector:
    '''Represent a vector in a n multidimensional space.'''

    def __init__(self, d):
        '''Create d-dimensional vector of zeros.'''
        if isinstance(d, int):
            self._coords = [0]*d
        elif isinstance(d, (list, tuple)):
            self._coords = [0]*d
            for i in range(len(d)):
                self._coords[i] = d[i]
        else:
            raise ValueError('Dimension should be an integer or a list or tuple')

    def __len__(self):
        '''Return the dimension of the vector.'''
        return len(self._coords)

    def __getitem__(self, j):
        '''Return the jth coordinate of the vector.'''
        return self._coords[j]

    def __setitem__(self, j, val):
        '''Set jth coordinate of vector to given value.'''
        self._coords[j] = val

    def __add__(self, other):
        '''Return sum of two vectors.'''
        if len(self) != other:                      # relies on __len__ mehtod
            raise ValueError('Dimension must agree!')

        result = Vector(len(self))                  # start with vector of zeros
        for j in range(len(self)):
            result[j] = self[j] + other[j]

        return result

    def __radd__(self, other):
        '''To ensure that other + vector will work. i.e., other is left side.'''
        return self + other

    def __sub__(self, other):
        '''Return the difference of two vectors.'''
        if len(self) != len(other):                 # relies on __len__ method
            raise ValueError('Dimension of the vector must agree!')
        
        result = Vector(len(self))                  # start with vector of zeros
        for j in range(len(self)):
            result [j] = self[j] - other[j]

        return result

    def __rsub__(self, other):
        '''To ensure that other - vector will work, i.e., other is left side.'''
        return self - other

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
            raise ValueError('Multiplicand should be either be a scaler or a vector with the same direction as multiplier')
        
        return result

    def __rmul__(self, other):
        '''To ensure that other * vector will work, i.e., other on left side.'''
        if isinstance(other, (int, float)):
            return self*other

    def __neg__(self):
        '''Return vector whose coordinate are all the negative value of the respective coorfinate of v.'''
        result = Vector(len(self)) + self
        for i in range(len(self)):
            result[i] *= - 1
        return result

    def __str__(self):
        '''Prodcuing string representation of vector.'''
        return '<' + str(self._coords)[1:-1] + '>'      # adapt list

    def __repr__(self):
        '''Return string representation of repr().'''
        return 'Vector({})'.format(self._coords)

if __name__ == "__main__":
    d = int(input('How many dimension of vector do you want? '))
    u = Vector(d)
    v = Vector(d)

    for i in range(d):
        u.__setitem__(i, float(input(f'Value of u{i+1}: ')))
    print('Vector u =',u.__str__())
    for i in range(d):
        v.__setitem__(i, float(input(f'Value of v{i+1}: ')))
    print('Vector v =',v.__str__())

    k = float(input('Enter a scalre value k: '))

    print('Product of vector u and sclare k =', u * k)
    print('Product of sclare k and vector u =', k * u)

    print('Dot product of vector u and vector v =', u * v)
    print('Dot product of vector v and vector u =', v * u)