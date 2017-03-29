from django.conf.urls import url
from rest_framework import renderers
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

# snippet_list = views.SnippetViewSet.as_view({'get': 'list', 'post': 'create'})
# snippet_detail = views.SnippetViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
# snippet_highlight = views.SnippetViewSet.as_view({
#     'get': 'highlight'
# }, renderer_classes=[renderers.StaticHTMLRenderer])
#
# app_name = 'snippet'
# urlpatterns = [
#     # url(r'^$', views.SnippetList.as_view(), name='snippet_list'),
#     # url(r'^(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view(), name='snippet_detail'),
#     # url(r'^(?P<pk>[0-9]+)/highlight/$', views.SnippetHighlight.as_view(), name='snippet_highlight'),
#     url(r'^$', snippet_list, name='snippet_list'),
#     url(r'^(?P<pk>[0-9]+)/$', snippet_detail, name='snippet_detail'),
#     url(r'^(?P<pk>[0-9]+)/highlight/$', snippet_highlight, name='snippet_highlight'),
#
# ]

urlpatterns = format_suffix_patterns(urlpatterns)
