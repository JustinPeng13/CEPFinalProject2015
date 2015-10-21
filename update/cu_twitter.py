import tweepy

CONSUMER_KEY = "rXGTkoYtC0eH0zNdYgJhzpdnQ"
CONSUMER_SECRET = "G10iGqbuwjq2YPCdHELA49RfgPxJeD76l3nrdWGp00iyqehJZc"

def get_login_link( callback=None ):
	auth = tweepy.OAuthHandler( CONSUMER_KEY , CONSUMER_SECRET , callback )
	try:
		return ( auth.get_authorization_url() , auth.request_token )
	except tweepy.TweepError as e:
		print("Error: failed to get authorization URL.",e)
		return False

def get_access_token( token , verifier ):
	auth = tweepy.OAuthHandler( CONSUMER_KEY , CONSUMER_SECRET )
	auth.request_token = token
	try:
		auth.get_access_token( verifier )
	except tweepy.TweepError as e:
		print("Error: failed to get access token.",e)
		return False
	return ( auth.access_token , auth.access_token_secret )

def get_tweepy_api_wrapper( token=None, secret=None , auth=None ):
	if token and secret:
		auth = tweepy.OAuthHandler( CONSUMER_KEY , CONSUMER_SECRET )
		auth.set_access_token( token , secret )
	if not auth:
		print("Error: Invalid call to get_tweepy_api_wrapper")
		return
	return tweepy.API( auth )

def get_tweets( api , sinceid=None , maxid=None , count=50 ):
	return api.home_timeline( since_id = sinceid , max_id = maxid , count = count )

def post_tweet( api , text , reply=None ):
	return api.update_status( status=text , in_reply_to_status_id = reply )

def delete_tweet( api , tweetid ):
	return api.destroy_status( tweetid )

def retweet( api , tweetid ):
	return api.retweet( tweetid )

def favourite( api , tweetid , yes=True ):
	if yes:
		api.create_favorite( tweetid )
	else:
		api.destroy_favorite( tweetid )

def status_get_text( status ):
	return status.text

def status_get_replyto( status ):
	return status.in_reply_to_status_id

def status_get_id( status ):
	return status.id

def status_get_poster( status ):
	return status.author

def status_get_time( status ):
	return status.created_at