from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import json
import re

class StdOutListener(StreamListener):
    """ A listener handles tweets are the received from the stream.
    This is a basic listener that just prints received tweets to stdout.

    """
    def __init__(self):
        self.ofile = open('twitterSample2','a')
    
    def on_data(self, data):
        data = json.loads(data)
        if 'text' in data:
            s = re.sub('[^0-9a-zA-Z#]+', ' ', data['text'])
            if not re.match(r'\s+',s):
                self.ofile.write(s+'\n')
                #print s
        return True

    def on_error(self, status):
        self.ofile.close()
        print status

if __name__ == '__main__':
    
    
    consumer_key="r84gz4c2RtsFzAJHDB80rJp9Z"
    consumer_secret="kImiedcdc5IE48wtJN3LEOzUXeU8seB9Rcxuq1QsXgCuvAiSgQ"
    access_token="74343881-yifGWeb8AHAxvWodeO5MkVlVjSYyFOVUvoEvoPE1d"
    access_token_secret="4n1XkDAvng0nF05BTDlEFnZtIHj9KeN8mFRyM9985OQbR"

    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    #stream.filter(track=['basketball'])
    stream.sample()

'''
Steaming API
'''
'''
twf = open('tweets_420.cl','w');
index = 0
for i in range(0,5):
    if i==0:
        public_tweets = api.home_timeline(count=200)
    else:
        public_tweets = api.home_timeline(count=200,max_id=public_tweets[-1].id)
    for tweet in public_tweets:
        text = tweet.text
        text = text.encode('UTF-8', 'ignore')
        twf.write(text+"\n")
    
    
    #ref https://dev.twitter.com/docs/api/1.1/get/search/tweets
    #temp=api.search("easter",lang="eu",count=100)

twf.close()



latitude = 34.022507
longtitude = -118.284302

trdf = open('trends.cl','w')

pls = api.trends_closest(lat=latitude,long=longtitude)
trends = api.trends_place(id=pls[0]['woeid'])
for trend in trends[0]['trends']:
    trdf.write(trend['name']+"\n")
        
trdf.close()
'''
    
