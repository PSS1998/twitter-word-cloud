import numpy as np
import matplotlib.pyplot as plt
import re
from PIL import Image
from persian_wordcloud.wordcloud import PersianWordCloud
from IPython.display import Image as im
import twitterscraper 
import json


def clean_tweets(raw_list):
	raw_string = ''.join(raw_tweets)
	no_links = re.sub(r'http\S+', '', raw_string)
	return no_links

def create_words(clean_string):
	words = clean_string.split(" ")
	words = [w for w in words if len(w) > 2]  # ignore a, to, at...
	return words

#Collect the data from the user timeline

with open("tweets_username.json", "r") as read_file:
    user_timeline = json.load(read_file)


raw_tweets = []
for tweets in user_timeline:
    raw_tweets.append(tweets['text'])

#Generate the cloud
clean_text = clean_tweets(raw_tweets)
words = create_words(clean_text)
clean_string = ','.join(words)
mask = np.array(Image.open('twitter-logo.jpg'))
wc = PersianWordCloud(background_color="white", max_words=2000, mask=mask)
wc.generate(clean_string)

plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show(block=True)

