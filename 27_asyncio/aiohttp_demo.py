import aiohttp
import asyncio
import async_timeout
import os


async def download_coroutine(session, url):
	with async_timeout.timeout(10):
		async with session.get(url) as response:  # http GET request on the url
			filename = os.path.basename(url)  
			with open(filename, 'wb') as f_handle:
				while True:
					chunk = await response.content.read(1024)  # downloads file in chunks of w/e size we want
					if not chunk:
						break
					f_handle.write(chunk)  # writes to the local disk
			return await response.release()  # finishes the response processing


async def main(loop):
	urls = ("http://www.irs.gov/pub/irs-pdf/f1040.pdf",
			"http://www.irs.gov/pub/irs-pdf/f1040a.pdf",
			"http://www.irs.gov/pub/irs-pdf/f1040ez.pdf",
			"http://www.irs.gov/pub/irs-pdf/f1040es.pdf",
			"http://www.irs.gov/pub/irs-pdf/f1040sb.pdf")

	async with aiohttp.ClientSession(loop=loop) as session:  # creates a ClientSession object
		for url in urls:
			print(await download_coroutine(session, url))  # calls the download coroutine function for each url


if __name__ == '__main__':
	loop = asyncio.get_event_loop()  # asynchronous event loop
	loop.run_until_complete(main(loop))
