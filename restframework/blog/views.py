from django.shortcuts import render
from rest_framework.generics import ListAPIView

from blog.models import Post
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView

from .models import Post
from .serializers import PostSerializers


class PostListView(ListCreateAPIView):
    queryset = Post.objects.all()[:3]
    serializer_class = PostSerializers

class PostDetailView(RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers

# Create your views here.
