import tweepy

#get your keys from the locally stored keys in a text file
with open('keys.txt', 'r') as f:
    my_keys = f.readlines()

#strip the strings of string format characters : - \n, \t, etc
api_key = my_keys[0].strip()
api_secret = my_keys[1].strip()
access_token = my_keys[2].strip()
access_token_secret = my_keys[3].strip()


auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)   
keyword = "Narendra Modi"

results = api.search(keyword + ' -filter:retweets', tweet_mode='extended', lang = 'en', count = 5, include_entities = True)

print(len(results))

for result in results:
    print(result.full_text)
    print("Twitter Handle :- " + result.user.screen_name+"\n" + "Name of the account :- " + result.user.name)
    #print(result)