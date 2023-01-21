'''The SequenceIterator class of Section 2.3.4 provides what is known as a forward iterator. Implement a class named ReversedSequenceIterator that serves as a reverse iterator for any Python sequence type. The first call to next should return the last element of the sequence, the second call to next should return the second-to-last element, and so forth.'''


class SequenceIterator:
    '''An iterator for any python's sequence types.'''

    def __init__(self, sequence):
        '''Create an iterator for the given sequence.'''
        self._seq = sequence             # keep a reference to the underlying data
        self._k = -1                     # will increament to 0 on first call to next

    def __next__(self):
        '''Return the next element, or else raise Stopiteration error.'''
        self._k += 1                    # advance to next index
        if self._k < len(self._seq):
            return self._seq[self._k]   # return the data element
        else:
            return StopIteration()      # there are no more element
    
    def __iter__(self):
        '''By convention, an iterator must return itself as an iterator.'''
        return self

class ReverseSequenceIterator:
    '''An reverse iterator for any python's sequence types.'''

    def __init__(self, sequence):
        '''Create an iterator for the given sequence.'''
        self._seq = sequence            # keep a reference to the underlying data
        self._k = len(sequence)         # will decrement to n - 1 on first call i.e., last element of the sequence

    def __next__(self):
        '''Return the previous element of the last element occure, or else raise Stopiteraion error.'''
        self._k -= 1                    # advance to previous index
        if self._k >= 0:
            return self._seq[self._k]   # return the data element
        else:
            raise StopIteration()       # there are no more element

    def __iter__(self):
        '''By convention, an iterator must return itelf as an iterator.'''
        return self