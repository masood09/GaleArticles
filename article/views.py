from django.shortcuts import render
from .helpers import *



def listing(request):
    random_article = helper_get_random_article()
    article_list = helper_get_published_article()
    next_articles = helper_get_random_articles()

    return render(
        request,
        'list.html',
        {
            'random_article': random_article,
            'article_list' : article_list,
            'next_articles' : next_articles,
        }
    )
