import tweepy
"""
You will need to register with Twitter to get an authentication key and 
secret that you can use with their OAuth implementation.

More about the OAuth with Twitter API: http://tweepy.readthedocs.io/en/v3.5.0/auth_tutorial.html
"""
key = 'random_key'
secret = 'random_secret'
access_token = 'access_token'
access_secret = 'super_secret'

auth = tweepy.OAuthHandler(key, secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

my_tweets = api.user_timeline()  # grabs our 20 (by default) latest tweets

for tweet in my_tweets:
	dir(tweet)
	# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', 
	# '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__le__', 
	# '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', 
	# '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_api', '_json', 
	# 'author', 'contributors', 'coordinates', 'created_at', 'destroy', 'entities', 'favorite', 
	# 'favorite_count', 'favorited', 'geo', 'id', 'id_str', 'in_reply_to_screen_name', 
	# 'in_reply_to_status_id', 'in_reply_to_status_id_str', 'in_reply_to_user_id', 'in_reply_to_user_id_str', 
	# 'is_quote_status', 'lang', 'parse', 'parse_list', 'place', 'possibly_sensitive', 'retweet', 
	# 'retweet_count', 'retweeted', 'retweets', 'source', 'source_url', 'text', 'truncated', 'user']
	print (tweet.text)

api.update_status('I just tweeted using Python')
api.update_with_media(filename, 'I can tweet files with Python')
