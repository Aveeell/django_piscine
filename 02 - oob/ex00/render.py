import re
import sys
import os

if __name__ == '__main__':
	if len(sys.argv) != 2 or sys.argv[1][-9:] != '.template' or not os.path.isfile(sys.argv[1]):
		exit('no template file')

	with open (sys.argv[1], 'r') as file:
		template = file.read()
	with open('settings.py', 'r') as file:
		settings = file.read()

	settings = dict((i.replace('"', '').split(' = ') for i in settings.split('\n')))
	tmp = re.findall(r'[{]\w*[}]', template)
	for i in tmp:
		try:
			template = template.replace(i, settings.get(i.strip('{}')))
		except TypeError:
			exit('TypeError')

		html = '''
	<!DOCTYPE html>
	<html>
		<head>
			<title>myCV</title>
		</head>
		<style>
			div {{
				border-style: solid;
				border-color: #424242;
				border-radius: 5px;
				width: 50%;
			}}
		</style>
		<body>
			<div>
					{template}
			</div>
		</body>
	</html>
	'''

	with open('file.html', 'w') as file:
		file.write(html.format(template = template))