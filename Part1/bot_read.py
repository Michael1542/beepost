#App to draw top landscape picture per week and then add to an image library
import praw
import datetime

reddit = praw.Reddit('bot1')

subreddit = reddit.subreddit("imaginarylandscapes")

images = []

for submission in subreddit.top(limit=5):
    print("Title: ", submission.title)
    print("Score: ", submission.score)
    print("URL: ", submission.url)
    print("Date: ", datetime.datetime.fromtimestamp(submission.created_utc))
    print("---------------------------------\n")
