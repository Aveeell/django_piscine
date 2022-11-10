from path import Path

if __name__ == '__main__':
	try:
		Path.makedirs('directory')
	except FileExistsError as e:
		print(e)
	Path.touch('directory/file.txt')
	f = Path('directory/file.txt')
	f.write_lines(['hello world!'])
	print(f.read_text())
