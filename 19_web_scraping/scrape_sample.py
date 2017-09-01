"""
Web scraping is where a programmer will write an application to download 
web pages and parse out specific information from them.

Advice: 
Websites change all the time, so your scraper will break some day. 
Know this: You will have to maintain your scraper if you want it to keep working.
"""
import requests
from bs4 import BeautifulSoup
"""
One of the most popular HTML parsers for Python is called BeautifulSoup. 
It’s been around for quite some time and is known for being able to handle malformed HTML well.
"""

url = 'http://www.blog.pythonlibrary.org/'

def get_articles():
	"""
	Get the articles from the front page of the blog
	"""
	req = requests.get(url)  # HTTP GET request on the url
	html = req.text  # pulls the HTML as a string
	soup = BeautifulSoup(html, 'html.parser')  # transforms into a nice object thanks to BeautifulSoup
	pages = soup.findAll('h1')  # finds all the instances of 'h1' 

	articles = {i.a['href']: i.text.strip() for i in pages if i.a}  # sets a dictionary with all the 'h1' found

	for article in articles:
		s = '{title}: {url}'.format(title=articles[article].encode('utf-8'), url=article)
		print (s)

	return articles


if __name__ == '__main__':
	articles = get_articles()
# b'Back to School Python Book Sale 2017': http://www.blog.pythonlibrary.org/2017/08/28/back-to-school-python-book-sale-2017/
# b'PyDev of the Week: Shannon Turner': http://www.blog.pythonlibrary.org/2017/08/28/pydev-of-the-week-shannon-turner/
# b'PyDev of the Week: Katherine Scott': http://www.blog.pythonlibrary.org/2017/08/21/pydev-of-the-week-katherine-scott/
# b'PyDev of the Week: Brian E. Granger': http://www.blog.pythonlibrary.org/2017/08/14/pydev-of-the-week-brian-e-granger/
# b'Python 101: Recursion': http://www.blog.pythonlibrary.org/2017/08/10/python-101-recursion/
# b'PyDev of the Week: Dave Forgac': http://www.blog.pythonlibrary.org/2017/08/07/pydev-of-the-week-dave-forgac/
# b'ANN: Python 101 Website': http://www.blog.pythonlibrary.org/2017/08/03/ann-python-101-website/
# b'Python is #1 in 2017 According to IEEE Spectrum': http://www.blog.pythonlibrary.org/2017/07/23/python-is-1-in-2017-according-to-ieee-spectrum/
# b'Python: All About Decorators': http://www.blog.pythonlibrary.org/2017/07/18/python-all-about-decorators/
# b'PyDev of the Week on Hiatus': http://www.blog.pythonlibrary.org/2017/07/05/pydev-of-the-week-on-hiatus/
