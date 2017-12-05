from django.shortcuts import render
from urllib.parse import quote
from django.http import JsonResponse
import requests
from requests_oauthlib import OAuth2

def insta_search(request):
	search_term = "#selfi"
	query = quote(search_term)
	url = "https://api.instagram.com/oauth/authorize/?client_id=CLIENT-ID&redirect_uri=REDIRECT-URI&response_type=code"


	aruwaished = request.user
	social_account = aruwaished.social_account_set.get(user=aruwaished.id)
	social_token = social_account.socialtoken_set.get(account=social_account.id)
	token =social_token.token 
	token_Secret= social_token.token_secret

	social_app = Social_App.objectd.get(provider=social_account.provider)
	client_id = social_app.client_id
	client_secret = social_app.secret

	auth_value = OAuth2(client_id, client_secret, token, token_secret)
	resp = requests.get(url)




	
	return JsonResponse(res.json(), safe=False)