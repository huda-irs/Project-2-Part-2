In the Find a Buddy Project, the Twitter API and Google NLP were used to send a tweet from the user and from the keywords described from the user the google nlp matches your sentimental level of your tweet to others who have tweeted with some key terms that were specified. By matching senitment level of the tweets from the query to the user's tweet the user will have a list of twitter accounts printed to show their similar interests.

## Set up
1. First you create a google cloud account and install [Google Cloud SDK](https://cloud.google.com/sdk/docs/install) and the necessary packages for [client libraries](https://cloud.google.com/apis/docs/cloud-client-libraries)
2. set up a project using either the Google Cloud Console on the web browser or the gcloud command for the Google Cloud SDK Shell
3. Create a service account and make the service account the account linked to the authorization keys (from this step you should recieve a json file)
4. Create a Twitter Developer Account
5. Create project and retrieve its API key, API key secret, Access token, and Access token secret
6. Install python3, tweepy, and other python libraries needed for this project under the Google Cloud SDK Shell
7. clone this github and fill in the required fields (the twitter keys and path to json file)

## How it works

To find someboy to qualify as a buddy then they must share similar attitude of the same topic as the tweet the user just posted. The user may feel like tweeting something at the moment and suddenly wants to relate to someone else in the moment on the same topic. The post of the tweet is then followed by a key terms request by the machine. The user adds key words which are further used for the query of tweets. Once the list is generated, measuring similar attitudes are observed through Google NLP entities, this obtains the emotional level of the text fed into the processor for Google NLP. When the user's tweet and the tweet from the query are equal in emotional level then the tweet is saved to extract the screen name of the tweet from query. The list of screen names are then printed for the user to send a requent if they please.

![Program Blck diagram](https://github.com/huda-irs/Project-2-Part-2/blob/main/Proj2_diagram.png)

## Important Note:
When retrieving keys for the Twitter project created, be sure to modify the App Permussions from 'Read Only' to 'Read + Post Tweets and profile information'

## Possible Future Work:
- [ ] Have the script automatically choose key terms using Google NLP Entity analysis
- [ ] Provided a range for the query tweets to fall under rather than exactly equal
- [ ] Find a cleaner way to process the tweet for the screen name
- [ ] Have a ranking system for which users from the query are most relatable based on the recently submitted tweet
