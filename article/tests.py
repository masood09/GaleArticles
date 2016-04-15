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
