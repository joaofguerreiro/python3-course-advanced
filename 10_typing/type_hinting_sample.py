def some_function(number: int, name: str) -> None:
	print ("%s entered %s" % (name, number))

print (some_function(13, 'Mike'))
# Mike entered 13
# None

def process_data(my_list: list, name:str) -> bool:
	return name in my_list

if __name__ == '__main__':
	my_list = ['Mike', 'Nick', 'Toby']
	print (process_data (my_list, 'Mike'))
	print (process_data (my_list, 'John'))
# True
# False
