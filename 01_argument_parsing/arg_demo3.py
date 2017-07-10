import argparse

def get_args():
	"""
	Simple method of a parser demo with a mutually exclusive group.

	python3 arg_demo3.py -x 10 -y 2
	usage: arg_demo3.py [-h] [-x EXECUTE | -y Y] [-z Z]
	arg_demo3.py: error: argument -y: not allowed with argument -x/--execute
	"""
	parser = argparse.ArgumentParser(
		description="A simple argument parser",
		epilog="This is where you might put example usage"
	)

	group = parser.add_mutually_exclusive_group()
	group.add_argument('-x', '--execute', action="store", help='Help text for option X')
	group.add_argument('-y', help='Help text for option Y', default=False)

	parser.add_argument('-z', help='Help text for option Z', type=int)
	print(parser.parse_args())

if __name__ == '__main__':
	get_args()
