def read_and_print():
	with open ('numbers.txt', 'r') as file:
		res = file.read().split(',')
	for i in res:
		print(int(i))

if __name__ == '__main__':
	read_and_print()