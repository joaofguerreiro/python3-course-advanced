import urllib.request

url = urllib.request.urlopen('https://www.google.com')
print (url.geturl())  # returns the URL of the resource that was retrieved.
# https://www.google.pt/?gfe_rd=cr&dcr=0&ei=Ag25WY_dC-mJ8QfK_Z64DA

header = url.info()  # returns meta-data about the page, such as headers.
print (header.as_string())
# Date: Wed, 13 Sep 2017 10:49:29 GMT
# Expires: -1
# Cache-Control: private, max-age=0
# Content-Type: text/html; charset=ISO-8859-1
# P3P: CP="This is not a P3P policy! See https://www.google.com/support/accounts/answer/151657?hl=en for more info."
# Server: gws
# X-XSS-Protection: 1; mode=block
# X-Frame-Options: SAMEORIGIN
# Set-Cookie: NID=112=o_u4I64-K2c2K05NhF17z6CeVgvrLJzDmGqE-uB7L8z29cdOtns-Ee29qSeSwSKx7x8vKir_6CF-dBll2TD7cRoP0fBOXaYjdQBkBCxyFFKejoEBMGLq8isHQX08Q5XP; expires=Thu, 15-Mar-2018 10:49:29 GMT; path=/; domain=.google.pt; HttpOnly
# Alt-Svc: quic=":443"; ma=2592000; v="39,38,37,35"
# Accept-Ranges: none
# Vary: Accept-Encoding
# Connection: close

print (url.getcode())  # the HTTP response code 
# 200


# ============== DOWNLOADING A FILE ==============
url = 'http://www.blog.pythonlibrary.org/wp-content/uploads/2012/06/wxDbViewer.zip'
response = urllib.request.urlopen(url)  # GET request to the url
data = response.read()
with open('test.zip', 'wb') as fobj:
	fobj.write(data)


url = 'http://www.blog.pythonlibrary.org/wp-content/uploads/2012/06/wxDbViewer.zip'
tmp_file, header = urllib.request.urlretrieve(url)  # Copies a network object to a local file.
# The file it copies to is randomly named and goes into the temp directory unless you use the second 
# parameter to urlretrieve where you can actually specify where you want the file saved. 
with open('test.zip', 'wb') as fobj:
	with open(tmp_file, 'rb') as tmp:
		fobj.write(tmp.read())


# When you visit a website with your browser, the browser tells the website who it is. 
# This is called the user-agent string. 
user_agent = ' Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0'
url = 'http://www.whatsmyua.com/'
headers = {'User-Agent': user_agent}
request = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(request) as response:
	with open('test.html', 'wb') as out:
		out.write(response.read())  # we successfully changed our user-agent string.


# ============== PARSING a URL ==============
from urllib.parse import urlparse
import urllib.parse

# We import the urlparse function and pass it an URL that contains a search query to the duckduckgo website.
result = urlparse('https://duckduckgo.com/?q=python+stubbing&t=canonical&ia=qa')
print (result)
# ParseResult(scheme='https', netloc='duckduckgo.com', path='/', params='', query='q=python+stubbing&t=canonical&ia=qa', fragment='')

print (result.netloc)
# duckduckgo.com

print ( result.geturl())
# https://duckduckgo.com/?q=python+stubbing&t=canonical&ia=qa

print (result.port)
# None


data = urllib.parse.urlencode({'q': 'Python'})  # query using Python instead of browser
print (data)
# q=Python

url = 'http://duckduckgo.com/html/'
full_url = url + '?' + data
response = urllib.request.urlopen(full_url)
with open('results.html', 'wb') as f:
	f.write(response.read())


# ============== ROBOTPARSER ==============
import urllib.robotparser

robot = urllib.robotparser.RobotFileParser()
 # This class will answer questions about whether or not a specific user agent can 
 # fetch a URL that has a published robots.txt file.

# The robots.txt file will tell a web scraper or robot what parts of the server should not be accessed.
print (robot.set_url('http://arstechnica.com/robots.txt'))
# None

print (robot.read())  # We tell our parser to read the file.
# None

print (robot.can_fetch('*', 'http://arstechnica.com/'))
# True

print (robot.can_fetch('*', 'http://arstechnica.com/cgi-bin/'))
# False

