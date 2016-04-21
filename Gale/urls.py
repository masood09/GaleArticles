"""Gale URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from article import views
from article.api_views import ArticleViewSet

urlpatterns = [
    url(r'^$', views.listing, name='index'),
    url(r'^blog/(?P<slug>[\w\-]+)/$', views.detail, name='article__detail'),

    url(r'^api/articles/(?P<pk>[\d]+)/$', ArticleViewSet.as_view({'get': 'retrieve'}), name="api__article_detail"),
    url(r'^api/articles/search/$', ArticleViewSet.as_view({'get': 'search'}), name="api__article_search"),

    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
