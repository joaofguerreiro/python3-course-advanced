import argparse

def get_args():
	"""Simple method of a parser demo without arguments."""
	parser = argparse.ArgumentParser(
		description="A simple argument parser",
		epilog="This is where you might put example usage"
	)
	return parser.parse_args()

if __name__ == '__main__':
	get_args()
