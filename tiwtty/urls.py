from django.conf.urls import url
from tiwtty import views

urlpatterns = [ 
url(r'^search/$', views.tweet_search, name='tweetsearch'),
]