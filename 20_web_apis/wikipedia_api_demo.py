import wikipedia


print (wikipedia.search('Python'))
# ['Python', 'PYTHON', 'Monty Python', 'Python (programming language)', 'Python molurus', 
# 'Python (missile)', 'Burmese python', 'Ball python', 'Python curtus', 'African rock python']

print (wikipedia.summary('Python (programming language'))
# Python is a widely used high-level programming language for general-purpose programming, 
# created by Guido van Rossum and first released in 1991. An interpreted language, Python 
# has a design philosophy that emphasizes code readability (notably using whitespace 
# 	indentation to delimit code blocks rather than curly brackets or keywords), 
# and a syntax that allows programmers to express concepts in fewer lines of code 
# than might be used in languages such as C++ or Java. The language provides constructs 
# intended to enable writing clear programs on both a small and large scale.
# Python features a dynamic type system and automatic memory management and 
# supports multiple programming paradigms, including object-oriented, imperative, 
# functional programming, and procedural styles. It has a large and comprehensive standard library.
# # Python interpreters are available for many operating systems, allowing Python code 
# to run on a wide variety of systems. CPython, the reference implementation of Python, 
# is open source software and has a community-based development model, as do nearly all 
# of its variant implementations. CPython is managed by the non-profit Python Software Foundation.


def print_wikipedia_results(word):
	"""
	Searches for pages that match the specified word
	"""
	results = wikipedia.search(word)

	for result in results:
		try:
			page = wikipedia.page(result)
		except wikipedia.exceptions.DisambiguationError:
			print ('DisambiguationError')
			continue
		except wikipedia.exceptions.PageError:
			print ('PageError for result: ' + result)
			continue

		print (page.summary.encode('utf-8'))


if __name__ == '__main__':
	print_wikipedia_results('wombat')
	# TL;DR
	# b'Wombat is a town in South West Slopes region of New South Wales, Australia. 
	# It is situated on the Olympic Highway, 15 kilometres (9.3 mi) south-west of the 
	# regional centre of Young. It is in the local government area of Hilltops Council. 
	# Wombat has a population of approx 180.'
	# b"The Curse of the Flying Wombat is a 13-part serial of the British radio comedy series 
	# I'm Sorry, I'll Read That Again. It was written by Graeme Garden and Bill Oddie."
	# PageError for result: Wombat (TV series)


page = wikipedia.page('Python (programming language)')
print (page)
# <WikipediaPage 'Python (programming language)'>

print (page.title)
# Python (programming language)

print (page.url)
# https://en.wikipedia.org/wiki/Python_(programming_language)

print (page.content.encode('utf-8'))
# TL;DR
# b'Python is a widely used high-level programming language for general-purpose programming, 
# created by Guido van Rossum and first released in 1991. An interpreted language, Python has 
# a design philosophy that emphasizes code readability (notably using whitespace indentation to 
# 	delimit code blocks rather than curly brackets or keywords), and a syntax that allows 
# programmers to express concepts in fewer lines of code than might be used in languages such 
# as C++ or Java. The language provides constructs intended to enable writing clear programs on 
# both a small and large scale.\nPython features a dynamic type system and automatic memory 
# management and supports multiple programming paradigms, including object-oriented, imperative, 
# functional programming, and procedural styles. It has a large and comprehensive standard library.\n
# Python interpreters are available for many operating systems, allowing Python code to run on a wide 
# variety of systems. CPython, the reference implementation of Python, is open source software and has 
# a community-based development model, as do nearly all of its variant implementations.


print (wikipedia.set_lang('fr'))
# None

page = wikipedia.page('Python (programming language)')
print (page.summary.encode('utf-8'))
# TL;DR
# b"Python est un langage de programmation objet, multi-paradigme et multiplateformes. 
# Il favorise la programmation imp\xc3\xa9rative structur\xc3\xa9e, fonctionnelle et 
# orient\xc3\xa9e objet. Il est dot\xc3\xa9 d'un typage dynamique fort, d'une gestion 
# automatique de la m\xc3\xa9moire par ramasse-miettes et d'un syst\xc3\xa8me de gestion 
# d'exceptions ; il est ainsi similaire \xc3\xa0 Perl, Ruby, Scheme, Smalltalk et Tcl.\nLe 
# langage Python est plac\xc3\xa9 sous une licence libre proche de la licence BSD et fonctionne 
# sur la plupart des plates-formes informatiques, des supercalculateurs aux ordinateurs centraux, 
# de Windows \xc3\xa0 Unix avec notamment GNU/Linux en passant par macOS, ou encore Android, iOS, 
# et aussi avec Java ou encore .NET. Il est con\xc3\xa7u pour optimiser la productivit\xc3\xa9 
# des programmeurs en offrant des outils de haut niveau et une syntaxe simple \xc3\xa0 utiliser.
# \nIl est \xc3\xa9galement appr\xc3\xa9ci\xc3\xa9 par certains p\xc3\xa9dagogues qui y trouvent 
# un langage o\xc3\xb9 la syntaxe, clairement s\xc3\xa9par\xc3\xa9e des m\xc3\xa9canismes de bas 
# niveau, permet une initiation ais\xc3\xa9e aux concepts de base de la programmation."
