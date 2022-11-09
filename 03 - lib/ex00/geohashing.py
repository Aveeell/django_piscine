import antigravity
import sys

if __name__ == '__main__':
	if len(sys.argv) != 4:
		exit("Invalid arguments")
	try:
		lat = float(sys.argv[1])
		long = float(sys.argv[2])
	except:
		exit("wrong coords")
	try:
			str = sys.argv[3].encode('utf-8')
	except:
		exit("need a string")
	antigravity.geohash(lat, long, str)
