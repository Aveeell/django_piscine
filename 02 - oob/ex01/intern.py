class Intern:
	class Coffee:
		def __str__(self) -> str:
			return 'This is the worst coffe you ever tasted.'

	def __init__(self, Name = None) -> None:
		if Name:
			self.Name = Name
		else:
			self.Name = 'My name? I\'m nobody, an intern, I have no name'

	def __str__(self) -> str:
		return self.Name

	def work(self):
		raise Exception("I'm just an intern, I can't do that...")

	def make_coffee(self):
		return Intern.Coffee()

if __name__ == '__main__':
	intern = Intern()
	int1 = Intern("Mark")

	print(intern.__str__())
	print(int1.__str__())

	try:
		intern.work()
	except Exception as exc:
		print(exc)

	print(intern.make_coffee())