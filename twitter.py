#/usr/bin/python3
# Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# Enter Twitter API Keys
access_token = "488650850-SdUNecgQyDGo7n5Rl85hlFKb51znw6fQZD8LH1nV"
access_token_secret = "wyShJScbtuDjfAeKQ6MCOufuEEhvxPYGPeLBGs6olRlbk"
consumer_key = "YV34hSKe6wXoKp3qSekqtGtMR"
consumer_secret = "QIbpHiRTmAAO2sfNsz49YeCz4a311QY8UY2yTpM75K8BEkELn3"


# Create the class that will handle the tweet stream
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':
    # Handle Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    stream.filter(track=['#COVID-19','#USA'])


