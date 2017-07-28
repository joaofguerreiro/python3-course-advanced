"""
Python 3 has 7 compilation flags that can change the behaior of compiled patterns.

re.A / re.ASCII
Matches against ASCII instead of using full Unicode matching when coupled 
with the following escape codes: w, W, b, B, d, D, s and S. 

re.DEBUG
Displays debug information about the compiled expression.

re.I / re.IGNORECASE
To perform case-insensitive matching. Upper and lowercase letters are considered the same.

re.L / re.LOCALE
Makes the escape codes: w, W, b, B, d, D, s and S depend on the current locale. (Unreliable!)

re.M / re.MULTILINE
Makes the ^ pattern character match at both the beginning of the string and at the beginning of each line.
$ should match at the end of the string and the end of each line.

re.S / re.DOTALL
Makes the . (period) metacharacter match any character at all.

re.X / re.VERBOSE
Whitespace within the pattern will be ignored except when in a character class or when the whitespace
is preceded by an unescaped backslash.
"""
import re

# Using a compilation flag for a common email finding regex 
test = re.compile('''
	[\w\.-]+.  # the user name
	@
	[\w\.-]+'  # the domain
	''', 
	re.VERBOSE)
