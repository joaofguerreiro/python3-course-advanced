"""
Concurrent.futures module provides the developer with a high-level interface 
for asynchronously executing callables. Basically concurrent.futures is an 
abstraction layer on top of Python's threading and multiprocessing modules that 
simplifies using them.

The future is a way to describe the result of a process or thread
before it has finished processing. Kinda like a pending result.
"""
import os
import urllib.request

from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed


def downloader(url):
	"""
	Downloads the specified URL and saves it to disk
	"""
	req = urllib.request.urlopen(url)
	filename = os.path.basename(url)
	ext = os.path.splitext(url)[1]  # checks that the URL ends with an extension
	if not ext:
		raise RunTimeError('URL does not contain an extension')

	with open(filename, 'wb') as file_handle:
		while True:
			chunk = req.read(1024)
			if not chunk:
				break
			file_handle.write(chunk)
	msg = 'Finished downloading {filename}'.format(filename=filename)
	return msg


def main(urls):
	"""
	Create a thread pool and download specified urls
	"""
	with ThreadPoolExecutor(max_workers=5) as executor:  # instantiates the thread pool which has 5 worker threads
		
		# Using futures
		# futures = [executor.submit(downloader, url) for url in urls]
		# for future in as_completed(futures):  # yields each future as it completes
		# 	print (future.result())

		# Using a Pool
		# map takes a function and an iterable and then calls the function for each item in the iterable
		return executor.map(downloader, urls, timeout=60)  # stops a thread that hangs for 60 seconds


if __name__ == '__main__':
	urls = ["http://www.irs.gov/pub/irs-pdf/f1040.pdf",
			"http://www.irs.gov/pub/irs-pdf/f1040a.pdf",
			"http://www.irs.gov/pub/irs-pdf/f1040ez.pdf",
			"http://www.irs.gov/pub/irs-pdf/f1040es.pdf",
			"http://www.irs.gov/pub/irs-pdf/f1040sb.pdf"]
	results = main(urls)
	for result in results:
		print (result)
# Finished downloading f1040ez.pdf
# Finished downloading f1040sb.pdf
# Finished downloading f1040a.pdf
# Finished downloading f1040.pdf
# Finished downloading f1040es.pdf
