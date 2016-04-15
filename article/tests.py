from django.test import TestCase

from .models import Category
from .models import Article


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
        response = self.client.get('/blog/18/')
        self.assertEquals(response.status_code, 200)

    def test_detail_page_not_published(self):
        """When the page is not published yet (ie., publishing date is in future), we need to send 404 response"""
        response = self.client.get('/blog/25/')
        self.assertEquals(response.status_code, 404)

    def test_detail_page_not_exist(self):
        """When the page does not exist, visiting the page should return 404"""
        response = self.client.get('/blog/1000/')
        self.assertEquals(response.status_code, 404)
