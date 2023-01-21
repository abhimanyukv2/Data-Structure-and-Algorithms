class Progression:
    '''Iterator producing a generic progression.
    Default iterator produce the whole numbers 0, 1, 2, ...'''
    
    def __init__(self, start=0):
        '''Initilize the current to the first value of the expression.'''
        self._current = start

    def _advance(self):
        '''Update self._current to a new value
        This should be overridden by a subclass to customize progression.
        By convention, if current is set to None, this designates the end of a finite progression'''
        self._current += 1

    def __next__(self):
        '''Return the next element, or else raise StopIteration error.'''
        if self._current is None:       #our convention to end a progression
            raise StopIteration()
        else:
            answer = self._current      #record current value to return
            self._advance()             #advance to prepare for next time
            return answer

    def __iter__(self):
        '''By convention, an iterator must return itself as an iterator.'''
        return self

    def print_progression(self, n):
        '''Print next n values of the progression.'''
        print(' '.join(str(next(self)) for j in range(n)))

class ArithmeticProgression(Progression):       #inherit from progression
    '''Iterator producing an arthmetic progression.'''

    def __init__(self,increment=1, start=0):
        '''Create a new arithmetic operation.
        increment   the fixed constent to add to each term (default 1)
        start       the first term of the progression (default 0)'''
        super().__init__(start)             # initialize base class
        self._increment = increment

    def _advance(self):                     # override inherited version
        '''Update current value by adding the fixed increment.'''
        self._current += self._increment

if __name__ == "__main__":
    print("Arithmetic Progression with increment 5:")
    ArithmeticProgression(5).print_progression(10)

    print("Arithmetic Progression with increment 5 and start 2:")
    ArithmeticProgression(5,2).print_progression(10)

    increment = int(input())
    start = int(input())
    print('Arithmetic progression with increment {increment} and start {start}')
    AP = ArithmeticProgression(increment, start)
    n =int(input())
    AP.print_progression(n)