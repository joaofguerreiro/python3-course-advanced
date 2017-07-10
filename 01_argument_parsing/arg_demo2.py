import argparse

def get_args():
	"""
	Simple method of a parser demo with required and optional arguments.
	
	'--first-name' is the long-option argument name
	python3 arg_demo2.py --first-name something
	works the same way as
	python3 arg_demo2.py -x something
	"""
	parser = argparse.ArgumentParser(
		description="A simple argument parser",
		epilog="This is where you might put example usage"
	)

	# required argument
	parser.add_argument('-x', '--first-name', action="store", required=True, help='Help text for option X')
	# '--first-name' is the long-option argument name

	# python3 arg_demo2.py --first-name something
	# python3 arg_demo2.py -x something


	# optional argument
	parser.add_argument('-y', help='Help text for option Y', default=False)
	parser.add_argument('-z', help='Help text for option Z', type=int)
	print(parser.parse_args())

if __name__ == '__main__':
	get_args()
