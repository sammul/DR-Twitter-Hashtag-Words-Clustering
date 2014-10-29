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
        self.ofile = open('twitterSample','a')
    
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
    
    
    consumer_key=""
    consumer_secret=""
    access_token=""
    access_token_secret=""

    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    #stream.filter(track=['basketball'])
    stream.sample()
    
