"""Write a set of Python classes that can simulate an Internet application
in which one party, Alice, is periodically creating a set of packets that
she wants to send to Bob. An Internet process is continually checking if
Alice has any packets to send, and if so, it delivers them to Bob’s computer,
and Bob is periodically checking if his computer has a packet from Alice, and,
if so, he reads and deletes it."""

import time
import random


class InternetBot:
	"""Simulate an Internet application."""

	def __init__(self, name, packets):
		"""Create a new InternetBot instance.

		name    the name of the bot
		packets the list of packets to be sent
		"""
		self._name = name
		self._packets = packets

	def send(self, receiver):
		"""Send a packet to the receiver."""
		if self._packets:
			packet = self._packets.pop(0)
			print(f'{self._name} sends {packet} to {receiver._name}')
			receiver.receive(packet)

	def receive(self, packet):
		"""Receive a packet."""
		print(f'{self._name} receives {packet}')
		print(f'{self._name} reads {packet}')
		print(f'{self._name} deletes {packet}')
		# self._packets.pop()

	def has_packets(self):
		"""Return True if the bot has packets to send."""
		return bool(self._packets)


class Alice(InternetBot):
	"""Simulate Alice, who sends packets to Bob."""

	def __init__(self, packets):
		"""Create a new Alice instance."""
		super().__init__('Alice', packets)

	def create_packets(self):
		"""Create a new packet to send to Bob."""
		packet = random.randint(1, 100)
		self._packets.append(packet)
		print(f'Alice creates packet {packet}')

	def check_packets(self):
		"""Check if Alice has packets to send."""
		return self.has_packets()

	def send_packets(self, receiver):
		"""Send a packet to Bob."""
		if self.has_packets():
			self.send(receiver)


class Bob(InternetBot):
	"""Simulate Bob, who receives packets from Alice."""

	def __init__(self):
		"""Create a new Bob instance."""
		super().__init__('Bob', [])

	def check_packets(self):
		"""Check if Bob has packets to receive."""
		return self.has_packets()

	def receive_packets(self, sender):
		"""Receive a packet from Alice."""
		if self.has_packets():
			self.receive(sender)

	def read_packets(self, sender):
		"""Read a packet."""
		if self.receive_packets(sender):
			packet = self._packets.pop(0)
			print(f'Bob reads packet {packet}')

	def delete_packets(self, packet):
		"""Delete a packet."""
		if self.read_packets(packet):
			self._packets.pop(0)
			print(f'Bob deletes packet {packet}')


if __name__ == '__main__':
	alice = Alice([])
	bob = Bob()

	while True:
		alice.create_packets()
		alice.send_packets(bob)
		# bob.receive_packets(alice)
		# bob.read_packets(alice)
		bob.delete_packets(alice)
		time.sleep(1)