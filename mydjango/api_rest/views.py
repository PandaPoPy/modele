from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.decorators import detail_route

from blog.models import Post
from .serializers import PostSerializer


class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


#class PostEnrollView(APIView):
    #authentication_classes = (BasicAuthentication,)
    #permission_classes = (IsAuthenticated,)

    #def post(self, request, pk, format=None):
        #post = get_object_or_404(Post,pk)
        #post.author.add(request.user)
        #return Response({'enrolled':True})


class PostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @detail_route(methods=['post'], authentication_classes = [BasicAuthentication], permission_classes = [IsAuthenticated])
    def enroll(self, request, *args, **kwargs):
        post = self.get_object()
        post.author.add(request.user)
        return Response({'enrolled': True})



