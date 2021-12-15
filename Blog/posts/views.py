from django.shortcuts import render
from rest_framework import generics
from .serializers import PostSerialzer
from .models import Post
from .permissions import IsAuthenticatedOrReadOnly 

# Create your views here.


class PostList(generics.ListCreateAPIView):
    # queryset = Post.objects.filter(published = True)
    queryset = Post.objects.all()
    serializer_class = PostSerialzer
    permissions_class = IsAuthenticatedOrReadOnly

# RUD view


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerialzer
    permissions_class = IsAuthenticatedOrReadOnly



# class PostCreate():
#     pass


# class PostUpdate():
#     pass


# class PostDelete():
#     pass
