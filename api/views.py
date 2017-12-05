from rest_framework.generics import DestroyAPIView, ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, CreateAPIView
from posts.models import Post 
from .serialzers import PostListSerializer, PostDetailSerializer , PostCreateSerializer, CommentListSerializer, UserCreateSerializer, UserLoginSerializer
from .permissions import IsOwner
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.filters import SearchFilter, OrderingFilter
from django_comments.models import Comment
from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.response import Response

class UserLoginView(APIView):
	permission_classes = [AllowAny,]
	serializer_class = UserLoginSerializer

	def post(self, request, format=None):
		data = request.data
		serialzer = UserLoginSerializer(data=data)
		if serialzer.is_valid(raise_exception=True):
			new_data=serialzer.data
			return Response(new_data, status=HTTP_200_OK)
		return Response(serialzer.errors, status=HTTP_400_BAD_REQUEST)

class UserCreateView(CreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserCreateSerializer


class PostListView(ListAPIView):
	queryset = Post.objects.all()
	serializer_class = PostListSerializer
	filter_backends = [SearchFilter, OrderingFilter]
	search_fields = ['title', 'content', 'author__username']
	permission_classes=[AllowAny,]

class PostDetailView(RetrieveAPIView):
	queryset = Post.objects.all()
	serializer_class =PostDetailSerializer
	lookup_field = 'slug'
	looking_url_kwarg = 'post_slug'

class PostDeleteView(DestroyAPIView):
	queryset = Post.objects.all()
	serializer_class =PostDetailSerializer
	lookup_field = 'slug'
	lookup_url_kwarg = 'slug'
	permission_classes = [IsAuthenticated, IsAdminUser]



class PostUpdateView(RetrieveUpdateAPIView):
	queryset = Post.objects.all()
	serializer_class =PostDetailSerializer
	lookup_field = 'slug'
	lookup_url_kwarg = 'slug'

class PostCreateView(CreateAPIView):
	queryset = Post.objects.all()
	serializer_class =PostCreateSerializer
	permission_classes = [IsAuthenticated, IsAdminUser]

	def preform_create(self, serialzer):
		serialzer.save(autor=self.request.user)

class CommentListView(ListAPIView):
	queryset = Comment.objects.all()
	serializer_class = CommentListSerializer
	permission_classes = [AllowAny,]

	def get_queryset(self, *args, **kwargs):
		queryset = Comment.objects.all()
		query = self.request.GET.get("query")
		if query:
			queryset = queryset.filter(
				Q(object_pk=query)|
				Q(user=query)
				).distinct()
		return queryset

	lookup_field = 'slug'
	lookup_url_kwarg = 'slug'


