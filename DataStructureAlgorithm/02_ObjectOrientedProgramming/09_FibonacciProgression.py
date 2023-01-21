class Progression:
    '''Iterator producing a greneric progression.
    Defeault iterator produce the whole number 0, 1, 2, ...'''

    def __init__(self, start=0):
        '''Initilize the current to the first value of the progression'''
        self._current = start

    def _advance(self):
        '''Update self._current to a new value.
        This should be overridden by a subclass to cutomize progression.
        By convention, if current is set to None, this designates the end of a finite progression.'''
        self._current += 1

    def __next__(self):
        '''Return the next element, or else raise StopIteration error.'''
        if self._current is None:       # our convention to end a progression
            raise StopIteration()
        else:
            answer = self._current      # record current value to return
            self._advance()             # advance to prepare for the next time
            return answer               # return the answer

    def __iter__(self):
        '''By convention, an iterator must return itself as an iteratoe.'''
        return self

    def print_progression(self, n):
        '''PRint next n value of the progression.'''
        print(' '.join(str(next(self)) for j in range(n)))

class FibonacciProgression(Progression):
    '''Iterator producing a generalized Fibonacci progression.'''

    def __init__(self, first=0, second=1):
        '''Create a new fibonacci progression.
        first       the first term of the progression (dafault 0)
        second      the second term of the progression (default 1)'''
        super().__init__(first)         # satrt progression at first
        self._prev = second - first     # fictitious value preceding the first

    def _advance(self):
        '''Update current value by taking sum of previous two.'''
        self._prev, self._current = self._current, self._prev + self._current

if __name__ == "__main__":
    print('Fibonacci progression with default start value:')
    FibonacciProgression().print_progression(10)

    print('Fibonacci progression with start value 4 and 6:')
    FibonacciProgression(4,6).print_progression(10)

    first = int(input())
    seceond = int(input())
    Fibo = FibonacciProgression(first, seceond)
    n = int(input())
    Fibo.print_progression(n)