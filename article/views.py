from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404
from django.shortcuts import render
from .helpers import *



def index(request):
    return render(
        request,
        'index.html'
    )


def detail(request, slug):

    try:
        article = Article.objects.filter(
            publication_date__lte = datetime.date.today()
        ).get(slug=slug)
    except Article.DoesNotExist:
        raise Http404("Article does not exist")

    next_articles = helper_get_random_articles()

    return render(
        request,
        'detail.html',
        {
            'article': article,
            'next_articles': next_articles,
        }
    )

def search(request):
    term = request.GET.get("q", '')

    return render(
        request,
        'search.html',
        {
            'term': term,
        }
    )
