from django.conf.urls import url
from insta import views
urlpatterns = [ 
url(r'^search/$', views.insta_search, name='tweetsearch'),
]