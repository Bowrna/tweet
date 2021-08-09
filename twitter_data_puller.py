import tweepy

api_key = 'xxxxxxxxxxxxxxxxxxxxxxxxxxx'
api_key_secret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxx'
# access_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxx'
# access_token_secret ='xxxxxxxxxxxxxxxxxxxxxxxxxxx'
# auth = tweepy.OAuthHandler(api_key, api_key_secret)
# auth.set_access_token(access_token, access_token_secret)

auth = tweepy.AppAuthHandler(api_key, api_key_secret)
api = tweepy.API(auth)
user = api.get_user('malai_san')
print(user.screen_name)
print(user.followers_count)

for status in tweepy.Cursor(api.user_timeline, id ='malai_san').items(5):
    print(status._json.keys())
    tweet_status = api.get_status(status._json['id'])
    # print(tweet_status)
    print(status._json.get('text'))
    # print(status.retweeted_status)
    # print(type(status))
    # import pdb;pdb.set_trace()

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)