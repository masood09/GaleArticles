import datetime

from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.response import Response

from .models import Article
from .serializers import ArticleSerializer

class ArticleViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for retrieving and searching articles.
    """

    def retrieve(self, request, pk=None):
        """
        View used to retrieve a single article item. 404 if not found.
        """
        queryset = Article.objects.filter(
            publication_date__lte = datetime.date.today()
        )
        article = get_object_or_404(queryset, pk=pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def search(self, request):
        """
        View used to search articles. We will search only using Title.
        """
        term = request.GET.get("q", '')

        queryset = Article.objects.filter(
            publication_date__lte = datetime.date.today()
        ).filter(
            title__icontains = term
        )

        serializer = ArticleSerializer(queryset, many=True)
        return Response(serializer.data)
