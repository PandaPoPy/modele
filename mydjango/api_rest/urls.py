from django.conf.urls import url, include

from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register('posts', views.PostViewSet)

urlpatterns = [
    #url(r'^posts/$', views.PostListView.as_view(), name='post_list'),
    #url(r'^posts/(?P<pk>\d+)/$', views.PostDetailView.as_view(), name='post_detail'),
    #url(r'^posts/(?P<pk>\d+)/enroll/$', views.PostEnrollView.as_view(), name='post_enroll'),
    url(r'^', include(router.urls))
]
