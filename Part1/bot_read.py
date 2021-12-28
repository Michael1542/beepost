#App to draw top landscape picture per week and then add to an image library
import praw
import datetime
import requests

class Reader:
    reddit = praw.Reddit('bot1')
    subreddit = reddit.subreddit("imaginarylandscapes")
    images = []

    def write_image(self):
        for submission in self.subreddit.hot(limit=1):
            print("Title: ", submission.title)
            print("Score: ", submission.score)
            print("URL: ", submission.url)
            print("Date: ", datetime.datetime.fromtimestamp(submission.created_utc))
            print("---------------------------------\n")
            img_data = requests.get(submission.url)
            file = open("sample_image.png", "wb")
            file.write(img_data.content)
            file.close()