"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.routers import DefaultRouter

from member import views as m_views
from snippets import views as s_views

router = DefaultRouter()
router.register(r'user', m_views.UserViewSet)
router.register(r'snippets', s_views.SnippetViewSet)

# router_snippet = DefaultRouter()
# router_user = DefaultRouter()
# router_snippet.register(r'snippets',s_views.SnippetViewSet )
# router_user.register(r'user', m_views.UserViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    # url(r'^$', views.APIRoot.as_view()),
    # url(r'snippets/', include(router_snippet.urls, namespace='snippet')),
    # url(r'^user/', include(router_user.urls, namespace='user')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
