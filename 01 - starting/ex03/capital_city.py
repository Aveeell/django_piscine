import sys

if __name__ == '__main__':
	states = {
		"Oregon" : "OR",
		"Alabama" : "AL",
		"New Jersey": "NJ",
		"Colorado" : "CO"
	}
	capital_cities = {
		"OR": "Salem",
		"AL": "Montgomery",
		"NJ": "Trenton",
		"CO": "Denver"
	}
	if len(sys.argv) < 2:
		exit()
	elif states.get(sys.argv[1]):
		print(capital_cities.get(states.get(sys.argv[1])))
	else:
		print("Unknown state")