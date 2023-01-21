'''When using the ArithmeticProgression class of Section 2.4.2 with an increment of 128 and a start of 0, how many calls to next can we make before we reach an integer of 2**63 or larger?'''

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

class ArithmeticProgression(Progression):               # inherit from Progression
    '''Iterator producing an arithmetic progression.'''
    def __init__(self, increment=1, start=0):
        '''Create a new arithmetic progression.
        increment   the fixed constant to add to each term (default 1)
        start       the first term of the progression (default 0)'''
        super().__init__(start)                         # initialize base class
        self._increment = increment                     # initialize the increment

    def _advance(self):                                 # override inherited version
        '''Update current value by adding the fixed increment.'''
        self._current += self._increment

if __name__ == "__main__":
    print('Arithmetic progression with increment 128 and start 0:')
    print('We have to call 72,05,75,94,03,79,27,936 times to next() to reach 2**63 or larger.')
    ArithmeticProgression(128, 0).print_progression(72057594037927936)