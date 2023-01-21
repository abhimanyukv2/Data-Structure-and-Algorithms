"""Write a Python program that inputs a document and then outputs a barchart
 plot  of the  frequencies  of each  alphabet  character  that  appears
 in that document."""

import matplotlib.pyplot as plt
import string


class Document:
    """Creating a Document class."""

    def __init__(self, file_name):
        """Create a new document."""
        self._file_name = file_name
        self._document = self._create_document()

    def _create_document(self):
        """Create a document."""
        with open(self._file_name, 'r') as file:
            document = file.read()
        return document

    def __str__(self):
        """Return the document."""
        return self._document

    def __repr__(self):
        """Return the document."""
        return self._document

    def get_frequency(self):
        """Return the frequency of each alphabet character."""
        frequency = {}
        for char in self._document:
            if char in string.ascii_letters:
                if char in frequency:
                    frequency[char] += 1
                else:
                    frequency[char] = 1
        return frequency

    def plot(self):
        """Plot the frequency of each alphabet character."""
        frequency = self.get_frequency()
        plt.bar(frequency.keys(), frequency.values())
        plt.show()


if __name__ == '__main__':
    document = Document('P2_35.py')
    document.plot()
