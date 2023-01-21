class Range:
    """A class that mimic's the bult-in range class."""
    
    def __init__(self, start, stop=None, step=1):
        '''Initalize a Range instance.
        Semantic is similar to built-in range class.'''
        if step == 0:
            raise ValueError('step cannot be zero')

        if stop is None:            #special case of range(n)
            start, stop = 0, start  #should be trated as if range(0,n)

        """Calculate the effective length once."""
        self._length = max(0, (stop - start + step - 1)//step)

        """need knowledge of start and step (but not step) to suppport __getitem__"""
        self._start = start
        self._step = step

    def __len__(self):
        '''Return number of entries in the range.'''
        return self._length

    def __getitem__(self, k):
        """Return at index k (using standard interpretation if negative)."""
        if k < 0:
            k += len(self)          #attempt to convert negative index
        
        if not 0 <= k <self._length:
            raise IndexError('Index out of range')

        return self._start + k * self._step

if __name__ == "__main__":
    start = int(input())
    r = Range(start)
    print(r.__len__())
    print(r.__getitem__(4))