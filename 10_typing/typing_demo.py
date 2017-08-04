class Fruit:
	def __init__(self, name, color):
		self.name = name
		self.color = color

def salad(fruit_one: Fruit, fruit_two: Fruit) -> list:
	print (fruit_one.name)
	print (fruit_two.name)
	return [fruit_one, fruit_two]


if __name__ == '__main__':
	f = Fruit('orange', 'orange')
	f2 = Fruit('apple', 'red')
	salad(f, f2)
# orange
# apple
