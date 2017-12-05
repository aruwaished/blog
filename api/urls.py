from . import views
from django.conf.urls import url
from api.views import *

urlpatterns = [

	url(r'^$', views.PostListView.as_view(), name = "list"),
	url(r'^create/$', views.PostCreateView.as_view(), name = "create"),
	url(r'^(?P<slug>[-\w]+)/detail/$', views.PostDetailView.as_view(), name= "detail"),
	url(r'^(?P<slug>[-\w]+)/delete/$', views.PostDeleteView.as_view(), name= "delete"), 
	url(r'^(?P<slug>[-\w]+)/update/$', views.PostUpdateView.as_view(), name= "update"),
	url(r'^comments/list/$', views.CommentListView.as_view(), name= "comment"),
	url(r'^register/$', UserCreateView.as_view(), name= "register"),
	url(r'^login/$', UserLoginView.as_view(), name= "login"),


]