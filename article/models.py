from django.db import models
from django.template.defaultfilters import slugify



class Category(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        """We want the string representation of Category model to be its title"""
        return self.title

    class Meta:
        """Django will call this as Categorys, lets make it grammatically correct!"""
        verbose_name_plural = "categories"



class Article(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True, editable=False, max_length=255)
    author = models.ForeignKey('auth.User')
    publication_date = models.DateField()
    category = models.ForeignKey(Category)
    hero_image = models.ImageField(upload_to='images/')
    optional_image = models.ImageField(upload_to='images/', blank=True, null=True)
    body_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        """We want the string representation of Article model to be its title"""
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
