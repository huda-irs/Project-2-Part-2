import tweepy
import argparse
import os
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
from google.oauth2 import service_account
from textblob import TextBlob

#set tokens
creds = service_account.Credentials.from_service_account_file(path_to_json_file) # insert .json file path here including the .json file's name with double air quotes ("")

client = language.LanguageServiceClient(credentials=creds, )

auth = tweepy.OAuthHandler("consumer key", "consumer key secret") # put key in double air quotes
auth.set_access_token("access token key", "access token secret ")
api = tweepy.API(auth)
## ask user for tweet they want to send and save the tweet

user_tweet = input("Enter the tweet you would like to send:")

## send tweet they want to send

api.update_status(user_tweet)

## Analyze tweet through nlp

text = (user_tweet)

encoding_type = enums.EncodingType.UTF32

document = types.Document(
		content=user_tweet,
		type=enums.Document.Type.PLAIN_TEXT)

user_sentiment = client.analyze_sentiment(document=document).document_sentiment

## find recent tweets on same topic and anaylze their nlps

user_entities = client.analyze_entities(document = document, encoding_type=encoding_type)

Key_words = input("Key words:")
query_str = Key_words.split(' ')

query = ""

for i in range(len(query_str)):

	if(i < len(query_str)-1):
		query += query_str[i] 
		query += " OR "
	else: 
		query += query_str[i]
   
max_tweet = 20

search_text = [0 for i in range(20)]
search_score = [0 for i in range(20)]
username = [0]
freinds_names = []

print("Here is a list of people who could be your friend: ")

for friend_search in tweepy.Cursor(api.search, q=query).items(max_tweet):
	
	document = types.Document( content=friend_search.text, type=enums.Document.Type.PLAIN_TEXT)

	# Detects the sentiment of the text
	search_sentiment = client.analyze_sentiment(document=document).document_sentiment

	if(search_sentiment.score == user_sentiment.score):  
		search_text[i] = friend_search.text
		search_score[i] = search_sentiment.score
		username = friend_search.text.lstrip("@").split(" ")[1]
		print("{}".format(username))



