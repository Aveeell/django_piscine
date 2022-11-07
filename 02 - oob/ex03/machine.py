import beverages as b
import random

class CoffeeMachine:
	class EmptyCup(b.HotBeverage):
		def __init__(self) -> None:
			self.name = 'empty cup'
			self.price = 0.90

		def description(self):
			return 'An empty cum?! Gimme my money back!'

	class BrokenMachineException(Exception):
		def __init__(self, *args: object) -> None:
			super().__init__("This coffee machine has to be repaired.")

	def __init__(self) -> None:
		self.points = 10

	def repair(self):
		self.points = 10

	def serve(self, drink: b.HotBeverage()):
		if self.points <= 0:
			raise CoffeeMachine.BrokenMachineException
		self.points -= 1
		if random.randint(0, 5) == 0:
			return CoffeeMachine.EmptyCup()
		return drink()

if __name__ == '__main__':
	machine = CoffeeMachine()

	print(machine.serve(b.Coffee))
	print(machine.serve(b.Cappucino))
	print(machine.serve(b.Tea))
	print(machine.serve(b.Chocolate))
	for i in range(0,6):
		machine.serve(b.Chocolate)
	
	try:
		machine.serve(b.Chocolate)
	except Exception as exc:
		print('\n')
		print(exc)


