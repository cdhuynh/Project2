import tweepy

auth = tweepy.OAuthHandler("6LoIdh1Mip5jAyZ7YKwinqjRz", "WAc26venjlyTU56zC8KCvpT2Kk8mHRqTe9MjgQs3hPJSf64BmB")
auth.set_access_token("1440794762852724736-H6vaoaeNa4BmnsUzHRK6kVZN8yzWv7", "SrHMoOA2RTUmRyBUq3yoDNdHJVxIJS7aVU9EZCukIcwRq")

api = tweepy.API(auth)

# Based on the tweepy getting started program.
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.user.screen_name)

print ("----Test---")
# Simple test program based on specific user 'NASA'.
user = api.get_user(user = "NASA")
screen_name = "NASA"
nasa_ID = user.id_str
print("NASA's ID: " + nasa_ID)
nasa_count = 5

# Retrieve the last 5 recent tweets from NASA, and the username.
nasa_status = api.user_timeline(screen_name, count = nasa_count)
print(user.screen_name)
print(user.followers_count)
for test_status in nasa_status:
    print(test_status.id, test_status.text, end = "\n\n")

api.create_favorite(1441567735448686592)

print("#Testing a StreamListener ---------------")


class StreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print(status.text)


myStreamListener = StreamListener()
myStream = tweepy.Stream(auth = api.auth, listener = myStreamListener)
myStream.filter(follow=["11348282"])