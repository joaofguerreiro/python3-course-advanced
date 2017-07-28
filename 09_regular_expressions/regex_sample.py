"""
Matching characters in a string.

d: Matches digit - [\d] is the equivalent of [0-9]

D: Matches non-digit

s: Matches whitespace

S: Matches non-whitespace

w: Matches alphanumeric

W: Matches non-alphanumeric
"""
import re
text = 'abcdefghijk'
parser = re.search('a[b-f]*f', text)
print (parser)
# <_sre.SRE_Match object; span=(0, 6), match='abcdef'>

print (parser.group())
# abcdef

# xb{1,4}z will match xbz, xbbz, xbbbz and xbbbbz, but not xz because it doesn’t have a “b”.
# co-?op will match both coop and co-op.
# [^a] will match any character except the letter 'a'.

text = "The ants go marching one by one"
strings = ['the', 'one']

for string in strings:
	# loop over the strings we plan to search for and actually run a search for them
	match = re.search(string, text)
	if match:
		print ('Found "{}" in "{}"'.format(string, text))
		text_pos = match.span()
		print (text[match.start():match.end()])
	else:
		print ('Did not find "{}"'.format(string))
# Did not find "the"
# Found "one" in "The ants go marching one by one"
# one


for string in strings:
	regex = re.compile(string) # saves it to be reused later on in the code

	# When you compile patterns, they will get automatically cached so if 
	# you aren’t using lot of regular expressions in your code, then you 
	# may not need to save the compiled object to a variable.
	match = re.search(regex, text)
	if match:
		print ('Found "{}" in "{}"'.format(string, text))
		text_pos = match.span()
		print (text[match.start():match.end()])
	else:
		print ('Did not find "{}"'.format(string))
# Did not find "the"
# Found "one" in "The ants go marching one by one"
# one


"""
Finding multiple instances in a string.
"""
silly_string = "the cat in the hat"
pattern = "the"
match = re.search(pattern, silly_string)
print (match.group())
# the
print (re.findall(pattern, silly_string))  # adds each match to a list
# ['the', 'the']


for match in re.finditer(pattern, silly_string):  # returns an iterator of Match instances instead of the strings
	s = "Found '{group}' at {begin}:{end}".format(
		group=match.group(), begin=match.start(),
		end=match.end())
	print (s)
# Found 'the' at 0:3
# Found 'the' at 11:14
