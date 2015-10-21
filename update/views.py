from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
import json
from datetime import *

from update import cu_twitter

# Create your views here.
def update( req ):
	ct = datetime.now()
	jsonupdatelist = []
	if req.user.userprofile.twitter_token and req.user.userprofile.twitter_secret:
		since = req.GET.get('twittersince')
		try:
			since = int( since )
		except Exception:
			return HttpResponse( "{\"status\":0}" )
		tweetlist = cu_twitter.get_tweets( cu_twitter.get_tweepy_api_wrapper( req.user.userprofile.twitter_token , req.user.userprofile.twitter_secret ) , sinceid = since , count = 999999 )
		for i in range( len( tweetlist ) ):
			s = tweetlist[i]
			jsonupdatelist.append( { "app": "twitter" , "text": cu_twitter.status_get_text( s ) , "dt": ( ct - cu_twitter.status_get_time( s ) ).total_seconds() / 60 , "author": "@" + cu_twitter.status_get_poster( s ).screen_name , "id": cu_twitter.status_get_id( s ) } )
	dt = json.dumps( {"status":1,"response":jsonupdatelist} )
	return HttpResponse( dt )

def link_twitter( req ):
	login_link = cu_twitter.get_login_link()
	tries = 10
	while not login_link and tries:
		login_link = cu_twitter.get_login_link()
		tries -= 1
	if not login_link and not tries:
		return redirect("/")
	req.session['oatwitter'] = login_link[1]
	return redirect(login_link[0])

def oa_twitter( req ):
	oauth_info = cu_twitter.get_access_token( req.session['oatwitter'] , req.GET.get('oauth_verifier') )
	tries = 10
	while not oauth_info and tries:
		oauth_info = cu_twitter.get_access_token( req.session['oatwitter'] , req.GET.get('oauth_verifier') )
		tries -= 1
	del req.session['oatwitter']
	if not oauth_info and not tries:
		return redirect("/")
	req.user.userprofile.twitter_token = oauth_info[0]
	req.user.userprofile.twitter_secret = oauth_info[1]
	req.user.userprofile.save()
	return redirect("/")

def post_twitter( req ):
	if req.POST.get("text"):
		cu_twitter.post_tweet( cu_twitter.get_tweepy_api_wrapper( req.user.userprofile.twitter_token , req.user.userprofile.twitter_secret ) , req.POST.get("text") )
	return redirect("/")