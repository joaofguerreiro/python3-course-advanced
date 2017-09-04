import praw

# NOTE: Pass in your Reddit client_id and 
# client_secret for this API to work
red = praw.Reddit(client_id='my client id', client_secret='my client secret', user_agent='pyred')
# user_agent can be set to any string I like

for i in red.front.hot():
    print(i)

# 6807 :: Supreme Court Strikes Down Strict Abortion Law
# 5583 :: Grandpa plays a virtual reality game
# 5532 :: Our trip to the petting zoo did not go as planned
# 5728 :: My pepper looks like a fist
# 5501 :: New Samurai Jack receives a TV-MA rating for it's dark tone and viole...
# 5868 :: The sunset at Glastonbury Festival on Saturday was incredible.
# 5485 :: Let me out of this kennel please!
# 5427 :: Good morning, I love you!
# 5389 :: TIL an airplane crashed into the Empire State Building in 1945. Among...
# 5409 :: Meanwhile in France...
# 5340 :: Barclays and RBS shares suspended from trading after tanking more tha...
# 5228 :: The wood grain on this door looks like a damp woman ran into it
# 5225 :: Seeing a ceiling fan in action for the first time
# 5258 :: Half funny, half disturbing
# 5067 :: Old dogs are cute too.
# 5036 :: Our veterinary clinic sent us a sympathy card with our dog's paw prin...
# 5082 :: Experiments confirm that the barium-144 nucleus is pear shaped
# 5340 :: He doesn't like his new bow tie
# 4924 :: One of my favorite jokes from Dr. Cox.
# 4921 :: Pope says Church should ask forgiveness from gays for past treatment
# 4912 :: Hawaii becomes first U.S. state to place gun owners on FBI database
# 5043 :: I'll give a million dollars to the man who can do something about mot...
# 4836 :: 100 kids have sleepover at Dallas Cowboys' AT&T Stadium as part of As...
# 4719 :: TIL illegal income, such as bribes, are considered taxable income. Au...
# 4681 :: War Veteran, pencil on paper, A2



"""Subreddits"""
python = red.subreddit('python')
submissions = python.get_hot(limit=5)
print (submissions)
#<generator object get_content at 0x7fab632614c0>

for submission in submissions:
    print (submission)

# 298 :: Post learning questions to /r/LearnPython
# 146 :: Python 3.5.2 is released
# 84 :: My peer-to-peer networking module is now on pip
# 36 :: WTF! Stop the next line
# 0 :: [Advice] What path should I choose for further programming?


"""Checking a submission from some Subreddit"""
id = '4q2lxb'
submission = red.get_submission(submission_id=id)
comments = submission.comments  # grabs all the Comment objects (as a list) in the Submission object
print (comments)
# [<praw.objects.Comment object at 0x7fab626c2668>]

print (comments[0].author)
# Redditor(user_name='brombaer3000')

print (comments[0].body)
# ('[Actual release '
# 'notes](https://docs.python.org/3/whatsnew/changelog.html#python-3-5-2)')

print (comments[0].replies)  # grabs all the Comment objects (as a list) as replies in the parent Comment object 
# [<praw.objects.Comment object at 0x7fab626c2588>]
