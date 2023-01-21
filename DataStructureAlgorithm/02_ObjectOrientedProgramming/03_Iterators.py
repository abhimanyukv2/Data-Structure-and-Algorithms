class SequenceIterator:
    """An iterator for any of Python's sequence types."""

    def __init__(self, sequence):
        '''Create an Iterator for the given sequence.'''
        self._seq = sequence    #keep a reference to the underlying data
        self._k = -1            #will increment to 0 o first call

    def __next__(self):
        '''Return the next element, or else raise stopIteration error.'''
        self._k += 1                    #Advance to the next step
        if self._k < len(self._seq):
            return self._seq[self._k]   #Return the data element 
        else:
            raise StopIteration()       #There are no more element

    def __iter__(self):
        '''By convention, an iterator must return itself as an iterator.'''
        return self

if __name__ == "__main__":
    sequence = list(input().split())
    s = SequenceIterator(sequence)
    print(s.__iter__())
    while True:
        print(s.__next__())