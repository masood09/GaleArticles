import datetime

from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.response import Response

from .models import Article
from .serializers import ArticleSerializer

class ArticleViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for retrieving articles.
    """

    def retrieve(self, request, pk=None):
        queryset = Article.objects.filter(
            publication_date__lte = datetime.date.today()
        )
        article = get_object_or_404(queryset, pk=pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def search(self, request, term=None):
        queryset = Article.objects.filter(
            publication_date__lte = datetime.date.today()
        ).filter(
            title__icontains = term
        )

        serializer = ArticleSerializer(queryset, many=True)
        return Response(serializer.data)
