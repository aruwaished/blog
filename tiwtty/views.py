from django.shortcuts import render
from urllib.parse import quote
from django.http import JsonResponse
import requests
from requests_oauthlib import OAuth1

def tweet_search(request):
	search_term = "#Python"
	query = quote(search_term)
	url = "https://api.twitter.com/1.1/search/tweets.json?q=%s"%(query)


	aruwaished = request.user
	social_account = aruwaished.social_account_set.get(user=aruwaished.id)
	social_token = social_account.socialtoken_set.get(account=social_account.id)
	token =social_token.token 
	token_Secret= social_token.token_secret

	social_app = Social_App.objectd.get(provider=social_account.provider)
	client_id = social_app.client_id
	client_secret = social_app.secret

	auth_value = OAuth1(client_id, client_secret, token, token_secret)
	resp = requests.get(url)




	
	return JsonResponse(res.json(), safe=False)