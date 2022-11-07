def make_dict(arr):
	arr = []
	for i in d:
		arr.append(list(i))
	for i in arr:
		i = i.reverse()
	for i in arr:
		i[0] = int(i[0])
	return dict(arr)

if __name__ == '__main__':
	d = [
		('Hendrix' , '1942'),
		('Allman' , '1946'),
		('King' , '1925'),
		('Clapton' , '1945'),
		('Johnson' , '1911'),
		('Berry' , '1926'),
		('Vaughan' , '1954'),
		('Cooder' , '1947'),
		('Page' , '1944'),
		('Richards' , '1943'),
		('Hammett' , '1962'),
		('Cobain' , '1967'),
		('Garcia' , '1942'),
		('Beck' , '1944'),
		('Santana' , '1947'),
		('Ramone' , '1948'),
		('White' , '1975'),
		('Frusciante', '1970'),
		('Thompson' , '1949'),
		('Burton' , '1939')
	]
	dct = make_dict(d)
	for i in dct:
		print(str(i) + " : " + dct.get(i))