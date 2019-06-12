from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream



#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print (data)
        return True

    def on_error(self, status):
        print (status)
        return True


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    print ("Executing the main function.....")
    l = StdOutListener()
    consumer_key="Y5BQOVg1X1B3fD1aSYNgmxhyK"
    consumer_secret="wzqNmNP3Cr8DLEzIEaQpOxEmzNeZzeT0XNYVbR2l36F6Tl4Qib"
    access_token= "2732496352-TRPD4IkrfBPFiEvsSeFc0aklZO41UAif3Zc1Kcu"
    access_token_secret= "NdCRSWXkCUhTnvA8c58qyIAPrg4gvT8uSF6HUzToHX6EJ"
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python'])
    stream.disconnect()



#     data = pd.read_csv('AID.csv')

# # Store in list tweets that still exist; print out IDs of those that have been deleted by tweeter
#     tweet_list = []
#     for i, row in data.iterrows():
#         if i < 100:
#             try:
#                 id_of_tweet = row['id']
#                 print(id_of_tweet)
#                 tweet_list.append(api.get_status(id_of_tweet))
#             except:
#                 print(str(id_of_tweet) + ' not present any more 