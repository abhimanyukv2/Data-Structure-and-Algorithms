'''Give a short fragment of Python code that uses the progression classes from Section 2.4.2 to find the 8th value of a Fibonacci progression that starts with 2 and 2 as its first two values.'''

class Progression:
    '''Iterator producing a generic progression.
    Default iterator produces the whole number 0, 1, 2, ...'''

    def __init__(self, start=0):
        '''Initilize the current to the first value of the progression.'''
        self._current = start

    def _advance(self):
        '''Update self._current to a new value.
        This should be overridden by the sub class to customize progression.
        By convention, if current is set to None, this designates the end of a fine progression.'''

        self._current += 1

    def __next__(self):
        '''Return the next element, or raise StopIteration error.'''
        if self._current is None:           # our convention to end a progression
            raise StopIteration
        else:
            answer = self._current          # record current value to return
            self._advance()                 # advance to prepare for the next time
            return  answer                  # return the answer

    def print_progression(self, n):
        '''Print next n values of the progrression.'''
        print(' '.join(str(next(self)) for j in range(n)))

class FibonacciProgression(Progression):
    '''Iterator producing a generalizes Fibonacci progression.'''
    def __init__(self, first=0, second=1):
        '''Create a new fibonacci progression.
        first       the fist term of the progression (default 0)
        second      the second term of the progression (default 1)'''

        super().__init__(first)         # start progression at first
        self._previous = second - first # fixtitious value preceding the first

    def _advance(self):
        '''Update current vallue by taking sum of previous two.'''
        self._previous, self._current = self._current, self._previous + self._current

if __name__ == "__main__":
    print('Fibonacci progression with start value 2 and 2:')
    FibonacciProgression(2, 2).print_progression(8)