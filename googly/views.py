from django.shortcuts import render
from django.http import JsonResponse
import requests

def place_text_search(request):
	key = "AIzaSyBSRyvXgyPY7u-eE63CT_PUmDvoajf6MFY"
	query = request.GET.get( 'query','coded')
	url = "https://maps.googleapis.com/maps/api/place/textsearch/json?query=%s&key=%s&region=kw"%(query, key)

	next_page = request.GET.get('nextpage')
	if next_page is not None:
		url += "&pagetoken="+next_page

	response = requests.get(url)

	context = {

	"response": response.json()
	}

	return render (request, 'place_search.html', context)

def place_detail(request):
	key = "AIzaSyBSRyvXgyPY7u-eE63CT_PUmDvoajf6MFY"
	place_id =request.GET.get('place_id', )
	url = "https://maps.googleapis.com/maps/api/place/details/json?key=%s&placeid=%s"%(key, place_id)
	map_key= "AIzaSyDOyxKHBH4laojhcRxoX9iNj0OlMWFLiyg"

	response = requests.get(url)
	context = {"response": response.json(), "map": map_key}

	return render (request, 'place_detail.html', context)