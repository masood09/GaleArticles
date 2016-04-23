from django.test import TestCase

from .models import Category
from .models import Article
from .serializers import ArticleSerializer


class CategoryModelTest(TestCase):
    """The unit test cases for Category Model"""

    def test_string_representation(self):
        '''Test whether the string representation is equal to its title'''
        category = Category(title="My Category Title")
        self.assertEquals(str(category), category.title)

    def test_category_name_plural(self):
        """Test whether the plural name is correct"""
        self.assertEquals(str(Category._meta.verbose_name_plural), "categories")



class ArticleModelTest(TestCase):
    """The unit test cases for Article Model"""

    def test_string_representation(self):
        '''Test whether the string representation is equal to its title'''
        article = Article(title="My Article Title")
        self.assertEquals(str(article), article.title)



class ResponseCodeTest(TestCase):
    """The unit test cases for checking the correct response codes for various URL's"""

    fixtures = ['fixtures.json']

    def test_homepage(self):
        """When user visits homepage he should get 200"""
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_api_articles(self):
        """When REST API endpoint for articles list is hit, response code should be 200"""
        response = self.client.get('/api/articles/')
        self.assertEquals(response.status_code, 200)

    def test_api_article_random(self):
        """When REST API endpoint for random article is hit, response code should be 200"""
        response = self.client.get('/api/articles/random/')
        self.assertEquals(response.status_code, 200)

    def test_api_article_details(self):
        """When REST API endpoint for article detail is hit, response code should be 200"""
        response = self.client.get('/api/articles/1/')
        self.assertEquals(response.status_code, 200)

    def test_api_article_search(self):
        """When REST API endpoint for article search is hit, response code should be 200"""
        response = self.client.get('/api/articles/search/')
        self.assertEquals(response.status_code, 200)


class ArticleSerializerTest(TestCase):
    """The unit test cases for checking the ArticleSerializer"""

    fixtures = ['fixtures.json']

    def test_article_author_serializer(self):
        """Test whether the author name and date format is correct"""
        article = Article.objects.get(pk=1)
        serialized = ArticleSerializer(article)
        self.assertEquals(serialized['author'].value, 'tamaraollis')
        self.assertEquals(serialized['publication_date'].value, 'January 01, 2013')
