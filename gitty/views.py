from django.shortcuts import render
from django.http import JsonResponse
import requests

def member_list(request):

	aruwaished = request.user
	social_account = aruwaished.social_account_set.get(user=aruwaished.id)
	social_token = social_account.socialtoken_set.get(account=social_account.id)
	token =social_token.token 
	url = "https://api.github.com/orgs/joinCODED/members"
	res = requests.get(url, headers={"Authorization": "token "+token})
	return JsonResponse(res.json(), safe=False)