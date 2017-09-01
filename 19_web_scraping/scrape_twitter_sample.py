import requests
from bs4 import BeautifulSoup


url = 'https://twitter.com/mousevspython'

req = requests.get(url)  # HTTP GET request on the url
html = req.text  # pulls the HTML as a string
soup = BeautifulSoup(html, 'html.parser')  # transforms into a nice object thanks to BeautifulSoup
tweets = soup.findAll('li', 'js-stream-item')  # grabs all the instances that match our search criteria

for item in range(len(soup.find_all('p', 'TweetTextSize'))):  # looks for the paragraph tag and class 'TweetTextSize'
    tweet_text = tweets[item].get_text().encode('utf-8')
    print(tweet_text)
    dt = tweets[item].find('a', 'tweet-timestamp')
    print('This was tweeted on ' + str(dt))
