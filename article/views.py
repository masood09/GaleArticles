from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .helpers import *



def listing(request):
    random_article = None
    article_list = helper_get_published_article()

    paginator = Paginator(article_list, 10)

    page = request.GET.get('page')

    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    next_articles = helper_get_random_articles()

    if articles.number == 1:
        random_article = helper_get_random_article()

    return render(
        request,
        'list.html',
        {
            'random_article': random_article,
            'articles' : articles,
            'next_articles' : next_articles,
        }
    )
