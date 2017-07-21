class Doubler:
	"""
	An infinite iterator
	"""

	def __init__(self):
		"""
		Constructor
		"""
		self.number = 0

	def __iter__(self):
		"""
		Returns itself as an iterator
		"""
		return self

	def __next__(self):
		"""
		Doubles the number each time next is called and returns it
		"""
		self.number += 1
		return self.number * self.number


if __name__ == '__main__':
	doubler = Doubler()
	
	# To make sure we don’t end up in an infinite loop, we add a 
	# counter before we start iterating over our custom iterator
	count = 0

	for number in doubler:
		print (number)
		if count > 5:
			break
		count += 1
# 1
# 4
# 9
# 16
# 25
# 36
# 49
