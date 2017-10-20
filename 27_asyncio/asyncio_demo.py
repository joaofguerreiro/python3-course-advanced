import asyncio
import os
import urllib.request


async def download_coroutine(url):
	"""
	A coroutine to download the specified url
	"""
	request = urllib.request.urlopen(url)
	filename = os.path.basename(url)

	with open(filename, 'wb') as file_handle:
		while True:
			chunk = request.read(1024)
			if not chunk:
				break
			file_handle.write(chunk)
	msg = 'Finished downloading {}'.format(filename)
	return msg


async def main (urls):
	"""
	Creates a group of coroutines and waits for them to finish
	"""
	coroutines = [download_coroutine(url) for url in urls]  # takes a list of one or more URLs and queues them up
	completed, pending = await asyncio.wait(coroutines)  # wait for the coroutines to finish
	for item in completed:
		print (item.result())


if __name__ == '__main__':
	urls = ("http://www.irs.gov/pub/irs-pdf/f1040.pdf",
			"http://www.irs.gov/pub/irs-pdf/f1040a.pdf",
			"http://www.irs.gov/pub/irs-pdf/f1040ez.pdf",
			"http://www.irs.gov/pub/irs-pdf/f1040es.pdf",
			"http://www.irs.gov/pub/irs-pdf/f1040sb.pdf")

	event_loop = asyncio.get_event_loop()
	try:
		# we get an event loop and then call its run_until_complete method
		event_loop.run_until_complete(main(urls))  # we pass in the main coroutine to the event loop
		# starts running the main coroutine which queues up the second coroutine and gets it going
		# known as a chained coroutine
	finally:
		event_loop.close()
