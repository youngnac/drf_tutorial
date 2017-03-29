from django.conf.urls import include
from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from . import views


user_list = views.UserViewSet.as_view({'get': 'list'})

user_detail = views.UserViewSet.as_view({'get': 'retrieve'})
app_name = 'member'

urlpatterns = [
    url(r'^$', user_list, name='user_list'),
    url(r'^(?P<pk>[0-9]+)/$', user_detail, name='user_detail'),
]
