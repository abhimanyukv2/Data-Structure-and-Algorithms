'''Our Range class, from Section 2.3.5, relies on the formula max(0, (stop −start + step −1) // step) to compute the number of elements in the range. It is not immediately evident why this formula provides the correct calculation, even if assuming a positive step size. Justify this formula, in your own words.'''

class Range:
    '''A class that mimic's the built-in range class.'''

    def __init__(self, start, stop=None, step=1):
        '''Initialize a Range instance.
        Semantics is similar to built-in range class.'''

        if step == 0:
            raise ValueError('step cannot be 0')

        if stop is None:                # special case of range(n)
            start, stop = 0, start      # should be treated as if range(0, n)

        # calculate the effective length once
        self._length = max(0, (stop - start + step - 1) // step)

        # need knowledge of start and step (but not stop) to support __getitem__
        self._start = start
        self._step = step

    def __len__(self):
        '''Return number of entries in the range.'''
        return self._length

    def __getitem__(self, k):
        '''Return entry at index k (using standard interpretation if negative).'''
        if k < 0:
            k += len(self)              # attempt to convert negative index

        if not 0 <= k < self._length:
            raise IndexError('index out of range')

        return self._start + k * self._step

'''
Range = max(0, (stop - start + step - 1) // step)

We substract the start from the stop to get the length of the range. 
length = stop - start

We then add the step - 1 to the length to get the number of steps. 
steps = length + step - 1

We then divide the number of steps by the step to get the number of elements in the range. 
num_elements = steps // step

We then take the max of 0 and the number of elements in the range to get the number of elements in the range. 
num_elements = max(0, num_elements)

If the number of elements in the range is negative, we return 0. If the number of elements in the range is positive, we return the number of elements in the range.
'''