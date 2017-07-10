import argparse
import os

from collections import ChainMap


def main():
	"""
	Some example outputs:
	○ → python3 chain_map_demo.py
	admin
	test

	○ → python3 chain_map_demo.py -u joao 
	joao
	joao
	"""
	app_defaults = {
		'username': 'admin',
		'password': 'admin'
	}

	parser = argparse.ArgumentParser()
	parser.add_argument('-u', '--username')
	parser.add_argument('-p', '--password')
	args = parser.parse_args()
	command_line_arguments = {key:value for key, value in vars(args).items() if value}

	# the dictionary with the highest priority should be assigned first in the ChainMap
	chain = ChainMap(command_line_arguments, os.environ, app_defaults)
	print (chain['username'])

if __name__ == '__main__':

	main()
	os.environ['username'] = 'test'
	main()
