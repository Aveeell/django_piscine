import sys

def get_elem(text):
	text = 'name:' + text
	arr = text.replace(' = ', ', ').split(', ')
	elem = dict((i.split(':') for i in arr))
	return elem

def parse_file():
	dct = []
	with open ('periodic_table.txt', 'r') as file:
		file = file.read().strip('\n').split('\n')
	for i in file:
		dct.append(get_elem(i))
	return dct

if __name__ == '__main__':
	elems = parse_file()
	html = '''
	<!DOCTYPE html>
	<html>
		<head>
			<title>periodic_table</title>
		</head>
		<style>
			table, td {{
				border-style: solid;
				border-radius: 5px;
				border-color: #424242;
			}}
			#name {{
				color: red;
			}}
		</style>
		<body>
			<div>
				<table>
					{table}
				</table>
			</div>
		</body>
	</html>
	'''
	table = '''
						<td>
							<h4 id="name">{name}</h4>
							<ul>
								<li>{position}</li>
								<li>{number}</li>
								<li id="name">{small}</li>
								<li>{molar}</li>
								<li>{electron}</li>
							</ul>
						</td>'''
	
	
	position = 0
	template = ''
	for i in elems:
		while position < int(i['position']):
			template += '<td></td>'
			position += 1
		if position == 0:
			template += '<tr>'
		elif position > int(i['position']):
			position = 0
			template += '</tr>'
		template += table.format(name = i['name'], 
									position=i['position'],
									number = i['number'],
									small = i['small'],
									molar = i['molar'],
									electron = i['electron'])
		position += 1

	html = html.format(table = template)

	with open ('1.html', 'w') as file:
		file.write(html)
