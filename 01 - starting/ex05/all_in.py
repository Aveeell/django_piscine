import sys

def get_key(city):
	capital_cities = {
		"OR": "Salem",
		"AL": "Montgomery",
		"NJ": "Trenton",
		"CO": "Denver"
	}
	for i in capital_cities:
		if capital_cities.get(i) == city:
			return i
	return None
def get_value(city):
	states = {
		"Oregon" : "OR",
		"Alabama" : "AL",
		"New Jersey": "NJ",
		"Colorado" : "CO"
	}
	key = get_key(city.capitalize())
	if key:
		for i in states:
			if states.get(i) == key:
				print(city.capitalize() + " is the capital of " + i)
	else:
		print(city + " is neither a capital city nor a state")


if __name__ == '__main__':
	if len(sys.argv) != 2:
		exit()
	arr = sys.argv[1].split(", ")
	for i in arr:
		if len(i) > 0:
			get_value(i)

