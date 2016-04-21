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

    def test_detail_page_proper(self):
        """When the page exists and is published (we are using fixtures to seed the data) we should get 200"""
        response = self.client.get('/blog/omnia-peccata-paria-dicitis/')
        self.assertEquals(response.status_code, 200)

    def test_detail_page_not_published(self):
        """When the page is not published yet (ie., publishing date is in future), we need to send 404 response"""
        response = self.client.get('/blog/si-quicquam-extra-virtutem-habeatur/')
        self.assertEquals(response.status_code, 404)

    def test_detail_page_not_exist(self):
        """When the page does not exist, visiting the page should return 404"""
        response = self.client.get('/blog/asdf/')
        self.assertEquals(response.status_code, 404)

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
