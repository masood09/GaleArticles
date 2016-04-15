from django.shortcuts import render
from .helpers import *



def listing(request):
    random_article = helper_get_random_article()

    return render(
        request,
        'list.html',
        {
            'random_article': random_article
        }
    )
