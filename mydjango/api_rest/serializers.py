from rest_framework import serializers
from django.contrib.auth.models import User

from blog.models import Post, Comment


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id','last_name', 'first_name')


class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'slug','author','body','publish', 'created','updated','status')

