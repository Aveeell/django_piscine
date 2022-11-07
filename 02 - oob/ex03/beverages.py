class HotBeverage:
	price = 0.30
	name = 'hot beverage'
	
	def description(self):
		return 'Just some hot water in a cup.'

	def __str__(self) -> str:
		descr = ('name : {name}\n'
				'price : {price:0.2f}\n'
				'description : {description}').format(name = self.name, price=self.price, description = self.description())
		return descr

class Coffee(HotBeverage):
	def __init__(self) -> None:
		self.name = "coffee"
		self.price = 0.40

	def description(self):
		return 'A coffee, to stay awake.'

class Tea(HotBeverage):
	def __init__(self) -> None:
		self.name = 'tea'

class Chocolate(HotBeverage):
	def __init__(self) -> None:
		self.name = 'chocolate'
		self.price = 0.50

	def description(self):
		return 'Chocolate, sweet chocolate...'

class Cappucino(HotBeverage):
	def __init__(self) -> None:
		self.name = "cappucino"
		self.price = 0.45

	def description(self):
		return 'Un po\' di Italia nella sua tazza!'