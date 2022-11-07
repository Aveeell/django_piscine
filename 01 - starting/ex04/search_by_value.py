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
	else:
		for i in capital_cities:
			if capital_cities.get(i) == sys.argv[1]:
				for j in states:
					if states.get(j) == i:
						print(j)
						exit()
	print("Unknown capital city")