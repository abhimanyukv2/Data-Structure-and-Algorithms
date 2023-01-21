"""Write a Python program that simulates a system that supports the functions
of an e-book reader. You should include methods for users of your system to
“buy” new books, view their list of purchased books, and read their purchased
books. Your system should use actual books, which have expired copyrights
and are available on the Internet, to populate your set of available books
for users of your system to “purchase” and read."""


import time
import random
from pathlib import Path
from IPython.display import clear_output


class EBookReader:
	"""Creating a EBookReader class."""

	class Book:
		"""Creating a Book class."""

		MIN_PRICE = 0.99
		MAX_PRICE = 49.99
		LICENSE_DURATION = 365 * 24 * 60 * 60  # 1 year in seconds
		LINES_PER_PAGE = 50

		def __init__(self, filepath):
			"""Create a new Book instance."""
			self._name = str(filepath.name).replace('.txt', '')
			self._filepath = filepath
			self._price = random.uniform(self.MIN_PRICE, self.MAX_PRICE)
			self._license_start_time = time.time()
			self._license_end_time = self._license_start_time + self.LICENSE_DURATION
			self._purchased = False
			self._current_position = 0
			self._iostream = open(self._filepath, encoding='utf-8')
			self._length = self.determine_lenght()

		def __repr__(self):
			"""Return the string representation of a Book object."""
			return f'Book: {self._name}, Price: {self._price}, Purchased: {self._purchased}'

		def puchase_book(self):
			"""Puchase a book."""
			self._purchased = True
			self._current_position = 0
			self._iostream.seek(0)

		def open_book(self):
			"""Open a book."""
			if self._purchased:
				self._iostream.seek(self._current_position)
				return open(self._filepath, encoding='utf-8')
			else:
				raise Exception('Book is not purchased.')

		def seek_path(self, page=0):
			"""Seek to a position in the book."""
			self._iostream.seek(0)
			num_lines = page * self.LINES_PER_PAGE
			for _ in range(num_lines):
				self._iostream.readline()

		def read_book(self, page=None):
			"""Read a book."""
			if not self._purchased:
				raise Exception('Book is not purchased.')
			else:
				if page is None:
					start = self._current_position
				else:
					start = page
				print(start)
				self.seek_path(start)
				for _ in range(self.LINES_PER_PAGE):
					print(self._iostream.readline(), end='')
				self._current_position = start + 1
				return True

		def __len__(self):
			"""Return the length of the book."""
			return self._length

		def __getitem__(self, item):
			"""Return the item of the book."""
			if isinstance(item, int) and 0 < item < len(self):
				self.read_book(item)
			else:
				raise Exception('Invalid page number.')

		def determine_lenght(self):
			"""Determine the length of the book."""
			self._iostream.seek(0)
			num_lines = self._iostream.readlines()
			return len(num_lines) // self.LINES_PER_PAGE

	def __init__(self, book_dir='books'):
		"""Create a new EBookReader instance."""
		self._book_dir = Path(book_dir)
		self._library = self._bulid_book_directory()
		self._balance = 0
		self._current_book = None
		self._status_message = 'Nothing to report.'

	def load_money(self, amount):
		"""Load money into the EBookReader."""
		self._balance += amount
		self._status_message = f'${amount} added to your balance.'

	def output_status(self):
		"""Output the status of the EBookReader."""
		print(self._status_message)

	def purchase_book(self, book_name):
		"""Purchase a book."""
		if book_name in self._library:
			book = self._library[book_name]
			if book._purchased:
				self._status_message = 'You already own this book.'
			if book._price <= self._balance:
				book.puchase_book()
				self._balance -= book._price
				self._status_message = f'You have purchased {book_name}.'
			else:
				self._status_message = f'You do not have enough money to purchase {book_name}.'
		else:
			self._status_message = f'{book_name} is not available.'

	def read_book(self, book_name, page=None):
		"""Read a book."""
		if book_name in self._library:
			book = self._library[book_name]
			if book._purchased:
				if page is None:
					book.read_book()
				else:
					book.read_book(page)
			else:
				self._status_message = f'You do not own {book_name}.'
		else:
			self._status_message = f'{book_name} is not available.'

	def _read_page(self, book_name, page=None):
		"""Read a page."""
		if book_name in self._library:
			book = self._library[book_name]
			if book._purchased:
				if page is None:
					book.read_book()
				else:
					book.read_book(page)
			else:
				self._status_message = f'You do not own {book_name}.'
		else:
			self._status_message = f'{book_name} is not available.'

	def _bulid_book_directory(self):
		"""Build the book directory."""
		library = {}
		for book in self._book_dir.glob('*.txt'):
			library[book.stem] = self.Book(book)
		return library

	def _print_library(self):
		"""Print the library."""
		for book in self._library:
			print(self._library[book])

	def _print_purchased_books(self):
		"""Print the purchased books."""
		for book in self._library:
			if self._library[book]._purchased:
				print(self._library[book])

	def _print_balance(self):
		"""Print the balance."""
		print(f'Balance: ${self._balance}')

	def __repr__(self):
		"""Return the string representation of a EBookReader object."""
		print('Library:', self._library)
		print('Balance:', self._balance)
		print('Current Book:', self._current_book)
		print('Status Message:', self._status_message)
		print('Book Directory:', self._book_dir)

	def console(self):
		"""Run the console."""
		clear_output()
		self._read_page(self._current_book)

		print(self)
		print('Commands: quit, library, purchased, balance, status, '
			  'load <amount>, purchase <book>, read <book> <page> (optional) ')
		input_result = self.get_input()
		return input_result



	def get_input(self):
		"""Get the input."""
		input_string = input('Enter a command: ')
		if input_string == 'quit':
			return False
		elif input_string.lower() == 'purchase':
			book_name = input('Enter the book name: ')
			self.purchase_book(book_name)
			return True
		elif input_string.lower() == 'read':
			book_name = input('Enter the book name: ')
			page = input('Enter the page number: ')
			self.read_book(book_name, int(page))
			return True
		elif input_string.lower() == 'load':
			amount = float(input('Enter the amount: '))
			self.load_money(amount)
			return True
		elif input_string.lower() == 'status':
			self.output_status()
			return True
		elif input_string.lower() == 'library':
			self._print_library()
			return True
		elif input_string.lower() == 'next':
			self._current_book.next_page()
			return True
		elif input_string.lower() == 'previous':
			self._current_book.previous_page()
			return True
		elif input_string.lower() == 'open':
			book_name = input('Enter the book name: ')
			self.read_book(book_name)
			return True
		elif input_string.lower() == 'close':
			self._current_book = None
			return True
		else:
			print('Invalid command.')
			return True


if __name__ == '__main__':
	ereader = EBookReader()
	ereader.console()
	# while ereader.get_input():
	# 	pass
