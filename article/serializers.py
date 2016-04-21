from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    """
    Serializing the Articles
    """

    author = serializers.StringRelatedField(many=False)
    publication_date = serializers.DateField(format='%B %d, %Y')

    class Meta:
        model = Article
        fields = (
            'id',
            'author',
            'publication_date',
            'hero_image',
            'optional_image',
            'title',
            'body_text',
        )
